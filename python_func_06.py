def suggest_clothes(temperture):
    if temperture < -50 or temperture > 50 :
        return False
    return True

def judge_temperture(temperture):
    if not suggest_clothes(temperture):
        print(f'エラー:正しい気温を入力してください')
        return
    if temperture >= 30:
        return '半袖・短パン'
    
    elif temperture >= 20:
        return '長袖'
    
    elif temperture >= 10:
        return 'ジャケット'
    
    else:
        return 'コート・マフラー'

print(judge_temperture(35))
print(judge_temperture(22))
print(judge_temperture(8))
print(judge_temperture(100)) 
