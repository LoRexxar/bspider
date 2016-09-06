#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime
from bs4 import BeautifulSoup
from lib.log import logger
from spider.core.parse import remove_label
from spider.core.request import request
from spider.zhihu.database import SpiderDb
from spider.zhihu.login import login
from spider.zhihu.login import check_login

__author__ = "LoRexxar"


def zhihu_spider():

    """
    zhihu 收藏夹爬虫
    """
    # 初始化
    url = "https://www.zhihu.com/collections"
    db = SpiderDb('drops.db')
    cookie = {
        'z_c0': 'Mi4wQUFBQXJNczdBQUFBWUFDU1h0bC1DaGNBQUFCaEFsVk5RQ1QxVndCeGl1WEVSTWVSRVJVTlRQcUxxOUNaRjdGZGFn|1473091395|4ccda2c351f5bd890d1e32b4b911c37eb36fd82b',
        'q_c1': 'd9448b8562764d1da310820d979db944|1473091390000|1473091390000',
        'n_c': '1',
        'login': '"M2U1YzdkOTMxMDMyNDk4Yzk1ZDAxMmNkYzc3YWI1N2Q=|1473091392|ee25ad336624ccbf2596e028610c1709b3c383ac"',
        'l_cap_id': '"NjRlOThmODcyZjEwNGZiMThmNWJiOGJkYzhiZGY1MDY=|1473091390|bf94be8bd181a852d3b5cd7eec9d2a87f9d19141"',
        'd_c0': '"AGAAkl7ZfgqPTnZFCCt-GqkTgRpo4X4IADE=|1473091390"',
        'cap_id': '"NjJkMGZmNzQ1MGEzNDZhMWEwNjEyYjYyZDZiZjQwNzU=|1473091390|99cf5d3a0b21931f9b9e205f6c0a6e6a4b2b1d94"',
        'a_t': '"2.0AAAArMs7AAAXAAAAQyT1VwAAAKzLOwAAAGAAkl7ZfgoXAAAAYQJVTUAk9VcAcYrlxETHkREVDUz6i6vQmRexXWrImrNxWAA-p971nVyOEfIopKqyWA=="',
        '_zap': 'e9790297-b791-4440-934c-cc56a4f837be',
        '_za': 'c1e9ed73-8b57-4fa2-8118-33ed69adb393',
        '_xsrf': 'd4d9f5298a273a5ba6fab2cbca4a72e8',
        '__utmz': '51854390.1473091391.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/',
        '__utmv': '51854390.100-1|2=registration_date=20141025=1^3=entry_date=20141025=1',
        '__utmt': '1',
        '__utmc': '51854390',
        '__utmb': '51854390.4.10.1473091391',
        '__utma': '51854390.909723460.1473091391.1473091391.1473091391.1'
        }


    # login()
    check_login(url, cookie)

