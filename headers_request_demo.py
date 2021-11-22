import requests
url='https://www.baidu.com/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68'}
response=requests.get(url,headers=headers)
print('='*6+'response.status_code')
print(response.status_code)
#200:成功
print('='*6+'response.url')
print(response.url)
print('='*6+'response.headers')
print(response.headers)
print('='*6+'response.cookies')
print(response.cookies)
print('='*6+'response.text') #去掉了\r\n
print(response.text)
print('='*6+'response.content') #保留了\r\n
print(response.content)
print('='*6+"response.content.decode('utf-8')") #显示\r\n
print(response.content.decode('utf-8'))