# coding: utf-8
"""
爬取估计
"""
"""
class dataVo(BaseModel):
    image: str = None
    scene: str = None
    pdf: str = None
    pdf_page: str = '1'
    recog: str = None
    rotate_upright: bool = False
    det: bool = True
    threshold: int = 300
    minLineLength: float = 0.75
    maxLineGap: int = 30
    withLines: bool = True
"""

"""
class OcrVo(BaseModel):
    appId: str = None
    trCode: str = None
    trVersion: str = None
    timestamp: str = None
    requestId: str = None
    responseId: str = None
    data: dataVo = None
"""
import base64, os, uuid, time

def convert_b64(file):
    if os.path.isfile(file):
        with open(file, 'rb') as fh:
            x = base64.b64encode(fh.read())
            return x.decode('ascii').replace('\n', '')
    else:
        return None


data = {
    "appId": str(uuid.uuid4()),
    "trCode": "200",
    "trVersion": "3.1",
    "timestamp": str(int(time.time())),
    "requestId": str(uuid.uuid4()),
    "responseId": "456",
    "data": {
        "image": "",
        "scene": 'table_print',
        "pdf":"",
        "pdf_page": '1',
        "recog":"",
        "rotate_upright":True,
        "det": True,
        'threshold':300,
        'minLineLength': 0.75,
        "maxLineGap":30,
        "withLines": True
    }

}
# http://172.27.96.126:18506/lab/ocr/predict/table
tableurl="http://172.27.231.43:18506/lab/ocr/predict/table"
# tableurl="http://localhost:8602/lab/ocr/predict/table"
tableurl="http://172.27.231.43:18602/lab/ocr/predict/table"
ff = "aaa.jpg"

res = convert_b64(ff)
data["data"].update({
    "image": res
})
import requests
res = requests.post(url=tableurl, json=data)
aa = res.json()
print(aa)
