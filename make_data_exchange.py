import requests
import json
from collections import OrderedDict


# API key
API_KEY = 'DBAH4dbneY14sHfaMcBHfx0eJ7AM8lkN'

# 요청 URL
URL = url = f' https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&searchdate=20180102&data=AP01'

# json 응답으로 변경
response = requests.get(URL).json()

# 응답 확인
print(json.dumps(response, ensure_ascii=False, indent="\t"))

# 파일 생성
file = OrderedDict()
save_dir = './make_exchange.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    
    for i in range(len(response)):
        # 랜덤한 데이터를 삽입
        file["model"] = "service.Exchange"
        file["pk"] = i+1
        file["fields"] = {
            "cur_unit": response[i]["cur_unit"],
            "cur_nm": response[i]["cur_nm"],
            "ttb": response[i]["ttb"],
            "tts": response[i]["tts"],
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != len(response)-1:
            f.write(',')
    f.write(']')
    f.close()


# with open('exchange_data.json', 'w', encoding="utf-8") as make_file:
#     json.dump(response, make_file ,ensure_ascii=False, indent="\t")


