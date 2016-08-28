#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

__author__ = "LoRexxar"


def remove_label(r):

    dr = re.compile(r'<[^>]+>', re.S)
    result = dr.sub('', r)

    return result.strip()
