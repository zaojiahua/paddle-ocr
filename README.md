# 接口调用说明
## 请求ocr服务

路径：/ocr

方法：POST

参数说明：支持表单和json俩种传参方式。

1. image_body File类型，需要传入一张要识别的图片，必传。
2. words string类型，非必传，传入以后代表查看该图片中是否包含指定的文字。

返回值：
status string类型，success表示请求成功，fail代表请求失败。
result array类型，每个元素是一个dict类型，dict中的text代表识别的文字，cx，cy代表文字的中心点坐标。

### Python代码示例

```python
import requests
import os


def ocr_request(pic_path, words=None):
    assert (pic_path is not None and os.path.exists(pic_path))

    response = requests.request('POST', 'http://10.0.0.56:8089/ocr', timeout=120.0, files={"image_body": open(pic_path, "rb")},
                       data={'words': words})

    return response

print(ocr_request('picture.png').json())

# {
#     'result': [
#     {
#         'cx': 345.0,
#         'cy': 588.5,
#         'text': '病毒扫描'
#     },
#     {
#         'cx': 347.0,
#         'cy': 751.0,
#         'text': '优化加速'
#     },
#     {
#         'cx': 82.5,
#         'cy': 917.0,
#         'text': '游戏加速'
#     },
#     {
#         'cx': 346.5,
#         'cy': 913.5,
#         'text': '应用管理'
#     },
#     {
#         'cx': 108.5,
#         'cy': 939.0,
#         'text': '提升游戏网络稳定性'
#     },
#     {
#         'cx': 360.0,
#         'cy': 937.0,
#         'text': '56个应用有更新'
#     },
#     {
#         'cx': 186.0,
#         'cy': 988.0,
#         'text': '安全中心'
#     },
#     {
#         'cx': 458.5,
#         'cy': 1030.5,
#         'text': '开启速抢'
#     }],
#     'status': 'success'
# }
```

## 网页测试地址

1. 路径：/test
2. 功能：通过浏览器打开该地址，即可测试ocr接口，操作方便，便于调试。


## 客户ocr服务器地址

### ip
美的：10.80.43.138

### 端口
1. ocr1: 8089
2. ocr2: 8090
3. ocr3: 8091（算法效果较好，支持中英文，部分客户没有部署）
