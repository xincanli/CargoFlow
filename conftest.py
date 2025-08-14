def pytest_make_parametrize_id(config, val, argname):
    # 如果是 YAML 用例字典并且有 name
    if isinstance(val, dict) and 'name' in val:
        return val['name']
    return repr(val)