#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib.log import logger
from lib.log import log
from spider.drops import drops_spider
import logging
import time

__author__ = "LoRexxar"


def main():

    log(logging.DEBUG, repr(int(time.time())) + ".log")

    drops_spider()

if __name__ == '__main__':
    main()
