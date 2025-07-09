import os
import sqlite3
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import numpy as np
from sklearn.linear_model import RidgeClassifier
from sklearn.naive_bayes import GaussianNB
from random import choice

# ---- KONFIGURACIJA SLIKA ----
KARTA_PNG = {
    'Pik': 'icons/pik.png',
    'Tref': 'icons/tref.png',
    'Herc': 'icons/herc.png',
    'Karo': 'icons/karo.png'
}
KARTA_LISTA = ['Pik', 'Tref', 'Herc', 'Karo']
BOJA_MAP = {'Pik': 'Crna', 'Tref': 'Crna', 'Herc': 'Crvena', 'Karo': 'Crvena'}
SLOT_IGRE = ['100 Super Hot', '40 Super Hot', 'Wild Hot 40']

# ---- SQLITE ----
class DBHelper:
    def __init__(self, db_name="predictions.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slot_type TEXT,
                predicted_card TEXT,
                card_color TEXT,
                timestamp TEXT,
                correct INTEGER
            )
        """)
        self.conn.commit()

    def save_prediction(self, slot_type, predicted_card, card_color, timestamp, correct):
        self.cursor.execute(
            "INSERT INTO predictions (slot_type, predicted_card, card_color, timestamp, correct) VALUES (?, ?, ?, ?, ?)",
            (slot_type, predicted_card, card_color, timestamp, correct)
        )
        self.conn.commit()

    def fetch_stats(self):
        self.cursor.execute("SELECT slot_type, COUNT(*), SUM(correct) FROM predictions GROUP BY slot_type")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

# ---- AI ----
class AdvancedCardAI:
    def __init__(self, history_length=4):
        self.history_length = history_length
        self.mapping = {znak: i for i, znak in enumerate(KARTA_LISTA)}
        self.inv_mapping = {v: k for k, v in self.mapping.items()}
        self.models = {s: RidgeClassifier() for s in SLOT_IGRE}
        self.bayes_models = {s: GaussianNB() for s in SLOT_IGRE}
        self.data = {s: {'X': [], 'y': [], 'time': []} for s in SLOT_IGRE}
        self.trained = {s: False for s in SLOT_IGRE}
        self.performance = {s: [] for s in SLOT_IGRE}
        self.ai_strength = 1.0

    def set_strength(self, factor):
        self.ai_strength = factor

    def encode_sequence(self, seq):
        return [self.mapping.get(s, 0) for s in seq]

    def extract_time_features(self, timestamp):
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        return [dt.hour, dt.minute, dt.weekday()]

    def add_sample(self, sequence, target, timestamp=None, slot_type=None):
        if len(sequence) < self.history_length or slot_type not in self.data:
            return
        x = self.encode_sequence(sequence[-self.history_length:])
        self.data[slot_type]['X'].append(x)
        self.data[slot_type]['y'].append(self.mapping.get(target, 0))
        if timestamp:
            tf = self.extract_time_features(timestamp)
            self.data[slot_type]['time'].append(tf)

    def update_performance(self, slot, is_correct):
        self.performance[slot].append(is_correct)
        if len(self.performance[slot]) > 100:
            self.performance[slot] = self.performance[slot][-100:]

    def best_slot_by_behavior(self):
        return max(self.performance.items(), key=lambda x: sum(x[1]) / len(x[1]) if x[1] else 0)[0]

    def train(self):
        for slot in SLOT_IGRE:
            if len(self.data[slot]['X']) >= 10:
                X = np.array(self.data[slot]['X'])
                y = np.array(self.data[slot]['y'])
                self.models[slot].fit(X, y)
                if self.data[slot]['time']:
                    X_bayes = np.array(self.data[slot]['time'])
                    self.bayes_models[slot].fit(X_bayes, y)
                self.trained[slot] = True

    def predict(self, sequence, timestamp, slot_type):
        if slot_type == 'Automatski':
            slot_type = self.best_slot_by_behavior()
        if not self.trained[slot_type] or len(sequence) < self.history_length:
            return choice(KARTA_LISTA)
        x_lr = np.array(self.encode_sequence(sequence[-self.history_length:])).reshape(1, -1)
        model = self.models[slot_type]
        lr_pred = model.predict(x_lr)[0]
        lr_conf = 1.0
        if timestamp:
            x_bayes = np.array(self.extract_time_features(timestamp)).reshape(1, -1)
            bayes_model = self.bayes_models[slot_type]
            bayes_pred = bayes_model.predict(x_bayes)[0]
            bayes_conf = 1.0
        else:
            bayes_pred = lr_pred
            bayes_conf = 0
        if self.ai_strength < 1.0:
            return self.inv_mapping[bayes_pred]
        elif self.ai_strength > 1.0:
            return self.inv_mapping[lr_pred]
        else:
            return self.inv_mapping[lr_pred] if lr_conf >= bayes_conf else self.inv_mapping[bayes_pred]

# ---- UI ----
class CardSelector(BoxLayout):
    def __init__(self, label, **kwargs):
        super().__init__(orientation='vertical', size_hint=(None, None), size=(100, 140), **kwargs)
        self.selected_card = KARTA_LISTA[0]
        self.image = Image(source=KARTA_PNG[self.selected_card], size_hint=(1, 0.8))
        self.spinner = Spinner(text=self.selected_card, values=KARTA_LISTA, size_hint=(1, 0.2))
        self.spinner.bind(text=self.on_card_select)
        self.add_widget(Label(text=label, size_hint=(1, 0.2)))
        self.add_widget(self.image)
        self.add_widget(self.spinner)

    def on_card_select(self, instance, value):
        self.selected_card = value
        self.image.source = KARTA_PNG[value]

    def get_selected(self):
        return self.selected_card

class PredictionField(BoxLayout):
    def __init__(self, label, **kwargs):
        super().__init__(orientation='vertical', size_hint=(None, None), size=(100, 140), **kwargs)
        self.image = Image(source=KARTA_PNG[KARTA_LISTA[0]], size_hint=(1, 0.8))
        self.label = Label(text=label, size_hint=(1, 0.2))
        self.add_widget(self.label)
        self.add_widget(self.image)

    def set_card(self, card):
        self.image.source = KARTA_PNG[card]

class MainScreen(BoxLayout):
    def __init__(self, app, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.app = app
        self.ai = AdvancedCardAI()
        self.last_prediction = None

        self.add_widget(Label(text="Slot Predikcija - AI", font_size=24, size_hint_y=None, height=40))

        controls = GridLayout(cols=2, size_hint_y=None, height=60)
        self.slot_izbor = Spinner(text='Automatski', values=SLOT_IGRE + ['Automatski'])
        self.snaga_ai = Spinner(text='Normalno', values=['Slabo', 'Normalno', 'Jako'])
        controls.add_widget(Label(text="Izbor igre:"))
        controls.add_widget(self.slot_izbor)
        controls.add_widget(Label(text="AI Jačina:"))
        controls.add_widget(self.snaga_ai)
        self.add_widget(controls)

        self.card_selectors = []
        cards_layout = GridLayout(cols=4, size_hint_y=None, height=170)
        for i in range(4):
            sel = CardSelector(f"Karta {i+1}")
            cards_layout.add_widget(sel)
            self.card_selectors.append(sel)
        self.add_widget(Label(text="Unesi/prethodne karte (klikni za izbor):", size_hint_y=None, height=30))
        self.add_widget(cards_layout)

        predictions_layout = GridLayout(cols=2, size_hint_y=None, height=170)
        self.prediction_fields = []
        for i in range(2):
            pf = PredictionField(f"Predikcija {i+1}")
            predictions_layout.add_widget(pf)
            self.prediction_fields.append(pf)
        self.add_widget(Label(text="Predikcija sledeće karte (slika):", size_hint_y=None, height=30))
        self.add_widget(predictions_layout)

        self.dugme_predvidi = Button(text="🎯 Predvidi Sledeću Kartu", size_hint_y=None, height=50)
        self.dugme_predvidi.bind(on_press=self.predvidi_karte)
        self.add_widget(self.dugme_predvidi)

        self.rezultat_label = Label(text="", size_hint_y=None, height=40)
        self.add_widget(self.rezultat_label)

        dugmici_layout = GridLayout(cols=2, size_hint_y=None, height=50)
        self.dugme_tacno = Button(text="✔ Tačno", background_color=(0,1,0,1))
        self.dugme_netacno = Button(text="✘ Netačno", background_color=(1,0,0,1))
        self.dugme_tacno.bind(on_press=self.mark_correct)
        self.dugme_netacno.bind(on_press=self.mark_wrong)
        dugmici_layout.add_widget(self.dugme_tacno)
        dugmici_layout.add_widget(self.dugme_netacno)
        self.add_widget(dugmici_layout)

        self.dugme_stats = Button(text="📊 Prikaz statistike", size_hint_y=None, height=40)
        self.dugme_stats.bind(on_press=self.prikazi_statistiku)
        self.add_widget(self.dugme_stats)

        self.stats_label = Label(text="", size_hint_y=None, height=60)
        self.add_widget(self.stats_label)

    def predvidi_karte(self, instance):
        uneti_znakovi = [sel.get_selected() for sel in self.card_selectors]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        snaga = self.snaga_ai.text
        jacina = {'Slabo': 0.5, 'Normalno': 1.0, 'Jako': 2.0}
        self.ai.set_strength(jacina[snaga])
        slot = self.slot_izbor.text

        self.ai.train()
        pred1 = self.ai.predict(uneti_znakovi, timestamp, slot)
        self.ai.add_sample(uneti_znakovi, pred1, timestamp, slot)
        pred2 = self.ai.predict(uneti_znakovi, timestamp, slot)

        self.prediction_fields[0].set_card(pred1)
        self.prediction_fields[1].set_card(pred2)
        self.last_prediction = (pred1, BOJA_MAP[pred1], timestamp, slot)

        self.rezultat_label.text = f"Predikcija: {pred1} ({BOJA_MAP[pred1]}) ili {pred2} ({BOJA_MAP[pred2]})"
        self.app.db.save_prediction(slot, pred1, BOJA_MAP[pred1], timestamp, None)

    def mark_correct(self, instance=None):
        if self.last_prediction:
            slot = self.last_prediction[3]
            self.ai.update_performance(slot, 1)
            self.app.db.cursor.execute(
                "UPDATE predictions SET correct=1 WHERE id=(SELECT MAX(id) FROM predictions)"
            )
            self.app.db.conn.commit()
            self.rezultat_label.text = "Označeno kao tačno!"

    def mark_wrong(self, instance=None):
        if self.last_prediction:
            slot = self.last_prediction[3]
            self.ai.update_performance(slot, 0)
            self.app.db.cursor.execute(
                "UPDATE predictions SET correct=0 WHERE id=(SELECT MAX(id) FROM predictions)"
            )
            self.app.db.conn.commit()
            self.rezultat_label.text = "Označeno kao netačno!"

    def prikazi_statistiku(self, instance):
        stats = self.app.db.fetch_stats()
        if stats:
            msg = "Statistika:\n"
            for slot, total, tacno in stats:
                tacno = tacno if tacno else 0
                msg += f"{slot}: {tacno}/{total} tačno\n"
            self.stats_label.text = msg
        else:
            self.stats_label.text = "Nema podataka."

class CardPredictionApp(App):
    def build(self):
        Window.clearcolor = (0.05, 0.05, 0.05, 1)
        self.db = DBHelper()
        return MainScreen(self)

    def on_stop(self):
        self.db.close()

if __name__ == '__main__':
    CardPredictionApp().run()
