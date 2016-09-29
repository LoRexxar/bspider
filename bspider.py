#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib.log import logger
from lib.log import log
from spider.drops.drops import drops_spider
from spider.zhihu.zhihu import zhihu_spider
import logging
import time

__author__ = "LoRexxar"


def main():

    # 初始化log
    log(logging.DEBUG, repr(int(time.time())) + ".log")

    drops_spider()

    # zhihu_spider()

if __name__ == '__main__':
    main()
