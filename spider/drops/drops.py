#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime
from bs4 import BeautifulSoup
from lib.log import logger
from spider.core.parse import remove_label
from spider.core.request import request
from spider.drops.database import SpiderDb

__author__ = "LoRexxar"


def drops_spider():

    """
    drops爬虫
    """
    # 初始化
    url = "http://drops.hduisa.org"
    essays = []
    db = SpiderDb('drops.db')

    logger.info("Start Crawling drops...")
    response = request(url)

    if response is None:
        return 0

    try:
        bs0bj = BeautifulSoup(response, "lxml")

        html = bs0bj.find_all("article")

        for article in html:

            time = get_time(bs0bj=article) + ".12000"
            atime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f")
            ntime = datetime.now()

            if (ntime - atime).days <= 1:
                essay = []
                title = get_title(bs0bj=article)
                if title == '\xb4\xcb\xc4\xda\xc8\xdd\xb1\xbb\xc3\xdc\xc2\xeb\xb1\xa3\xbb\xa4':
                    continue
                content = get_content(bs0bj=article)

                essay.append(title)
                essay.append(content)
                db.insert(title, time, content)

                essays.append(tuple(essay))
            else:
                continue

    except AttributeError:
        logger.error("html parse error...")

    if len(essays) == 0:
        print 'drops\xe5\xb9\xb6\xe6\xb2\xa1\xe6\x9b\xb4\xe6\x96\xb0'.decode('utf-8')
        return 0

    for essay in essays:
        print essay[0], essay[1]


def get_title(bs0bj=None):

    if bs0bj is None:
        logger.error("bs0bj is None...")
        return None

    result = bs0bj.h2.a.encode('gb18030')

    return remove_label(result)


def get_content(bs0bj=None):

    if bs0bj is None:
        logger.error("bs0bj is None...")
        return None

    result = bs0bj.div.encode('gb18030')

    return remove_label(result)


def get_time(bs0bj=None):

    if bs0bj is None:
        logger.error("bs0bj is None...")
        return None

    result = bs0bj.time.encode('gb18030')

    return remove_label(result)
