# workers = 5        # 定义同时开启的处理请求的进程数量，根据网站流量适当调整
# worker_class = "gevent"  # 采用gevent库，支持异步处理请求，提高吞吐量
# bind = "0.0.0.0:8080"   # 这里8080可以随便调整

from gevent import monkey
​
monkey.patch_all()
​
import multiprocessing
​
bind = "0.0.0.0:8080"
​
# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'gevent'