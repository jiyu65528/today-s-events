import requests
import json
import random
from datetime import date

class Date(object):
    def __init__(self,mon,day) :
        self.mon=mon
        self.day=day
    
    
    def isValidDate(self):
        try:
            date(2023,int(self.mon),int(self.day))
        except:
            return False
        else:
            return True

    def get_todevs(self):
        ur1=['http://v.juhe.cn/todayOnhistory/queryEvent.php?key=682113ee2a424366fbe63fb494b4fdce&date=',str(self.mon),'/',str(self.day)]
        r=requests.get(''.join(ur1))
        evs=json.loads(r.text)
        max=int(evs['result'][-1]["e_id"])-int(evs['result'][0]["e_id"])
        x=[evs['result'][i]['date']+"\t"+evs['result'][i]['title'] for i in range(1,max)]
        return "\n".join(x)


    



        