# main.py

import sqlite3
from datetime import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
from kivy.core.window import Window
import numpy as np
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.naive_bayes import GaussianNB
from random import choice
from collections import Counter

# Konstante
color_map = {'Pik': 'Crna', 'Tref': 'Crna', 'Herc': 'Crvena', 'Karo': 'Crvena'}
znakovi = ['Pik', 'Tref', 'Herc', 'Karo']
boje = ['Crna', 'Crvena']
slot_igre = ['100 Super Hot', '40 Super Hot', 'Wild Hot 40']

class AdvancedCardAI:
    def __init__(self, history_length=4):
        self.history_length = history_length
        self.mapping = {znak: i for i, znak in enumerate(znakovi)}
        self.inv_mapping = {v: k for k, v in self.mapping.items()}
        self.models = {s: RidgeClassifier() for s in slot_igre}
        self.bayes_models = {s: GaussianNB() for s in slot_igre}
        self.data = {s: {'X': [], 'y': [], 'time': []} for s in slot_igre}
        self.trained = {s: False for s in slot_igre}
        self.performance = {s: [] for s in slot_igre}
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
        for slot in slot_igre:
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
            return choice(znakovi)

        x_lr = np.array(self.encode_sequence(sequence[-self.history_length:])).reshape(1, -1)
        model = self.models[slot_type]
        lr_pred = model.predict(x_lr)[0]
        try:
            lr_conf = max(model.predict_proba(x_lr)[0]) if hasattr(model, 'predict_proba') else 1.0
        except:
            lr_conf = 1.0

        if timestamp:
            x_bayes = np.array(self.extract_time_features(timestamp)).reshape(1, -1)
            bayes_model = self.bayes_models[slot_type]
            bayes_pred = bayes_model.predict(x_bayes)[0]
            bayes_conf = max(bayes_model.predict_proba(x_bayes)[0])
        else:
            bayes_pred = lr_pred
            bayes_conf = 0

        if self.ai_strength < 1.0:
            return self.inv_mapping[bayes_pred]
        elif self.ai_strength > 1.0:
            return self.inv_mapping[lr_pred]
        else:
            return self.inv_mapping[lr_pred] if lr_conf >= bayes_conf else self.inv_mapping[bayes_pred]

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.ai = AdvancedCardAI()
        self.unete_karte = []
        self.unete_boje = []
        self.slot_izbor = Spinner(text='Automatski', values=slot_igre + ['Automatski'])
        self.snaga_ai = Spinner(text='Normalno', values=['Slabo', 'Normalno', 'Jako'])

        controls = GridLayout(cols=2, size_hint_y=None, height=60)
        controls.add_widget(Label(text="Izbor igre:"))
        controls.add_widget(self.slot_izbor)
        controls.add_widget(Label(text="AI Jačina:"))
        controls.add_widget(self.snaga_ai)
        self.add_widget(controls)

        self.karte_input = []
        karte_layout = GridLayout(cols=4, size_hint_y=None, height=100)
        for i in range(4):
            inp = Spinner(text='?', values=znakovi)
            karte_layout.add_widget(inp)
            self.karte_input.append(inp)
        self.add_widget(Label(text="Unesi 4 prethodne karte:"))
        self.add_widget(karte_layout)

        self.boje_input = []
        boje_layout = GridLayout(cols=2, size_hint_y=None, height=60)
        for i in range(2):
            inp = Spinner(text='?', values=boje)
            boje_layout.add_widget(inp)
            self.boje_input.append(inp)
        self.add_widget(Label(text="Unesi 2 prethodne boje:"))
        self.add_widget(boje_layout)

        dugme_predvidi = Button(text="🎯 Predvidi Sledeću Kartu", size_hint_y=None, height=50)
        dugme_predvidi.bind(on_press=self.predvidi_kartu)
        self.add_widget(dugme_predvidi)

        self.rezultat_label = Label(text="", size_hint_y=None, height=40)
        self.add_widget(self.rezultat_label)

    def predvidi_kartu(self, instance):
        uneti_znakovi = [inp.text for inp in self.karte_input if inp.text in znakovi]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        snaga = self.snaga_ai.text
        jacina = {'Slabo': 0.5, 'Normalno': 1.0, 'Jako': 2.0}
        self.ai.set_strength(jacina[snaga])
        slot = self.slot_izbor.text
        pred = self.ai.predict(uneti_znakovi, timestamp, slot)
        self.last_prediction = (pred, color_map[pred], timestamp, slot)
        self.rezultat_label.text = f"Predikcija: {pred} ({color_map[pred]})"

    def mark_correct(self):
        self.ai.update_performance(self.last_prediction[3], 1)

    def mark_wrong(self):
        self.ai.update_performance(self.last_prediction[3], 0)

class CardPredictionApp(App):
    def build(self):
        Window.clearcolor = (0.05, 0.05, 0.05, 1)
        return MainScreen()

if __name__ == '__main__':
    CardPredictionApp().run()
