import requests
import os
import random
# from requests_toolbelt import MultipartEncoder
"""
封装常用的方法
"""


def post(header, url, request_parameter_type, timeout=20, data=None, files=None, cookie=None):
    # pass

    # if 'form_data' in request_parameter_type:
    #     for i in files:
    #         value = files[i]
    #         if '/' in value:
    #             file_parm = i
    #             files[file_parm] = (os.path.basename(value), open(value, 'rb'))
    #     enc = MultipartEncoder(
    #         fields=files,
    #         boundary='--------------' + str(random.randint(1e28, 1e29 - 1))
    #     )
    #     header['Content-Type'] = enc.content_type
    #
    #     response = requests.post(url=url, data=enc, headers=header, timeout=timeout, cookies=cookie)

    if 'data' in request_parameter_type:
        response = requests.post(url=url, data=data, headers=header, timeout=timeout, files=files, cookies=cookie)

    elif 'json' in request_parameter_type:
        response = requests.post(url=url, json=data, headers=header, timeout=timeout, files=files, cookies=cookie)

    return response.status_code, response.json()


def get(header, url, data, timeout=20, cookie=None):
    response = requests.get(url=url, params=data, headers=header, timeout=timeout, cookies=cookie)
    return response.status_code, response.json()

