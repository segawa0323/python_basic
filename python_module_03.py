import random

print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))

candidates = ['田中', '鈴木', '山田', '佐藤', '伊藤']
print(f'今月の当番：{random.choice(candidates)}')

numbers = list(range(1, 11))
random.shuffle(numbers)
print(numbers)

lottery = random.sample(range(1, 50), 6)
print(sorted(lottery))