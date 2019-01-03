import requests
import json
import base64

def get_ile_content(filePath):
	""" 读取图片base64 """
	with open(filePath, 'rb') as fp:
		return base64.b64encode(fp.read())

def get_access_token():
	# API_Key,Secret_Key 需要在 https://console.bce.baidu.com/ai/?fromai=1#/ai/ocr/app/list 创建应用才能获得
	API_Key = 'DVUu4BCefTUBTGiRaLqNLIl0'
	Secret_Key = '3mCiWIofCBiliq3sN4bFTrTeOb9kE607'
	r = requests.post('https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+API_Key+'&client_secret='+Secret_Key)
	j = json.loads(r.text)
	return j.get('access_token')

def recognise_handwriting_pic(access_token,image_path):
	image = get_file_content(image_path)
	r = requests.post(
		url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting?access_token='+access_token,
		headers={"Content-Type":"application/x-www-form-urlencoded"},
		data = {'image':image})
	j = json.loads(r.text)
	words_result = j.get('words_result')
	for i in words_result:
		print(i.get('words'))

access_token = get_access_token()  # 获取一次保存下来就够了，一般1个月有效期
recognise_handwriting_pic(access_token,image_path='/Users/jacklee/Desktop/5.png')
