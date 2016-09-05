#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib.log import logger
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
import os
import platform


__author__ = "LoRexxar"


def ph_request(url=None, header={}, value=None):

    if url is None:
        logger.error("URL is not found...")
        exit(0)
    else:
        logger.info("Target url is {}".format(url))

    if len(header) == 0:
        logger.warning("Header is empty...")
        header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
            }

    try:
        driver = webdriver.PhantomJS(executable_path=set_phantomjs_path())

    except WebDriverException:
        logger.error("phantomjs path error...")
        exit(0)

    try:
        driver.get(url)
        time.sleep(3)

    finally:
        return driver.page_source


def set_phantomjs_path():

    phantomjs_path = os.getcwd() + os.sep + "spider" + os.sep + "phantomjs" + os.sep
    logger.info("os is {}".format(platform.system()))

    if "Windows" in platform.system():
        return phantomjs_path + "phantomjs.exe"
    elif "Linux" in platform.system() and "x86_64" in platform.machine():
        return phantomjs_path + "phantomjs"
    elif "Darwin" in platform.system():
        return phantomjs_path + "phantomjs-mac"
    else:
        logger.error("Unsupported operating system.")
        logger.error("Only Windows and Linux x86_64 was supported.")
        exit(0)
