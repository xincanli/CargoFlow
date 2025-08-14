class Assertions:
    def assert_status_code(self,resp, expected=100):
        assert resp.status_code == expected, f'"期望:"{expected},"实际:"{resp.status_code}'

    def assert_status_field(self,resp, expected="access_token"):
        value = resp.json()
        assert expected in value, f'"成功获取token"'
