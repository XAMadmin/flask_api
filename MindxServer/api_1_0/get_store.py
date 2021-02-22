from . import api
from flask import request, jsonify, current_app
import json
from MindxServer.models import DBSession
from MindxServer.models import MdxStore


# 获取出库信息
@api.route("/store_info", methods=["POST"])
def store_hz():
    """
    djbh    单据编号
    rq      出库日期
    ontime  出库时间
    dwbh    曼迪新单位内码
    je      单据金额
    beizhu  备注
    """
    session = DBSession()
    req_dict = request.get_json()
    if req_dict:
        results = req_dict.get("data")
        lis = []
        for data in results:
            djbh = data.get("djbh")
            rq = data.get("rq")
            ontime = data.get("ontime")
            dwbh = data.get("dwbh")
            djje = data.get("djje")
            beizhu = data.get("beizhu")
            details = data.get("details")

            if not details:
                current_app.logger.error("请求参数错误,单据编号【】".format(djbh))
                return jsonify(err='err', errmsg= "请求参数错误！")

            for detail in details:
                dj_sn = detail.get("dj_sn")
                spid = detail.get("spid")
                pihao = detail.get("pihao")
                sxrq = detail.get("sxrq")
                baozhiqi = detail.get("baozhiqi")
                shl = detail.get("shl")
                dj = detail.get("dj")
                je = detail.get("je")
                
                result = session.query(MdxStore).filter(MdxStore.djbh==djbh, MdxStore.dj_sn==dj_sn).first()
                if result:
                    pass
                else:
                    lis.append(
                            MdxStore(djbh=djbh, rq=rq, ontime=ontime, 
                                    dwbh=dwbh, djje=djje, beizhu=beizhu, 
                                    dj_sn=dj_sn, spid=spid, pihao=pihao, 
                                    sxrq=sxrq, baozhiqi=baozhiqi, shl=shl, dj=dj, je=je)
                    )
        try:
            session.add_all(lis)
            session.commit()
            session.close()
        except Exception as e:
            session.rollback()
            session.close()
            current_app.logger.error("服务器异常！异常信息：{}".format(e))
            return jsonify(err='err', errmsg= "服务器异常！")
                
        return jsonify(err='OK', errmsg='成功！')
    else:
        current_app.logger.error("请求参数不能为空！")
        return jsonify(err='err', errmsg='请求参数不能为空！')

