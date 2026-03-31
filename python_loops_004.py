book =  {'title': '吾輩は猫である',
'author': '夏目漱石',
'year': 1905,
'pages': 648}
print(book['title'])
print(book['author'])
print(f'{book['title']} ( {book['author']} 著、 {book['year']} 年)')
product =  {'name': 'ノート PC',
'price': 89800,
'stock': 15}
if  product['stock'] >= 10:
    print(f'在庫あり（ {product['stock']} 個）')
else:
    print('頑張りましょう')
