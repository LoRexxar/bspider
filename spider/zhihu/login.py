#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime
from bs4 import BeautifulSoup
from lib.log import logger
from spider.core.parse import remove_label
from spider.core.request import request

__author__ = "LoRexxar"


def login():

    """
    zhihu 登陆
    """
    # 初始化
    url = "http://www.zhihu.com/#signin"
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
              'Cookie': 'd_c0="ACBAKoJvygmPTo5y_6OD9XjyA2qLmO5TGFI=|1460984044"; _za=437dcae3-bb5d-4282-a4a8-bb8c254c36df; q_c1=02d812460bc7450ab057a9b8f984a238|1472704342000|1460984044000; _xsrf=1569f5a947995ce167ca29984f5c99cd; l_cap_id="MGQxZTI3NzI5Yzk2NDhkOWIzZDRkMjM5NDc1NWJjYTk=|1472704341|ceb040aa5837d83390f2de702d76c907d0bb17da"; cap_id="MTZhMGE2MDUzNWEwNGNlNzljMGJkMGIwMTFjY2Y5N2Q=|1472704341|eb8a22027ab0bf15119c6e04faad42c899997f91"; _zap=c990efa2-8f74-4b8f-80be-82ba179e1aaf; __utma=51854390.1991431794.1469951161.1471753231.1472704351.4; __utmc=51854390; __utmz=51854390.1472704351.4.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.000--|2=registration_date=20160901=1^3=entry_date=20160418=1'
              }

    username = "13093790820"
    password = "test123!@#"

    logger.info("Start login zhihu...")
    response = request(url=url, header=header)

    if response is None:
        return 0

    try:
        bs0bj = BeautifulSoup(response, "lxml")

        html = bs0bj.find_all("div", {"class", "view-signin"})

        print html[0].encode('gb18030')
        xsrf = get_xsrf(bs0bj=html)

    except AttributeError:
        logger.error("html parse error...")


def get_xsrf(bs0bj=None):

    if bs0bj is None:
        logger.error("bs0bj is None...")
        return None

    result = bs0bj[0].input.attrs["value"].encode('gb18030')

    return result