from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DECIMAL
from sqlalchemy.orm import sessionmaker


engine = create_engine("")   # 请求服务数据库地址mssql+pymssql://服务名称:服务密码@服务地址/数据库名称 （这里用的是sql server数据库）
Base = declarative_base()
DBSession = sessionmaker(bind=engine)

class MdxStore(Base):
    __tablename__ = "mdx_store_ckmx"
    id = Column(Integer, primary_key=True)
    djbh = Column(String(15))
    rq = Column(String(10))
    ontime = Column(String(10))
    dwbh = Column(String(11))
    djje = Column(DECIMAL(14,3))
    beizhu = Column(String(80))
    dj_sn = Column(Integer)
    spid = Column(String(11))
    pihao = Column(String(20))
    sxrq = Column(String(10))
    baozhiqi = Column(String(10))
    shl = Column(DECIMAL(14,2))
    dj = Column(DECIMAL(14,2))
    je = Column(DECIMAL(14,2))


# session = DBSession()
# store = session.query(MdxStore).all()
# print(store)