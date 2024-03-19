import json

data = {"name":"홍길동", "age":30}

#json 형식으로 파일에 저장하기
with open('data.json', mode='w',encoding='utf-8') as f :
  json.dump(data,f,ensure_ascii=False)

#json 파일을 읽어와 파이썬 객체로 변환하기
with open('data.json', mode='r', encoding='utf-8') as f:
  data_loaded = json.load(f)

print(type(data_loaded))
print(data_loaded)

#키를 통해 값읽기
print(data_loaded['name'])
#키를 리스트로 가져오기
print(data_loaded.keys())
#값을 리스트로가져오기
print(data_loaded.values())
#entry로 가져오기
print(data_loaded.items())
