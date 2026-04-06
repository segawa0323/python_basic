age = 24
# age を用いて「私は24歳です」と出力してください
print('私は' + str(age) + '歳です')

count = '5'

# count に 1 を足した値を出力してください
print(int(count) + 1)
# 9 を 2 で割った値を出力してください
print(9 / 2)
# 7 に 5 を掛けた値を出力してください
print(7 * 5)
# 5 を 2 で割った時の余りを出力してください
print(5 % 2)
# 変数 name に文字列「 ATラボ 」を代入してください
name = 'ATラボ'
# 変数 name の値を出力してください
print(name)
# 変数 number に数値の 7 を代入してください
number = 7
# 変数 number の値を出力してください
print(number)

apple_price = 200
apple_count = 8

# apple_price と apple_count を掛けた結果を、変数 total_price に代入してください
total_price = apple_price * apple_count
# total_price の値を出力してください
print(total_price)

money = 2000
print(money)

# 変数 money に 5000 を足して、変数 money を上書きしてください
money = money + 5000
# 変数 money の値を出力してください
print(money)
# my_name という変数に「 ATラボ 」という文字列を代入してください
my_name ='ATラボ'
# my_name を用いて、「私はATラボです」となるように変数と文字列を連結して出力してください
print('私は' + my_name + 'です')

#for文練習　リスト・辞書
prefectures =  ['北海道', '宮城', '東京', '愛知', '大阪', '福岡', '沖縄']
print(prefectures[0])
print(prefectures[2])
print(prefectures[4])

print(f'3番目の都県は{prefectures[3]}です' )

scores =  [72, 88, 95, 61, 79]
print(scores[-1])

book =  {
    'title': '吾輩は猫である', 
    'author': '夏目漱石', 
    'year': 1905, 
    'pages': 648
    }

print(book['title'])
print(book['author'])

print(f'{book["title"]}({book["author"]}、{book['year']}年)')

product =  {
    'name': 'ノート PC',
    'price': 89800, 
    'stock': 15
    }

if product['stock'] >= 10 :
    print(f'在庫あり( {product['stock']} 個) ')
    
else :
    print('頑張りましょう')