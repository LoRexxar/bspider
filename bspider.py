#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib.log import logger
from lib.log import log
from spider.drops import drops_spider
import logging
import time

__author__ = "LoRexxar"


def main():

    # 初始化log
    try:
        log(logging.DEBUG, repr(int(time.time())) + ".log")
    except:
        logger.error("init log error...")
        exit(0)

    # 初始化数据库


    drops_spider()

if __name__ == '__main__':
    main()
