import json
import time

import requests
from common.yaml_util import YamlUtil
from common.logger_util import logger, log_decorator

yaml_util = YamlUtil()


class RequestsUtil:
    session = requests.Session()


    def send_request(self, method, url, data=None, headers=None, use_token=False,token_key="access_token",wait=None, **kwargs):
        method = str(method).lower()

        if headers is None:
            headers = {}

        if use_token:
            token = yaml_util.read_extract_yaml(token_key)
            headers["Authorization"] = f"Bearer {token}"

        if wait:
            time.sleep(wait)

        if method == "get":
            rep = RequestsUtil.session.request(method, url, params=data, headers=headers, **kwargs)
        else:
            if headers.get("Content-Type") == "application/x-www-form-urlencoded":
                rep = RequestsUtil.session.request(method, url, data=data, headers=headers, **kwargs)
            else:
                # print(f"请求头{headers}")
                rep = RequestsUtil.session.request(method, url, json=data, headers=headers, **kwargs)


        logger.info(f"响应状态码: {rep.status_code}")
        logger.debug(f"响应内容: {rep.text}")
        return rep
