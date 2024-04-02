import pandas as pd

# 데이터셋 로드
data = pd.read_csv('data.csv')

# 1. 데이터셋을 불러와서 처음 5개의 행을 출력하세요.
print(data.head())

# 2. '카테고리' 별로 몇 개의 상품이 있는지 각각 세어 출력하세요.
print(data['카테고리'].value_counts())

# 3. 모든 상품의 평균 가격을 계산하세요.
print(data['가격'].mean())

# 4. '판매수량'이 가장 높은 상위 10개 상품을 출력하세요.
print(data.sort_values(by='판매수량', ascending=False).head(10))

# 5. 각 '카테고리'별 평균 판매수량을 계산하세요.
print(data.groupby('카테고리')['판매수량'].mean())

# 6. '판매날짜'를 기준으로 데이터를 정렬하세요(오래된 순).
data_sorted = data.sort_values(by='판매날짜')
print(data_sorted)

# 7. 각 '카테고리'별로 최고 가격을 가진 상품의 이름을 출력하세요.
idx = data.groupby('카테고리')['가격'].idxmax()
print(data.loc[idx, ['카테고리', '상품명']])

# 8. 모든 상품의 총 판매액(가격 * 판매수량)을 계산하세요.
print((data['가격'] * data['판매수량']).sum())

# 9. 각 '카테고리'별 총 판매액을 계산하세요.
data['판매액'] = data['가격'] * data['판매수량']
print(data.groupby('카테고리')['판매액'].sum())

# 10. 각 '카테고리'별 평균 판매액을 계산하고, 평균 판매액이 가장 높은 카테고리를 출력하세요.
avg_sales = data.groupby('카테고리')['판매액'].mean()
print(avg_sales)
print(avg_sales.idxmax())

# 11. 각 상품별로 '판매액'을 새로운 열로 추가하세요.
# 이미 위에서 추가함.

# 12. 판매 데이터 중에서 '판매수량' 상위 25%에 해당하는 상품들만 선택하여, 그 상품들의 평균 '가격'을 계산하세요.
top_25_percent_sales = data[data['판매수량'] > data['판매수량'].quantile(0.75)]
print(top_25_percent_sales['가격'].mean())

# 13. '판매날짜'를 datetime 타입으로 변환하고, 연도별 총 판매수량을 계산하세요.
data['판매날짜'] = pd.to_datetime(data['판매날짜'])
print(data.groupby(data['판매날짜'].dt.year)['판매수량'].sum())

# 14. 각 카테고리 내에서 '가격' 상위 10%에 해당하는 상품들의 목록을 출력하세요.
top_10_percent_prices = data.groupby('카테고리').apply(lambda x: x[x['가격'] > x['가격'].quantile(0.9)])
print(top_10_percent_prices)


# 15. '판매날짜'를 기준으로 각 달의 총 판매액을 계산하고, 판매액이 가장 높은 달을 출력하세요.
data['월'] = data['판매날짜'].dt.month
monthly_sales = data.groupby('월')['판매액'].sum()
print(monthly_sales)
print(monthly_sales.idxmax(), '월')
