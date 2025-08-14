import os
import json
from ruamel.yaml import YAML

DATA_DIR = "E:/python/pythonProject13/Data/data"
TEMPLATE_FILE = "E:/python/pythonProject13/Data/flow_template.yaml"
OUTPUT_FILE = "/testcases/temp/output_flow.yaml"



def load_json_files():
    """读取 Data/data 下的所有 JSON 文件"""
    json_data_map = {}
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".json"):
            path = os.path.join(DATA_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                json_data_map[filename] = json.load(f)
    return json_data_map


def update_yaml_with_json(json_data_map):
    """将 JSON 数据填充到流程 YAML 的 data 字段"""
    yaml_parser = YAML()
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        flow = yaml_parser.load(f)

    # 遍历流程步骤
    for step in flow:
        if "request" in step and "data" in step["request"]:
            data_field = step["request"]["data"]
            if isinstance(data_field, str) and data_field.endswith(".json"):
                json_filename = data_field
                if json_filename in json_data_map:
                    step["request"]["data"] = json_data_map[json_filename]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        yaml_parser.dump(flow, f)





if __name__ == "__main__":
    json_map = load_json_files()
    update_yaml_with_json(json_map)
    print(f"✅ 已生成 {OUTPUT_FILE}")
