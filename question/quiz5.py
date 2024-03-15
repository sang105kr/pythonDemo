# 자바스크립트의 배열 고차함수 VS 파이썬
# 1.forEach
# const array = [1,2,3]
# array.forEach(item=>console.log(item))

array =  [1,2,3]
#case1)
for item in array:
  print(item)
#case2) 리스트 컴프리핸션
[print(item) for item in array]


#2.map
# const array =[1,2,3]
# const result = array.map(item => item * item )
# console.log(result)   // [1,4,9]
array = [1,2,3]

def f(item):
  return item * item
# list(map( f , array )
result = list(map(lambda item : item * item ,array))
print(result)  # [1,4,9]

#3.filter
# const array = [1,2,3]
# result = array.filter(item=> item % 2 != 0)
# console.log(result) [1,3]

array = [1,2,3]
result = list(filter(lambda item : item % 2 !=0  ,array))
print(result)  # [1,3]

# 4.reduce
# const array = [1,2,3]
# const result = array.reduce((acc,curr)=> acc + curr), 0)
# console.log(result)

from functools import reduce
array = [1,2,3]
sum = reduce(lambda acc,curr : acc + curr, array, 0)
print(f'합={sum}')
