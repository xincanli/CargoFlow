import sys
import os
import re
import requests
import pytest

# 将项目根目录添加到 sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common.logger_util import logger, log_decorator
from common.yaml_util import YamlUtil
from common.requests_util import RequestsUtil
from assertions import Assertions

yaml_util = YamlUtil()
request_util = RequestsUtil()
assertion = Assertions()


class TestBooking:
    session = requests.Session()

    @pytest.mark.parametrize("caseinfo", yaml_util.read_testcase_yaml('get_token.yaml'))
    def test_get_token(self, caseinfo):
        method = caseinfo["request"]["method"]
        url = caseinfo["request"]["url"]
        data = caseinfo["request"]["data"]
        headers = caseinfo["request"].get("headers", {})
        resp = request_util.send_request(method, url, data, headers=headers)

        token_key = caseinfo.get("name", "access_token")
        expected_status = caseinfo["validate"]["status_code"]

        rep = resp.json()
        assertion.assert_status_code(resp, expected=expected_status)
        yaml_util.write_extract_yaml({token_key: rep["access_token"]})

    @pytest.mark.parametrize("caseinfo2", yaml_util.read_testcase_yaml('output_flow.yaml'))
    @log_decorator
    def test_create_shipment(self, caseinfo2):
        name = caseinfo2["name"]
        method = caseinfo2["request"]['method']
        url = yaml_util.replace_variables(caseinfo2['request']['url'])
        headers = caseinfo2["request"].get("headers", {})
        data = yaml_util.replace_variables(caseinfo2["request"].get("data", {}))
        token_key = caseinfo2.get("token_key", "access_token")
        wait = caseinfo2.get("wait", None)
        expected_status = caseinfo2["validate"]["status_code"]

        LogistObject = request_util.send_request(
            method, url, data, headers=headers, use_token=True,
            token_key=token_key, wait=wait
        )

        if "logistics-objects?" in url or "access-delegations" in url:
            loid = ''.join(re.findall(r'[a-zA-Z]+', name))
            yaml_util.write_extract_yaml({loid: LogistObject.headers.get("Location")})

        assertion.assert_status_code(LogistObject, expected=expected_status)
