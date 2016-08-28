#!/usr/bin/env python
# -*- coding:utf-8 -*-

from spider.core.request import request
from bs4 import BeautifulSoup
from datetime import datetime
from lib.log import logger
from core.parse import remove_label

__author__ = "LoRexxar"


def drops_spider():

    url = "http://drops.hduisa.org"
    essays = []

    response = request(url)

    if response is None:
        return 0

    try:
        bs0bj = BeautifulSoup(response, "lxml")

        html = bs0bj.find_all("article")

        for article in html:

            atime = get_time(bs0bj=article) + ".12000"
            atime = datetime.strptime(atime,"%Y-%m-%d %H:%M:%S.%f")
            ntime = datetime.now()

            if (ntime - atime).days <= 3:
                essay = []
                essay.append(get_title(bs0bj=article))
                essay.append(get_content(bs0bj=article))

                essays.append(tuple(essay))
            else:
                continue

    except AttributeError:
        logger.error("html parse error...")

    for essay in essays:
        print essay


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