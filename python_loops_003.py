from functools import total_ordering


menu = ['ラーメン', 'カレー', 'パスタ', '寿司', '天ぷら']
for food in menu:
    print('「本日のメニュー：' + food + '」')
for i in range(1,6):
    print(i)
prices = [980, 1200, 750, 1500, 880]
total_price = 0
for price in prices:
    total_price = total_price + price
print(f'合計金額：{total_price}円')
