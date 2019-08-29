# -*- coding: utf-8 -*-
from sqlalchemy import  *
from sqlalchemy.orm import *


engine = create_engine('sqlite:///./howarddb/db/howard.db',encoding='utf-8',echo=True)
metadata= MetaData(engine)

baseinfo_table=Table('baseinfo',
               metadata,
               Column('id',Integer,primary_key=True),
               Column('name',String(500)),
               Column('tax_code',String(500)),
               Column('cust_rate',Float(10,2)),
               Column('vat_rate',Float(10,2)),
               Column('general_rate',Float(18,5)),
               Column('amount',Float(18,2)),
               Column('weight',Float(18,3)),
               Column('unit',String(100)),
               Column('english_elements',String(500)),
               Column('apply_elements',String(500)),
               Column('tags',String(5000)),
               Column('tags_utf8',String(5000)),
               Column('md5',String(200)),
               Column('name_english',String(1000)),
               Column('unit_english',String(1000)),
               )
if not baseinfo_table.exists():
    baseinfo_table.create()


    # 记录变为dict，才能进行json.dumps处理，返回给接口
def columns_to_dict(self):
        dict_ = {}
        # for key in self.__mapper__.c.keys():
        #     dict_[key] = getattr(self, key)
        for key in self.__dict__:
            print(key)
            if key <>'_sa_instance_state':
                dict_[key] = getattr(self, key)
        return dict_
