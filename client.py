from org.transcrypt.stubs.browser import __pragma__
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


# def on_click(selector):
#     def wrapper(fn):
#         print(selector)
#         print(fn)
#         jq(selector).on('click', fn)
#         return fn
#
#     return wrapper


def clear(evt):
    jq('#output').empty()
jq('button.clear').on('click', clear)


def hello(evt):
    text = random.choice(GREETINGS)
    plog(text)
jq('button.hello').on('click', hello)


def generator():
    def fn(n):
        for i in range(n):
            yield i, i*i
    for x in fn(10):
        plog(x)

jq('.generator').on('click', generator)
