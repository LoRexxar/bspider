# 爬虫结构

```
├─bspider
│  │  .gitignore
│  │  bspider.py
│  │  README.md
│  │
│  ├─db
│  │      drops.db
│  │
│  ├─lib
│  │      log.py
│  │      __init__.py
│  │
│  ├─log
│  │      1472355167.log
│  │
│  └─spider
│      │  __init__.py
│      │
│      ├─core
│      │      parse.py
│      │      request.py
│      │      __init__.py
│      │
│      └─drops
│              database.py
│              drops.py
│              __init__.py
```

/db: 数据库文件夹，sqlite3储存文件
/log: log文件夹，每次请求的log文件
/lib：爬虫结构通用类文件夹
/spider： 爬虫结构核心逻辑文件夹
/core: 通用内核类文件
/drops：已完成的drops爬虫逻辑