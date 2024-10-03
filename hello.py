#!/usr/bin/env python3

"""
Hello world Multi Language.

Dependent a language configuration in ambient this program print a mensage 
Hello World

how to usage:

have correct variables configurate ex:

    export LANG=en_US

Execution:

    python3 hello.py
    or
    ./hello.py
"""
__version__ = "0.0.1"
__author__  = "@Jhon"
__license__ = "Unlincense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello world!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"


print(msg)