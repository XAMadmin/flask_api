FROM python:3-slim
​
ADD ./  /code
​
WORKDIR /code
​
RUN pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip3 config set install.trusted-host pypi.tuna.tsinghua.edu.cn
RUN pip3 install -r requirements.txt
​
# 时区设置
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo 'Asia/Shanghai' >/etc/timezone
​
# 端口
EXPOSE 3340
​
# CMD ["python3", "/code/app.py"]  py文件启动方式
​
# gunicorn 启动
ENTRYPOINT ["gunicorn", "--config", "gunicorn.conf.py", "manage:app"]