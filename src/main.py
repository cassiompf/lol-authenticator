import requests
from requests.auth import HTTPBasicAuth
from lcu import LcuInfo

lcu_info = LcuInfo()

lcu_port = lcu_info.access_port
lcu_endpoint = f'https://127.0.0.1:{lcu_port}/rso-auth/v1/session/credentials'
lcu_password = lcu_info.remoting_auth_token
lcu_user = 'riot'

print()
print(f'LCU Token Access: {lcu_password}.')
print(f'LCU Port: {lcu_port}.')
print()

user_nickname = 'your-nickname'
user_password = 'your-password'

payload = {
  'username': user_nickname,
  'password': user_password,
  'persistLogin': False
}

response = requests.put(lcu_endpoint, json=payload, verify=False, auth=(lcu_user, lcu_password))

print(response.json())
