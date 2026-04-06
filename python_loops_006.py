population =  {'東京': 1400, '大阪': 880, '名古屋': 230, '福岡': 160}
for city in population:
    number = population[city]
    print(f'{city}の人口は{number}です')
for city in population:
    number = population[city]
    if number >= 500:
        print(f'大都市：{city}({number}万人)')
