#!/usr/bin/env python
# -*- coding:utf-8 -*-

from lib.log import logger
import sqlite3

__author__ = "LoRexxar"


class SpiderDb:
    """
    数据库操作类
    """
    def __init__(self, dbfile):
        """
        初始化
        :param dbfile: sqlite3 数据库文件
        """
        logger.debug('init database...')
        self.dbfile = "db/" + dbfile
        self.conn = sqlite3.connect(self.dbfile, check_same_thread=False)
        self.conn.text_factory = str
        self.cur = self.conn.cursor()

        check_table_sql = "select count(*) from sqlite_master where type='table' and name='drops'"
        self.cur.execute(check_table_sql)
        if self.cur.fetchone()[0] == 0:
            logger.debug('create a spider drops')
            self.create_table()
        else:
            logger.debug('spider table already exist...')

    def __del__(self):
        """
        销毁
        """
        self.conn.commit()
        self.conn.close()
        logger.debug('destroy database object')

    def create_table(self):
        """
        建表
        固定表名/字段
        """
        cb_sql = "CREATE TABLE drops (id INTEGER PRIMARY KEY autoincrement, title text, time text, content text)"
        self.cur.execute(cb_sql)
        self.conn.commit()
        logger.info("Create spider table drops...")

    def insert(self, title=None, time=None, content=None):
        """
        必须参数
        :param title: 爬取的页面标题
        :param time: 抓取页面的发布时间
        :param content: 抓取页面的内容
        :return:
        """
        values = self.select(title=title, content=content)

        if values[0][1] == title and values[0][3] == content:
            return 0

        in_sql = "INSERT INTO drops VALUES (null, ?, ?, ?)"

        self.cur.execute(in_sql, (title, time, content))
        logger.debug("INSERT suc and id is: " + str(self.cur.lastrowid))
        self.conn.commit()

    def select(self, title=None, time=None, content=None):

        se_sql = "SELECT * FROM drops WHERE title = '{}' and content = '{}'".format(title, content)

        self.cur.execute(se_sql)

        values = self.cur.fetchall()

        return values
