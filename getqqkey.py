import requests
import json
import re

class QQKey:

    s = requests.Session()
    s.headers.update({
            'Referer': 'https://xui.ptlogin2.qq.com'
        })
    
    def __gettoken(self):                
        self.__class__.s.get('https://xui.ptlogin2.qq.com/cgi-bin/xlogin?appid=1006102&daid=1&style=23&hide_border=1&proxy_url=http%3A%2F%2Fid.qq.com%2Flogin%2Fproxy.html&s_url=http://id.qq.com/index.html')
        for key in self.__class__.s.cookies:
            if key.name == 'pt_local_token':
                return key.value
    
    def getuin(self):
        r=self.__class__.s.get(f'https://localhost.ptlogin2.qq.com:4301/pt_get_uins?callback=ptui_getuins_CB&r=0.21624413130736064&pt_local_tk={self.__gettoken()}')
        match = re.search(r'var var_sso_uin_list=(.*?);', r.text)
        if match:
            uin_data = json.loads(match.group(1))
            return uin_data[0]['account']
    
    def getqqkey(self):        
        self.__class__.s.get(f'https://localhost.ptlogin2.qq.com:4301/pt_get_st?clientuin={self.getuin()}&callback=ptui_getst_CB&r=0.810010167110566&pt_local_tk={self.__gettoken()}')
        for key in self.__class__.s.cookies:
            if key.name == 'clientkey':
                return key.value


if __name__ == "__main__":
    qq_key = QQKey()
    
    print(f"QQ: {qq_key.getuin()} KEY: {qq_key.getqqkey()}")
    
