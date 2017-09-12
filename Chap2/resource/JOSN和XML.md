### API 返回数据的格式：JOSN 和 XML  

<br> JSON 是一种比较流行的数据格式，像 Python 中 list 和 dict 的组合体；XML 用于在不同的程序之间存储和传输数据。
<br>[JSON 官方文档](http://www.json.org/)
<br>[JSON 语法 - w3school](http://www.w3school.com.cn/json/index.asp)
<br>[XML 语言 - w3school](http://www.w3school.com.cn/xml/xml_intro.asp)

> 假设某 API 返回以下格式的 JSON 数据，如何取出温度呢？

    假设某 API 返回以下格式的 JSON 数据，如何取出温度呢？

```{
  "results": [{
  "location": {
      "id": "C23NB62W20TF",
      "name": "西雅图",
      "country": "US",
      "timezone": "America/Los_Angeles",
      "timezone_offset": "-07:00"
  },
  "now": {
      "text": "多云",
      "code": "4", 
      "temperature": "14", 
      "feels_like": "14",
      "pressure": "1018", 
      "humidity": "76", 
      "visibility": "16.09",
      "wind_direction": "西北", 
      "wind_direction_degree": "340", 
      "wind_speed": "8.05", 
      "wind_scale": "2", 
      "clouds": "90", 
      "dew_point": "-12" 
  },
  "last_update": "2015-09-25T22:45:00-07:00" 
  }]
}
```
### API 集市
<br>腾讯云 API 服务：[云 API - 腾讯云](https://www.qcloud.com/product/api)，可重点参考：[API 文档 - 帮助与文档 - 腾讯云](https://www.qcloud.com/document/api)
<br><br>百度 API Store：[API Store_为开发者提供最全面的 API 服务](http://apistore.baidu.com/)
<br><br>百度人工智能 API 服务：[百度大脑](http://ai.baidu.com/index/)
<br><br>京东 API 数据服务：[API 数据免费数据数据定制_京东万象官网—综合数据开放平台](http://wx.jcloud.com/)
<br><br>常用的 SAAS 服务比较网站，多数提供了 API：[SDK.CN - 中国领先的开发者服务平台](https://www.sdk.cn/)
<br><br>常见金融类、征信类数据 API 服务：[大数据交易平台 - 199IT 数据导航网站 --Hao.199it.com](http://hao.199it.com/jiaoyi.html)
<br><br>创业公司常用的第三方服务 API ：[北京创业工具箱 - 阳志平的网志](http://www.yangzhiping.com/info/startup.html)

