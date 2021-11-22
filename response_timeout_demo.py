import requests
i=0
j=0
k=0
for a in range(0,50):
    try:
        i+=1
        response=requests.get('https://www.baidu.com',timeout=0.1)
        print('第',i,'次：  ')
        print(response.status_code)

    except Exception as e:
        j+=1
        # print('第'+i+'次'+'异常：  ',str(e))
        print('第' , i ,'次' + '异常：  ')
        print(str(e))

    print('共',j,'次超时！比例为（超时次数/总get次数）：',j/50)
