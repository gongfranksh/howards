# -*- coding: utf-8 -*-
import json

from sqlalchemy.orm import mapper
from howard_db import baseinfo_table
from howarddb import ScopedSession

class BaseInfo(object):
    pass
mapper(BaseInfo,baseinfo_table)


class ApplyLine(object):
    pass

def query_same_baseinfo(se,md5):
    query_result = se.query(BaseInfo).filter(BaseInfo.md5==md5).first()
    if query_result is not None:
        return False
    else:
        return True


def match_baseinfo(matchlist):
    rst=[]
    query_result = ScopedSession.query(BaseInfo).all()
    try:
        if query_result is not None:
            for ruls in query_result:
                if len(ruls.tags_utf8) <>0:
                    match_rules=json.loads(ruls.tags_utf8)
                else:
                    match_rules=[]
                matchlist=set(matchlist)
                match_rules=set(match_rules)
                result = matchlist & match_rules
                len_result=len(result)
                # print ('input   sku==>%s '
                #        'match rules==>%s '
                #        'result    ===>%s '
                #        'rules_id  ===>%d '
                #        'length    ===>%d '  %
                #        (uft8_2_str(matchlist),
                #         uft8_2_str(match_rules),
                #         uft8_2_str(result),
                #         ruls.id,
                #         len_result
                #         ))
                item={
                    'inputsku':matchlist,
                    'rules':match_rules,
                    'result':result,
                    'rules_id':ruls.id,
                    'length':len_result,
                }
                rst.append(item)
        if len(rst)!=0:
            rst=sorted(rst,key=lambda i:i['length'],reverse=True)
            return ScopedSession.query(BaseInfo).get(rst[0]["rules_id"])
        else:
            return None

    except Exception, e:
        print(e.message)
        return None