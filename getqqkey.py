from urllib import request
import json
import re
import requests.cookies

class QQKey:
    
    cookies=requests.cookies.RequestsCookieJar()
    qiu=request.build_opener(request.HTTPCookieProcessor(cookies))
    qiu.addheaders = [('Referer','https://xui.ptlogin2.qq.com')]
    def __gettoken(self):
        self.__class__.qiu.open('https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=1006102&daid=1&style=23&hide_border=1&proxy_url=http%3A%2F%2Fid.qq.com%2Flogin%2Fproxy.html&s_url=http://id.qq.com/index.html')
        for key in self.__class__.cookies:
            if(key.name == 'pt_local_token'):
                return key.value
    
    def uins(self):
        url='https://localhost.ptlogin2.qq.com:4301/pt_get_uins?callback=ptui_getuins_CB&r=0.21624413130736064&pt_local_tk={}'.format(self.__gettoken())
        res=self.__class__.qiu.open(url)
        uin=json.loads(re.compile('var var_sso_uin_list=(.*?);').findall(str(res.read(),'utf-8'))[0])
        return uin[0]['account']
    def qqkeys(self):
        url = 'https://localhost.ptlogin2.qq.com:4301/pt_get_st?clientuin={0}&callback=ptui_getst_CB&r=0.810010167110566&pt_local_tk={1}'.format(self.uins(),self.__gettoken()) 
        self.__class__.qiu.open(url)
        for keys in self.__class__.cookies:
            if (keys.name == 'clientkey'): 
                return keys.value




