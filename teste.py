#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def compare_letter(txt1, txt2):
  if (Counter(txt1) == Counter(txt2)):
    return True
  else:
    return False

def sherlok(txt, qtd):
  count = 0
  jump = 1
  for i in range(0, len(txt), 1):
    if (len(txt[i:i+qtd]) == qtd ):
      for j in range(jump, len(txt), 1):
        if (len(txt[j:j+qtd]) == qtd):
          if (compare_letter(txt[i:i+qtd], txt[j:j+qtd])):
            count = count + 1
      jump = jump + 1
  return count



if __name__ == '__main__':

  s = "cdcd"
  count = 0
  for i in range(1, len(s)):
    count+= sherlok(s,i)
  print(count)