import math
from kivy.app import App

# ==========================================
# ФУНКЦИОНАЛЬНЫЕ КНОПКИ (РЯД 1)
# ==========================================

def press_clear(instance):
    """Кнопка 'C' — очистка экрана"""
    app = App.get_running_app()
    app.calc_screen.display.text = '0'


def press_sign(instance):
    """Кнопка '+/-' — смена знака числа"""
    app = App.get_running_app()
    a = app.calc_screen.display.text
    if a == '0':
        return
    if a.startswith('-'):
        app.calc_screen.display.text = a[1:]
    else:
        app.calc_screen.display.text = '-' + a


def press_sqrt(instance):
    """Кнопка '√' — квадратный корень"""
    app = App.get_running_app()
    current_text = app.calc_screen.display.text

    try:
        val = float(current_text.replace(',', '.'))
        if val < 0:
            app.calc_screen.display.text = 'Ошибка'
            return

        res = math.sqrt(val)

        if res.is_integer():
            app.calc_screen.display.text = str(int(res))
        else:
            app.calc_screen.display.text = str(res).replace('.', ',')

    except Exception:
        app.calc_screen.display.text = 'Ошибка'


def press_backspace(instance):
    """Кнопка '←' — удаление последнего символа"""
    app = App.get_running_app()
    a = app.calc_screen.display.text

    if len(a) >= 2:
        app.calc_screen.display.text = a[:-1]
    else:
        app.calc_screen.display.text = '0'

# ==========================================
# МАТЕМАТИЧЕСКИЕ ОПЕРАЦИИ
# ==========================================

def press_div(instance):
    """Кнопка '/' — деление"""
    app = App.get_running_app()
    current_text = app.calc_screen.display.text

    last_char = current_text[-1]

    if not last_char.isdigit():
        app.calc_screen.display.text = f'{current_text[:-1]}/'
    else:
        app.calc_screen.display.text = f'{current_text}/'


def press_mult(instance):
    """Кнопка '*' — умножение"""
    app = App.get_running_app()
    current_text = app.calc_screen.display.text

    last_char = current_text[-1]

    if not last_char.isdigit():
        app.calc_screen.display.text = f'{current_text[:-1]}*'
    else:
        app.calc_screen.display.text = f'{current_text}*'


def press_sub(instance):
    """Кнопка '-' — вычитание"""
    app = App.get_running_app()
    current_text = app.calc_screen.display.text

    last_char = current_text[-1]

    if not last_char.isdigit():
        app.calc_screen.display.text = f'{current_text[:-1]}-'
    else:
        app.calc_screen.display.text = f'{current_text}-'


def press_add(instance):
    """Кнопка '+' — сложение"""
    app = App.get_running_app()
    current_text = app.calc_screen.display.text

    last_char = current_text[-1]

    if not last_char.isdigit():
        app.calc_screen.display.text = f'{current_text[:-1]}+'
    else:
        app.calc_screen.display.text = f'{current_text}+'


def press_equal(instance):
    """Кнопка '=' — подсчет результата"""
    app = App.get_running_app()
    text = app.calc_screen.display.text
    try:
        text = text.replace(',', '.')
        new_text = str(eval(text))
        new_text = new_text.replace('.', ',')
        if new_text.endswith(',0'):
            new_text = new_text[:-2]
        app.calc_screen.display.text = new_text
    except Exception:
        app.calc_screen.display.text = 'ERROR'

# ==========================================
# ЦИФРЫ И ЗАПЯТАЯ
# ==========================================

def press_comma(instance):
    """Кнопка ',' — десятичная запятая"""
    app = App.get_running_app()
    current_text = app.calc_screen.display.text
    if not current_text:
        app.calc_screen.display.text = '0,'
        return
    if current_text[-1] in ['+', '-', '*', '/']:
        app.calc_screen.display.text += '0,'
        return
    temp_text = current_text.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ')
    parts = temp_text.split()
    last_number = parts[-1] if parts else ''
    if ',' not in last_number:
        app.calc_screen.display.text += ','


def press_num(instance):
    """Универсальная функция для ввода любых цифр (0-9)"""
    app = App.get_running_app()
    current_text = app.calc_screen.display.text
    digit = instance.text
    if current_text == '0':
        if digit == '0':
            return
        else:
            app.calc_screen.display.text = digit
    else:
        app.calc_screen.display.text += digit