import requests  # 导入库
import base64

# 账号
USERNAME = ''
# 密码
PASSWORD = ''
# 运营商：移动CMCC 联通Unicom 电信ChinaNet
DOMAIN = ''


# 定义了函数
def login(username='', password='', domain=''):
    password = base64.b64encode(password.encode()).decode()  # base64加密。。
    url = "http://a.nuist.edu.cn/index.php/index/login"
    dv = {  # 构造data
        'username': username,
        'domain': domain,
        'password': password,
        'enablemacauth': 0
    }
    try:  # 用try来防止未知错误。
        r = requests.post(url, data=dv)  # 发送post
        r.raise_for_status()  # 错误抛出异常
        return r.json()  # 返回json格式的数据
    except:
        print('error')


dic = login(USERNAME, PASSWORD, DOMAIN)
for i in list(dic.keys()):
    if dic[i]:
        print(i + ":" + str(dic[i]))  # 输出登陆信息，成功与否
