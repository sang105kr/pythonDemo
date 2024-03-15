# 매개변수로 두 개의 리스트를 받아, 첫 번째 매개변수로 받은 리스트에 두 번쨰 리스트의
#   데이터를 삭제한 리스트를 리턴하는 함수를 만드시오. 단, 첫 번째 매개변수로 들어온
#   리스트가 반드시 두 번째 매개변수로 들어온 리스트보다 데이터의 수가 많다고 가정한다.
#   두 매개변수 : [1, 3, 5, 7, 9], [1, 5]   => 결과 : [3, 7, 9]

def remove_elements(list1, list2) :

  #case1) for 반복문과 not in 연산자 사용
  # result = []
  # for ele1 in list1:
  #   if ele1 not in list2 :
  #     result.append(ele1)

  #case2) 리스트 컴프리헨션 사용
  result = [ ele1 for ele1 in list1 if ele1 not in list2 ]
  return result


print(remove_elements([1,3,5,7,9],[1,5]))

