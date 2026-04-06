from bdb import GENERATOR_AND_COROUTINE_FLAGS


temps = [18,22,35,28,41,30]
for temp in temps:
    if temp >= 35:
        print(f'「猛暑日（{temp}度）が検出されました」')
        break
    print(f'「{temp}度：問題なし」')

grades = ['A', 'C', 'B', 'F', 'A', 'D', 'B']
for grade in grades:
    if grade == 'F':
        print('不合格をスキップ')
        continue
    print(f'「合格：{grade}」')
    