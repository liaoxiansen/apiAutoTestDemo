"""
json格式
1、json有对象和数组两种结构，有字符串，数字，逻辑值，空值四种数据类型
2、用大括号{}表示对象，对象室友属性组成的，属性是由键值对组成的，键和值之间用冒号隔开，属性之间用逗号隔开，键必须用双引号引起来
3、用中括号[]表示数组，数组由单独的值组成
4、json的灵活就灵活在json可以嵌套

token- 令牌
1、token由服务器产生的，存在服务器的内存或硬盘中
2、有一套产生的规则，会涉及到加密算法、
3、有一定的时效性

cookie
1、cookie 是分站点的，站点和站点之间的cookie是相互独立
2、浏览器的cookie是保存在浏览器的某个位置的
3、服务器端可以通过，相应头中的set-cookie参数，对客户端的cookie进行管理
4、历览器的每次请求，都会把该站点的cookie发送给服务器
5、实现登录 cookie + session 配合使用、

session
1、session是一个对象，是服务器产生的，保存在服务器的内存中
2、session有自己的管理机制，包括session产生，销毁，超时等
3、sessionID是session对象的一个属性，是全局唯一的，永远都不会重复

用户登录成功服务器创建session，返回给客户端，客户端浏览器把session保存在他的cookie中


登录成功服务器立马创建session，并通过【响应头】中的set-cookie属性把session返回给客户端
浏览器把响应头中的set-cookie内容保存起来，存在浏览器自己的cookie中
以后浏览器每次发送请求时，都会把站点的全部cookie通过请求头中，传递给服务器

"""

# 登录接口
import requests
import hashlib


# md5加密
def get_md5(value):
    # 实例化一个对象
    md5 = hashlib.md5()
    # 加密操作
    md5.update(value.encode(encoding='utf-8'))
    # 返回十六进制
    return md5.hexdigest()


# print(get_md5("111111"))
# 设置代理
fiddler_proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888",
}


def test_login(inData, getToken=True):
    url = "http://121.41.14.39:8082/account/sLogin"
    inData['password'] = get_md5(inData['password'])
    param = inData

    # 设置代理
    # res = requests.post(url, params=param, proxies=fiddler_proxies)
    res = requests.post(url, data=param)
    # # 打印请求url
    # print(res.request.url)
    # # 请求body
    # print(res.request.body)
    # print(res.status_code)
    # print(res.text)

    # 判断getToken是否为真
    if getToken:
        # 获取token
        print(res.json()["data"]["token"])
        return res.json()["data"]["token"]
    else:
        # 打印字典类型的返回值
        print(res.json(), type(res.json()))
        return res.json()


param = {
        'username': 'sq0658',
        'password': "111111"
    }

test_login(param)