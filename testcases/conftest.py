import sys
import os

# 将项目根目录添加到 sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from common.yaml_util import YamlUtil


@pytest.fixture(scope="function")
def conn_database():
    print("连接数据库")
    yield
    print("关闭数据库")


@pytest.fixture(scope="session",autouse=True)
def clear_yaml():
    YamlUtil().clear_extract_yaml()
