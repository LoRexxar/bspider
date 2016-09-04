#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import string

__author__ = "LoRexxar"


def remove_label(r):
    """
    去标签
    """
    dr = re.compile(r'<[^>]+>', re.S)
    result = dr.sub('', r)

    return result.strip()


def clean_input(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    ninput = []
    input = input.split(' ')

    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            ninput.append(item)

    return ninput
