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


# ========或者一下配置===============================================
import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
accesslog ="-" # STDOUT
access_log_format = '%(h)s %(l)s %(u)s %(t)s"%(r)s" %(s)s %(b)s"%(q)s""%(D)s"'
bind ="0.0.0.0:5000"
keepalive = 120
timeout = 120
worker_class ="gthread"
threads = 3

#==================配置解释============================================
# 文件 gunicorn_config.py
loglevel = 'debug' #日志级别 debug info warning error critical
bind = "127.0.0.1:5000" #绑定地址和端口 # utils.get_host_ip2()+':8000'
daemon = False # 是否以守护进程启动
# workers = multiprocessing.cpu_count() * 2 + 1 #启动进程数
workers = 4 #10
worker_class = 'gthread' #工作模式 切记不能使用 gevent ,会拦截内部flask发出的请求
threads = 4 #每个工作者线程数
worker_connections = 2000 # 最大并发量
pidfile = "./log/gunicorn.pid" # pid 文件
accesslog = "./log/access.log" #访问日志目录
errorlog = "./log/debug.log" #出错日志
graceful_timeout = 300
timeout = 300 #reload worker after slicent 3 secs
# preload_app=True #是否预加载app,加快启动速度
# reload=True # 代码更新自动重启
