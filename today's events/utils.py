import requests
import json
import random
class date(object):
    def __init__(self,mon,day) :
        self.mon=mon
        self.day=day
    
    def get_todevs(self):
        ur1=['http://v.juhe.cn/todayOnhistory/queryEvent.php?key=682113ee2a424366fbe63fb494b4fdce&date=',str(self.mon),'/',str(self.day)]
        r=requests.get(''.join(ur1))
        evs=json.loads(r.text)
        max=int(evs['result'][-1]["e_id"])-int(evs['result'][0]["e_id"])
        x=[evs['result'][i]['title'] for i in range(1,max)]
        return "\n".join(x)


    



        