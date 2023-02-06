import datetime
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

executer = ThreadPoolExecutor()
path = "D:\\coral-ocr\\test_imgs"
big_pic_path = "desktop.png"
small_pic_path = "agree.jpg"
setting_path = "setting.jpg"


def send_request(i):
    try:
        response = requests.post(url="http://10.0.0.250:8089/ocr", files={"image_body": open(os.path.join(path, i),"rb"),})
        print(response.json())
    except Exception as e:
        print(repr(e))

print(os.listdir(path))
futureList = []
a = time.time()
for i in range(2):
    for j in os.listdir(path)[:10]:
        future = executer.submit(send_request, j)
        futureList.append(future)
for i in as_completed(futureList):
    pass
print(time.time() - a)



#2070s + r3 3700 = 0.392s
#2070 + i5 7500   = 0.485s