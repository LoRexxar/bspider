#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime
from bs4 import BeautifulSoup
from lib.log import logger
from spider.core.parse import remove_label
from spider.core.request import request
from spider.zhihu.database import SpiderDb
from spider.zhihu.login import login

__author__ = "LoRexxar"


def zhihu_spider():

    """
    zhihu 收藏夹爬虫
    """
    # 初始化
    url = "https://www.zhihu.com/collections"
    essays = []
    db = SpiderDb('drops.db')

    login()