# -*- coding: utf-8 -*-
import json
import sys
import jieba as jieba

from howarddb import ScopedSession
from howarddb.bean_baseinfo import BaseInfo

reload(sys)

sys.setdefaultencoding('utf8')
se=ScopedSession()

def maketags():
    list_rules= se.query(BaseInfo).all()
    for r in list_rules:
        tags_data=''
        tags_data_utf8=''
        tmp_apply_elements=''
        tmp_english_elements=''
        tmp_name=''
        tmp_tax_code=''

        if r.name is not None:
            tmp_name=r.name

        if r.tax_code is not None:
            tmp_tax_code=r.tax_code

        if r.apply_elements is not None:
            tmp_apply_elements=r.apply_elements

        if r.english_elements is not None:
                tmp_apply_elements = r.english_elements

        tags=[]

        tags_input_str=tmp_name+tmp_tax_code+" "+tmp_english_elements+tmp_apply_elements
        seg_list = jieba.cut(tags_input_str, cut_all=False)

        for word in seg_list:
            #过滤掉无用的字符
            if word ==" ":
                continue
            if word=="*":
                continue
            if word==",":
                continue

            tags.append(word)

        tags_data=json.dumps(list(set(tags)))
        tags_data=str(tags_data).replace('u\'','\'').decode("unicode-escape")

        tags_data_utf8=json.dumps(list(set(tags)))

        r.tags_utf8=tags_data_utf8
        r.tags=tags_data
        # print(tags_data)
    se.commit()


def get_keyword(str):
    tags = []
    seg_list = jieba.cut(str, cut_all=False)
    for word in seg_list:
        tags.append(word)
    return tags




maketags()