#!/usr/bin/env python
# -*- encode: utf8 -*-
#
# Title: ZunDoko
# Author: acque2two
# This is no licensed.

import sys
import random

class Zundoko:

    say = ["ズン", "ドコ"]
    correct = "キ・ヨ・シ!"

    def __init__(self):
        pass

    def run(self):
        hist = []
        while not self._is_kiyoshi(hist):
            hist = []
            sys.stdout.write('\n')
            for i in range(5):
                j = random.randrange(0,2)
                hist.append(j)
                sys.stdout.write(self.say[j])
        print(self.correct)

    def _is_kiyoshi(self, hist):
        if hist == [0,0,0,0,1]:
            return True
        return False

Zundoko().run()
