import random


GREETINGS = [
    'Hello World',
    'Hola Mundo',
    'ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ ਦੁਨਿਆ',
    'こんにちは世界',
    '你好世界',
    'Përshendetje Botë',
    'مرحبا بالعالم',
    'Բարեւ, աշխարհ',
    'হ্যালো দুনিয়া',
    'Saluton mondo',
    'გამარჯობა მსოფლიო',
]


jq = window.jQuery


def plog(text):
    return jq('<p>').text(text).appendTo('#output')


def clear(evt):
    jq('#output').empty()
jq('button.clear').on('click', clear)


def hello(evt):
    text = random.choice(GREETINGS)
    plog(text)
jq('button.hello').on('click', hello)
