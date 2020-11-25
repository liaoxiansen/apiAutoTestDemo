from core import apiMethod


def send_request(data, url):
# def send_request(data, host, url, _path, relevance=None):
#     result = apiMethod.post(header={"Authorization":"token"},
#                             url=host + url,
#                             request_parameter_type="json",
#                             data=data
#                             )
    result = apiMethod.get(header=None,url=url, data=data)
    return result


if __name__ == '__main__':
    host = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    url = host
    # data = 'corpid=wwf787d5b0ce9fb79c&corpsecret=Cj4PwDuoppPER69YGs-xHA96ZY2a7dB4PXW03ZsW4HE'
    data = {
        "corpid" : "wwf787d5b0ce9fb79c",
    "corpsecret": "Cj4PwDuoppPER69YGs-xHA96ZY2a7dB4PXW03ZsW4HE"
    }
    res = send_request(url=url, data=data)
    print(res[1])

    import jsonpath
    token = jsonpath.jsonpath(res[1], "$.access_token")
    print(token)


"""
python里线程与协程的区别
进程是资源分配的单位
线程是操作系统调度的单位
协程，又称微线程，纤程，协程的切换只是单纯的操作CPU的上下文，资源很小，效率高
进程切换需要的资源很最大，效率很低
一个程序至少有一个进程,一个进程至少有一个线程
线程执行开销小，但不利于资源的管理和保护；而进程正相反
"""
