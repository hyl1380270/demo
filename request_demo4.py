# import requests
# data={'word':'hello'}
# # data={'key':'value'} 死循环？
# response = requests.post('https://httpbin.org/post',data=data)
# print(response.content)
# print('='*6+'response.status_code')
# print(response.status_code)
# print('='*6+"response.content.decode('utf8')")
# print(response.content.decode())
# print('='*6+'response.text')
# print(response.text)
#


# import requests
# # data={'word':'hello'}
# # data={'key':'value'} 死循环？
# # response = requests.post('https://httpbin.org/post',data=data)
# response = requests.put('http://httpbin.org/put',data={'key':'value'})
# print(response.content)
# print('='*6+'response.status_code')
# print(response.status_code)
# print('='*6+"response.content.decode('utf8')")
# print(response.content.decode())
# print('='*6+'response.text')
# print(response.text)
#
import  requests
# response = requests.delete('http://httpbin.org/delet')
# response = requests.head('http://httpbin.org/get')
# response = requests.options('http://httpbin.org/get')
#
#
#
# print('='*6+'response.status_code')
# print(response.status_code)
# #200:成功
# print('='*6+'response.url')
# print(response.url)
# print('='*6+'response.headers')
# print(response.headers)
# print('='*6+'response.cookies')
# print(response.cookies)
# print('='*6+'response.text') #去掉了\r\n
# print(response.text)
# print('='*6+'response.content') #保留了\r\n
# print(response.content)
# print('='*6+"response.content.decode('utf-8')") #显示\r\n
# print(response.content.decode('utf-8'))


#
# import  requests
# response = requests.options('http://httpbin.org/get')
# #
# print('='*6+'response.status_code')
# print(response.status_code)
# #200:成功
# print('='*6+'response.url')
# print(response.url)
# print('='*6+'response.headers')
# print(response.headers)
# print('='*6+'response.cookies')
# print(response.cookies)
# print('='*6+'response.text') #去掉了\r\n
# print(response.text)
# print('='*6+'response.content') #保留了\r\n
# print(response.content)
# print('='*6+"response.content.decode('utf-8')") #显示\r\n
# print(response.content.decode('utf-8'))


import requests

payload={'key1':'value1','key2':'value2'}
response=requests.get('http://httpbin.org/get',params=payload)
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