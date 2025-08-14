import os

import yaml
import re


class YamlUtil:
    def read_extract_yaml(self, key):
        file_path = os.path.join(os.getcwd(), "extract.yaml")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"extract.yaml 不存在，无法读取键: {key}")
        with open(file_path, mode="r", encoding="utf-8") as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            if not value:
                raise KeyError(f"extract.yaml 为空或内容无效，无法读取键: {key}")
            if key not in value:
                raise KeyError(f"extract.yaml 中不存在键: {key}")
            return value[key]

    def write_extract_yaml(self, data):
        file_path = os.path.join(os.getcwd(), "extract.yaml")
        # 读取现有内容，合并后整体写回，避免多文档导致读取为 None
        existing = {}
        if os.path.exists(file_path):
            with open(file_path, mode="r", encoding="utf-8") as rf:
                loaded = yaml.load(rf, Loader=yaml.FullLoader)
                if isinstance(loaded, dict):
                    existing = loaded
        if not isinstance(data, dict):
            raise ValueError("write_extract_yaml 仅接受 dict 数据")
        existing.update(data)
        with open(file_path, mode="w", encoding="utf-8") as f:
            yaml.dump(data=existing, stream=f, allow_unicode=True)
            # print("token写入成功")

    def clear_extract_yaml(self):
        file_path = os.path.join(os.getcwd(), "extract.yaml")
        with open(file_path, mode="w", encoding="utf-8") as f:
            f.truncate()

    def read_testcase_yaml(self, yaml_name):
        file_path = os.path.join(os.getcwd(), f"testcases\\{yaml_name}")
        with open(file_path, mode="r", encoding="utf-8") as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
        return value

    def replace_variables(self, data):
        if isinstance(data, dict):
            return {k: self.replace_variables(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self.replace_variables(i) for i in data]
        elif isinstance(data, str):
            match = re.findall(r"\$\{(.*?)\}", data)
            for m in match:
                value = self.read_extract_yaml(m)
                data = data.replace(f"${{{m}}}", str(value))
            return data
        else:
            return data
    def pytest_generate_tests(self,metafunc):
        if "test_case" in metafunc.fixturenames:
            test_cases = self.read_testcase_yaml("create_BookingShipment.yaml")
            # 提取用例名作为 pytest 的显示 ID
            case_names = [tc["name"] for tc in test_cases]
            metafunc.parametrize("test_case", test_cases, ids=case_names)
