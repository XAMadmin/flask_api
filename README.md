# flask API服务

### 接口说明文档

1. 接口描述: 出库汇总信息

   + url:/api/v1.0/store_info

   + 请求方式：POST

   + 传入参数：

     ```
     格式：路径参数 （请求体json格式）
     名字             类型       是否必须      说明
     djbh            字符串       是          单据编号
     rq              字符串       是          出库日期
     ontime          字符串       是          出库时间
     dwbh            字符串       是          曼迪新单位内码
     djje            字符串       是          单据金额
     beizhu          字符串       是          备注
     dj_sn           int                     明细序号
     pihao                                   批号
     sxrq                                    失效日期
     baozhiqi                                生产日期
     shl                                     出库数量
     dj                                      价格
     je                                      出库金额
     ```

   + 实例：

     ```
     {
        "data":[
            {
             "djbh":"1", 
             "rq":"2020-01-01", 
             "ontime": "2020-01-01",
             "dwbh":"1234",
             "djje":"123.00", 
             "beizhu":"",
             "details":  [
                             {
                                 "dj_sn":"0",
                                 "spid":"SPH00000086",
                                 "pihao":"121311",
                                 "sxrq":"2021-01-01",
                                 "baozhiqi":"2023-01-01",
                                 "shl":"50",
                                 "dj":"20.00",
                                 "je":"123.00"
                             },
                                         
                             {
                                 "dj_sn":"1",
                                 "spid":"SPH00000087",
                                 "pihao":"121311",
                                 "sxrq":"2021-01-01",
                                 "baozhiqi":"2023-01-01",
                                 "shl":"50",
                                 "dj":"20.00",
                                 "je":"33.00"
                             }
                    
                         ]
             },
             {
             "djbh":"1", 
             "rq":"2020-01-01", 
             "ontime": "2020-01-01",
             "dwbh":"1234",
             "djje":"123.00", 
             "beizhu":"",
             "details":  [
                             {
                                 "dj_sn":"0",
                                 "spid":"SPH00000086",
                                 "pihao":"121311",
                                 "sxrq":"2021-01-01",
                                 "baozhiqi":"2023-01-01",
                                 "shl":"50",
                                 "dj":"20.00",
                                 "je":"123.00"
                             }
                                 
                         ]
             }
        ]
     }
     
     ```

   + 返回值

     ```
     格式：json
     名字             类型       是否必传      说明
     errno           字符串         否        错误代码
     errmsg          字符串         否        错误内容
     实例：
     '{"errno": "OK", "errmsg": "成功！"}'
     ```

### 服务部署

```bash
# 在linux上Dockerfile目录执行如下命令生成镜像,镜像和tag自定义即可, 别忘记后面的点
docker build -t flask_gunicorn:1.0 .
# 运行容器
docker run -d --name flask_api -p 8080:8080 flask_gunicorn:1.0
# 执行查看实时日志
docker logs -f --tail 30 flask_api 
# 进入容器内查看日志
docker exec -it flask_api /bin/bash
cd logs
```

### docker容器代码更新

```bash
# 进入接口py文件
docker cp get_store.py 容器ID:/code/MinxServer/api_1_0
# 重启docke容器
docker restart 容器ID
```

