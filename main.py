from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.lang.builder import Builder
import re

Window.size = (720, 1234)
Builder.load_file('./main.kv')


class CauculadoraWidget(Widget):
    def clear(self):
        self.ids.input_box.font_size = sp(43)
        self.ids.input_box.text = '0'

    def adicionar(self, num):
        num_existente = self.ids.input_box.text
        if len(num_existente) >= 14:
            self.ids.input_box.font_size = sp(20)

        if num_existente == '0' or num_existente == 'Equação errada.':
            self.ids.input_box.text = ''
            self.ids.input_box.font_size = sp(43)
            self.ids.input_box.text = f'{num}'

        else:
            self.ids.input_box.text = f'{num_existente}{num}'

    def sinais(self, sinal):
        num_existente = self.ids.input_box.text
        if '1/' in sinal:
            self.ids.input_box.font_size = sp(43)
            self.ids.input_box.text = f'{sinal} '
        else:
            self.ids.input_box.text = f'{num_existente} {sinal} '

    def remover(self):
        num_existente = self.ids.input_box.text
        if len(num_existente) < 14:
            self.ids.input_box.font_size = sp(43)
        if len(num_existente) <= 1:
            self.ids.input_box.text = '0'
        else:
            num_existente = num_existente[:-1]
            self.ids.input_box.text = num_existente

    def caucular(self):
        num_existente = self.ids.input_box.text
        try:
            if '1/' in num_existente:
                elem = num_existente.split()
                self.ids.input_box.text = f'{1 / float(elem[1]):.6f}'

            elif '(%)' in num_existente:
                elem = num_existente.split()
                self.ids.input_box.text = f'{(float(elem[2]) / 100) * float(elem[0]):.1f}'
            else:
                try:
                    elem = num_existente.split()
                    if len(elem) == 3 and elem[1] == '%':
                        resultado = f'{eval(num_existente)}'
                    else:
                        resultado = f'{eval(num_existente):.1f}'
                except:
                    self.ids.input_box.font_size = sp(43)
                    self.ids.input_box.text = 'Equação errada.'
                else:
                    self.ids.input_box.text = resultado
        except:
            self.ids.input_box.text = 'Equação errada.'

    def potencia(self):
        num_existente = self.ids.input_box.text
        try:
            num_existente = self.ids.input_box.text = f'{(float(num_existente) ** 2)}'
            if len(num_existente) > 15:
                self.ids.input_box.font_size = sp(20)
            else:
                self.ids.input_box.font_size = sp(43)
        except:
            self.ids.input_box.text = 'Equação errada.'

    def raiz(self):
        num_existente = self.ids.input_box.text
        try:
            num_existente = self.ids.input_box.text = f'{float(num_existente) ** 0.5}'
            if len(num_existente) > 15:
                self.ids.input_box.font_size = sp(20)
            else:
                self.ids.input_box.font_size = sp(43)
        except:
            self.ids.input_box.text = 'Equação errada.'

    def pos_neg(self):
        num_existente = self.ids.input_box.text
        if '-' in num_existente:
            self.ids.input_box.text = f"{num_existente.replace('-', '')}"
        else:
            self.ids.input_box.text = f'-{num_existente}'

    def ponto(self):
        num_existente = self.ids.input_box.text
        num_list = re.split('\+|\*|-|/|%', num_existente)

        if ("+" in num_existente or '-' in num_existente or '*' in num_existente or '/' in num_existente or '%' in num_existente) and '.' not in num_list[-1]:
            self.ids.input_box.text = f'{num_existente}.'

        elif '.' in num_existente:
            pass

        else:
            self.ids.input_box.text = f'{num_existente}.'


class MainApp(App):
    def build(self):
        return CauculadoraWidget()


MainApp().run()
