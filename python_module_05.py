from datetime import date, datetime, timedelta

today = date.today()
print(f'今日：{today.strftime('%Y年%m月%d日')}')

now = datetime.now()
print(f'実行時刻：{now.strftime('%Y年%m月%d日 %H時%M分')}')

print(today + timedelta(days=30))

birthday = date(1990, 3, 23)
print((today - birthday).days)