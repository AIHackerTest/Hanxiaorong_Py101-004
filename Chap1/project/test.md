## 1. 代码格式问题：
#### 这个文件 weather_task.py:

<details>
<summary>More details</summary>

```diff
--- 
+++ 
@@ -1,36 +1,35 @@
-from sys import exit
-weather = {}
-
-with open('G:\learnpython\Task\Ch1\weather_info.txt',encoding='utf-8') as f:
-    for target in f:
-        (key,val)=target.split(',')
-        #print(target)
-        weather[key]=val
-        #print(weather[key])
-    
-print("欢迎来到天气查询页面，如需帮助，请输入help或h\n")
-
-history =''
-while True:
-    order = input('请输入查询的城市：')
-    if order in ["help","h"]:#换成 if order == 'help' or 'h'：不行？
-        print("""
-        输入城市名，查询该城市的天气；
-        输入 help，获取帮助文档；
-        输入 history，获取查询历史；
-        输入 quit，退出天气查询系统
-    """)
-    elif order == 'history':
-        print(history)
-    
-    elif order in['quit','exit']:
-        exit(0)
-   
-    else:
-        city = weather.get(order)
-        if not city:
-            print("***请输入正确的城市名：")
-        else:
-            print("%s的天气为: %s" %(order,weather[order]))
-            history = history + order + weather[order] + '\n'
-            
+from sys import exit
+weather = {}
+
+with open('G:\learnpython\Task\Ch1\weather_info.txt', encoding='utf-8') as f:
+    for target in f:
+        (key, val) = target.split(',')
+        #print(target)
+        weather[key] = val
+        #print(weather[key])
+
+print("欢迎来到天气查询页面，如需帮助，请输入help或h\n")
+
+history = ''
+while True:
+    order = input('请输入查询的城市：')
+    if order in ["help", "h"]:  #换成 if order == 'help' or 'h'：不行？
+        print("""
+        输入城市名，查询该城市的天气；
+        输入 help，获取帮助文档；
+        输入 history，获取查询历史；
+        输入 quit，退出天气查询系统
+    """)
+    elif order == 'history':
+        print(history)
+
+    elif order in ['quit', 'exit']:
+        exit(0)
+
+    else:
+        city = weather.get(order)
+        if not city:
+            print("***请输入正确的城市名：")
+        else:
+            print("%s的天气为: %s" % (order, weather[order]))
+            history = history + order + weather[order] + '\n'
```

</details>


## 2. 代码相似问题：


## 3. 复杂度及其他问题：