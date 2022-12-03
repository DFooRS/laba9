#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    dictionary = {1:'бебра', 2: 'СКФУ', 3: 'Питон'}

    swapped = {v: k for k, v in dictionary.items()}

    print(swapped)