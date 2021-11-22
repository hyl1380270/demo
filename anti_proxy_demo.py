import socket

import requests
proxy = {'http': 'http://http://240.0.0.3:1082', 'https': 'https://http://240.0.0.3:1082'}
response = requests.get('http://www.mingrisoft.com/', proxies=proxy)
print(response.content)
print(socket.getaddrinfo('http://www.mingrisoft.com/',80))
# 上述程序没有pass
