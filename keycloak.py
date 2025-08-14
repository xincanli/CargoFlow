import requests

# ===== 配置部分 =====
KEYCLOAK_HOST = "http://120.55.195.144:8989/"     # Keycloak 地址
REALM = "neone"                                  # 你的 realm 名称

# 用 client_credentials 模式获取 token
CLIENT_ID = "neone-client"
CLIENT_SECRET = "lx7ThS5aYggdsMm42BP3wMrVqKm9WpNY"

# 要操作的用户名
TARGET_USERNAME = "ff"

# 要修改或创建的属性
ATTRIBUTES = {
    "logistics_agent_uri": [
        "http://49.235.163.153:8080/logistics-objects/7c2e19e..."
    ]
}

# 新用户的初始密码（只有创建时才会设置）
INITIAL_PASSWORD = "123456"
# ===================


def get_admin_token():
    """获取管理员 Access Token（client_credentials 模式）"""
    token_url = f"{KEYCLOAK_HOST}/realms/master/protocol/openid-connect/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    resp = requests.post(token_url, data=data)
    if resp.status_code != 200:
        raise RuntimeError(f"获取 Token 失败: {resp.status_code} {resp.text}")
    return resp.json()["access_token"]


def get_user_id(token, username):
    """根据用户名查找用户 ID"""
    url = f"{KEYCLOAK_HOST}/admin/realms/{REALM}/users"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"username": username}
    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code != 200:
        raise RuntimeError(f"查询用户失败: {resp.status_code} {resp.text}")
    users = resp.json()
    return users[0]["id"] if users else None


def create_user(token, username, attributes, password=None):
    """创建新用户，可选设置初始密码"""
    url = f"{KEYCLOAK_HOST}/admin/realms/{REALM}/users"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {
        "username": username,
        "enabled": True,
        "attributes": attributes
    }
    resp = requests.post(url, headers=headers, json=payload)
    if resp.status_code not in (201, 204):
        raise RuntimeError(f"创建用户失败: {resp.status_code} {resp.text}")
    print(f"已创建用户 {username}")

    # 获取新创建的用户 ID
    user_id = get_user_id(token, username)

    # 如果提供了初始密码，就设置
    if password:
        set_user_password(token, user_id, password)


def set_user_password(token, user_id, password):
    """为用户设置密码"""
    url = f"{KEYCLOAK_HOST}/admin/realms/{REALM}/users/{user_id}/reset-password"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {
        "type": "password",
        "value": password,
        "temporary": False
    }
    resp = requests.put(url, headers=headers, json=payload)
    if resp.status_code != 204:
        raise RuntimeError(f"设置密码失败: {resp.status_code} {resp.text}")
    print(f"已为用户 {user_id} 设置密码")


def update_user_attributes(token, user_id, attributes):
    """更新用户属性"""
    url = f"{KEYCLOAK_HOST}/admin/realms/{REALM}/users/{user_id}"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"attributes": attributes}
    resp = requests.put(url, headers=headers, json=payload)
    if resp.status_code != 204:
        raise RuntimeError(f"更新用户属性失败: {resp.status_code} {resp.text}")
    print(f"用户 {user_id} 属性已更新")


if __name__ == "__main__":
    try:
        print("获取管理员 Token...")
        token = get_admin_token()

        print(f"查找用户 {TARGET_USERNAME} ...")
        user_id = get_user_id(token, TARGET_USERNAME)

        if user_id:
            print(f"找到用户 ID: {user_id}，正在更新属性...")
            update_user_attributes(token, user_id, ATTRIBUTES)
        else:
            print(f"未找到用户 {TARGET_USERNAME}，正在创建...")
            create_user(token, TARGET_USERNAME, ATTRIBUTES, password=INITIAL_PASSWORD)

        print("完成！")
    except Exception as e:
        print("执行失败：", e)
