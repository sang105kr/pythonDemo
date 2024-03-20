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

def dupchk_word_in_dictionary(dic,word):
  '''
    딕셔너리에 단어 중복 체크하는 함수
    중복이면 DictionaryException 예외 발생
  '''
  if word not in dic:
    return True
  else :
    raise DictionaryException(f'단어 {word} 는 이미 등록되었습니다!')

def exist_word_in_dictionary(dic,word):
  '''
    딕셔너리에 단어가 존재하는지 체크하는 함수
    존재하면 True 그렇지 않으면 DictionaryException 예외 발생
  '''
  if word in dic:
    return True
  else :
    raise DictionaryException(f'{word} 단어를 찾을 수 없습니다!')



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
            # 체크 2) 단어 중복 체크
            dupchk_word_in_dictionary(dictionary,word)
          except DictionaryException as e:
            print(e)
          else:
            meaning = input('의미입력 > ')
            dictionary[word] = meaning
            print(f'{word} 단어를 등록하였습니다!')
            break;
      case '2' :  # 검색
        while True:
          try:
            # 단어입력
            word = input('단어입력 > ').lower()
            # 단어 존재여부 체크
            exist_word_in_dictionary(dictionary, word)
          except DictionaryException as e:
            print(e)
          else:
            print(f'{word} : {dictionary[word]}')
            break;
      case '3' :  # 수정
        while True:
          try:
            # 단어입력
            word = input('단어입력 > ').lower()
            # 단어 존재여부 체크
            exist_word_in_dictionary(dictionary, word)
          except DictionaryException as e:
            print(e)
          else:
            meaning = input('의미입력 > ')
            dictionary[word] = meaning
            print(f'{word} 단어를 {meaning}로 수정하였습니다.')
            break;
      case '4' :  # 삭제
        while True:
          try:
            # 단어입력
            word = input('단어입력 > ').lower()
            # 단어 존재여부 체크
            exist_word_in_dictionary(dictionary, word)
          except DictionaryException as e:
            print(e)
          else:
            if input('삭제하시겠습니까?(Y/y)').lower() == 'y' :
              del dictionary[word]
              print(f'{word} 단어를 삭제하였습니다.')
              break;
      case '5' :  # 목록
        if not dictionary :
          print('등록된 단어가 없습니다.')
          continue

        while True :
          print('1.오름차순 2.내림차순 3.상위메뉴' )
          submenu = input('선택 >> ')
          match submenu :
            case '1' : # 오름차순
              sorted_dict = dict(sorted(dictionary.items()))
              for key in sorted_dict.keys() :
                print(f'{key}:{sorted_dict[key]}')
            case '2' : # 내림차순
              sorted_dict = dict(sorted(dictionary.items(),reverse=True))
              for key in sorted_dict.keys():
                print(f'{key}:{sorted_dict[key]}')
            case '3' | _ :
                break
      case '6' :  # 통계
        print(f'1.저장된 단어 갯수 : {len(dictionary)}')
        #longest_word = max(dictionary.keys(), key=lambda k: len(k))
        longest_word = max(dictionary.keys(), key=len)
        print(f'2.단어의문자수가 가장 많은 단어 : {longest_word}')
        sorted_words = sorted(dictionary.keys(), key=len, reverse=True)
        print(f'3.단어 글자수 내림차순 출력(단어만) : ')
        for word in sorted_words:
          print(word)
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


