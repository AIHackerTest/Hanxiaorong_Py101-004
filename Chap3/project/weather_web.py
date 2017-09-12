from flask import Flask,render_template,request # 方便后面使用template
import requests
app = Flask(__name__)

history_list = []
def fetchweather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json',params={
    'key':'sxajxblmndgut1d6',
    'location':location,
    'language':'zh-Hans',
    'unit':'c'},timeout=1)
    # return result.json()
    tar = result.json() #fetchweather(city)
    city_name = tar['results'][0]['location']['name'] #TypeError: 'method' object is not subscriptable出现这个错误说明json()没写对
    text = tar['results'][0]['now']['text']
    temperature = tar['results'][0]['now']['temperature']
    update = tar['results'][0]['last_update'][:-6].replace('T',' ')
    weather_info = f'''您查询的城市名为:{city_name}\n
                     该城市的天气为:{text}\n
                     该城市的气温为:{temperature}\n
                     天气更新时间为:{update}\n'''
    return (weather_info)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user_request')
def process_request():
    try:
        if request.args.get('help') == '帮助':
            return render_template('help.html')
        elif request.args.get('query') == '查询':
            city = request.args.get("city")
            weather_info = fetchweather(city)
            history_list.append(weather_info)
            return render_template('query.html',weather_info=weather_info)
        elif request.args.get("history") == "历史":
            return render_template('history.html',history_list = history_list)
    except KeyError:
        return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True) # 调试程序，这样每次修改程序后就不需要关闭服务器
