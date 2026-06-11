from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

from logic import*

Window.clearcolor = '#999999'
Window.size = (350, 500)

class Calculator(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.display = TextInput(
            text='0',
            halign='right',
            multiline=False,
            size_hint_y=0.35,
            font_size=45
        )
        self.btnClear = Button(text='C')
        self.btnSign = Button(text='+/-')
        self.btnSqrt = Button(text='√')
        self.btnBack = Button(text='<-')
        self.btn7 = Button(text='7')
        self.btn8 = Button(text='8')
        self.btn9 = Button(text='9')
        self.btnDiv = Button(text='/')
        self.btn4 = Button(text='4')
        self.btn5 = Button(text='5')
        self.btn6 = Button(text='6')
        self.btnMult = Button(text='*')
        self.btn1 = Button(text='1')
        self.btn2 = Button(text='2')
        self.btn3 = Button(text='3')
        self.btnSub = Button(text='-')
        self.btnComma = Button(text=',')
        self.btn0 = Button(text='0')
        self.btnEqual = Button(text='=')
        self.btnAdd = Button(text='+')
        BL = BoxLayout(orientation='vertical')
        BL.add_widget(self.display)
        GL = GridLayout(cols=4)

        GL.add_widget(self.btnClear)
        GL.add_widget(self.btnSign)
        GL.add_widget(self.btnSqrt)
        GL.add_widget(self.btnBack)
        GL.add_widget(self.btn7)
        GL.add_widget(self.btn8)
        GL.add_widget(self.btn9)
        GL.add_widget(self.btnDiv)
        GL.add_widget(self.btn4)
        GL.add_widget(self.btn5)
        GL.add_widget(self.btn6)
        GL.add_widget(self.btnMult)
        GL.add_widget(self.btn1)
        GL.add_widget(self.btn2)
        GL.add_widget(self.btn3)
        GL.add_widget(self.btnSub)
        GL.add_widget(self.btnComma)
        GL.add_widget(self.btn0)
        GL.add_widget(self.btnEqual)
        GL.add_widget(self.btnAdd)


        self.btnClear.bind(on_press=press_clear)
        self.btnSign.bind(on_press=press_sign)
        self.btnSqrt.bind(on_press=press_sqrt)
        self.btnBack.bind(on_press=press_backspace)
        self.btnDiv.bind(on_press=press_div)
        self.btnMult.bind(on_press=press_mult)
        self.btnSub.bind(on_press=press_sub)
        self.btnAdd.bind(on_press=press_add)
        self.btnEqual.bind(on_press=press_equal)
        self.btnComma.bind(on_press=press_comma)

        # Цифры
        self.btn0.bind(on_press=press_num)
        self.btn1.bind(on_press=press_num)
        self.btn2.bind(on_press=press_num)
        self.btn3.bind(on_press=press_num)
        self.btn4.bind(on_press=press_num)
        self.btn5.bind(on_press=press_num)
        self.btn6.bind(on_press=press_num)
        self.btn7.bind(on_press=press_num)
        self.btn8.bind(on_press=press_num)
        self.btn9.bind(on_press=press_num)

        BL.add_widget(GL)
        self.add_widget(BL)


class CalculatorApp(App):
    def build(self):
        sm = ScreenManager()
        self.calc_screen = Calculator(name='calculator')
        sm.add_widget(self.calc_screen)
        return sm



if __name__ == '__main__':
    CalculatorApp().run()
