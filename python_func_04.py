def calc_time(distance,speed=60):
    print(f'{distance}kmを{speed}km/hで走ると約{distance/speed:.1f}時間かかります')

calc_time(120)
calc_time(120,80)
calc_time(300)