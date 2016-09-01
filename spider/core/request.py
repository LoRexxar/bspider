#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
from lib.log import logger

__author__ = "LoRexxar"


def request(url=None, header={}, value=None):

    if url is None:
        logger.error("URL is not found...")
        exit(0)
    else:
        logger.info("Target url is {}".format(url))

    if value is None:
        logger.warning("POST value is empty...")
    else:
        data = urllib.urlencode(value)
        value = urllib2.Request(url, data)

    if len(header) == 0:
        logger.warning("Header is empty...")
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
                  }

    req = urllib2.Request(url, value, headers=header)

    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError:
        logger.error("urlopen error...")
        return None
    except urllib2.URLError:
        logger.error("Something error")
        return None

    return response.read().decode('utf-8')
