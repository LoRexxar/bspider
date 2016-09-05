#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
from lib.log import logger

__author__ = "LoRexxar"


def request(url=None, header={}, value=None):

    if url is None:
        logger.error("URL is not found...")
        exit(0)
    else:
        logger.info("Target url is {}".format(url))

    if len(header) == 0:
        logger.warning("Header is empty...")
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
                  }

    req = requests.Session()

    try:
        if value is None:
            response = req.get(url, headers=header)
        else:
            response = req.post(url, data=value, headers=header)
    except:
        logger.error("Something error")
        return None

    return response.text.encode('utf-8')
