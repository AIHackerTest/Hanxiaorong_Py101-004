# coding=utf-8

# 数据来自心知天气
# API 密钥：key = sxajxblmndgut1d6
# 用户ID = U9A94670D4

import requests
print("这是一个天气查询系统，所有数据来源于《心知天气》")
print("请按照提示操作，如需帮助请按h或help\n")
print('-'*50)
now_api = 'https://api.seniverse.com/v3/weather/now.json'
daily_api = 'https://api.seniverse.com/v3/weather/daily.json'

def fetchweather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json',params={
    'key':'sxajxblmndgut1d6',
    'location':location,
    'language':'zh-Hans',
    'unit':'c'},timeout=1) # timeout表示经过多久后取消等待
    return result.json() # 这里写json()时少了括号，导致后面显示不出数据

city_history = []

while True:
    city = input("请输入你要查询的城市名：")
    try:
        tar = fetchweather(city)
    #print(tar)
        city_name = tar['results'][0]['location']['name'] #TypeError: 'method' object is not subscriptable出现这个错误说明json()没写对
        text = tar['results'][0]['now']['text']
        temperature = tar['results'][0]['now']['temperature']
        update = tar['results'][0]['last_update'][:-6].replace('T', ' ')

        print('您查询的城市名为:\t%s' %city_name)
        print("该城市的天气为: \t%s" %text)
        print('该城市的气温为: \t%s' %temperature)
        print('天气更新时间为: \t%s' %update)#这里注释掉，输入城市就不会打印相关天气信息，但是查询历史后面的weather_info依然可以打印
        weather_info = f'您查询的城市名为:{city_name}\n该城市的天气为:{text}\n该城市的气温为:{temperature}\n天气更新时间为:{update}\n'
        #print(weather_info)
        city_history.append(weather_info)
    except KeyError:
        if city == 'h' or city == 'help':
            print('''
                输入城市名,查询该该城市的天气;
                输入help,获取帮助文档;
                输入history,获取查询历史;
                输入quit,退出天气查询系统.
                ''')
        elif city == 'history':
            if city_history:
               for item in city_history:
                   print(item)
            else:
                print('你还没有查询历史。')
        elif city == 'quit' or city == 'q':
            print('你已退出查询程序。')
            break
        else:
            print('对不起，你输入的城市不存在，请检查后重新输入。')
