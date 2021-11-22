import requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException

for a in range(0,50):
    try:
        response=requests.get('https://baidu.com/',timeout=0.05)
        print(response.status_code)
    except ReadTimeout:
        print('timeout')
    except HTTPError:
        print('httpserver')
    except RequestException:
        print('referrer')
    except Exception as e:
        print('超时'+str(e))