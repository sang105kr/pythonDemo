# 3. 매개변수로 두 개의 리스트를 받아, 두 개의 리스트에 저장된 모든 데이터의 평균을 리턴하는
#    함수를 작성하시오.


def average_of_two_lists(list1, list2):

  combind_list = list1 + list2
  average = sum(combind_list) / len(combind_list)

  return average

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
result = average_of_two_lists(list1, list2)
print(result)

