import json

class DictionaryException(Exception) :
  def __init__(self,errmsg):
    self.errmsg = errmsg

  def __str__(self) :
    return self.errmsg

def dictionary_close(data) :
  '''
    json 형식으로 파일에 저장하기
  '''
  with open('dictionary.json', mode='w',encoding='utf-8') as f :
    json.dump(data,f,ensure_ascii=False)

def dectionary_open() :
  '''
    json 파일을 읽어와 파이썬 객체로 변환하기
  '''
  try :
    with open('dictionary.json', mode='r', encoding='utf-8') as f:
      return json.load(f)
  except FileNotFoundError:
      return {}

def exist_word_in_dictionary(dic,word):
  '''
    딕셔너리에 단어가 존재하는지 체크하는 함수
  '''
  if word not in dic:
    return True
  else :
    raise DictionaryException(f'단어 {word} 는 이미 등록되었습니다!')

MAX_WORD = 5  # 저장할 단어 최대 갯수
dictionary = dectionary_open()  # 사전에서 단어정보 가져오기

stop = False
while not stop :
  try:
    print('1.저장 2.검색 3.수정 4.삭제 5.목록 6.통계 7.종료 8.초기화')
    menu = input('선택 >> ')
    match menu:
      case '1' :  # 저장
        # 체크 1) 최대 단어 갯수
        if MAX_WORD == len(dictionary) :
          print(f'최대 저장용량{MAX_WORD} 초과')
          continue

        while True:
          try:
            # 단어입력
            word = input('단어입력 > ').lower()
            # 체크 2) 단어 유무 체크
            exist_word_in_dictionary(dictionary,word)
          except DictionaryException as e:
            print(e)
          else:
            meaning = input('의미입력 > ')
            dictionary[word] = meaning
            break;
      case '2' :  # 검색
        pass
      case '3' :  # 수정
        pass
      case '4' :  # 삭제
        pass
      case '5' :  # 목록
        if not dictionary :
          print('등록된 단어가 없습니다.')
        for key in dictionary.keys() :
          print(f'{key}:{dictionary[key]}')
      case '6' :  # 통계
        pass
      case '7' :  # 종료
        dictionary_close(dictionary)
        stop = True
      case '8' :  # 초기화
        dictionary.clear()
        dictionary_close(dictionary)
      case _ :
        print('1~7 사이의 메뉴를 선택하세요')

  except DictionaryException as e:
    print(e)


