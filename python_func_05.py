def clac_bmi(height,weight):
    bmi = weight / ((height/100) * (height/100))
    return bmi
bmi = clac_bmi(170,65)
print(f'「BMI：{bmi:.1f}')

def bmi_judge(bmi):
    if bmi < 18.5:
        return '低体重'
    elif bmi < 25:
        return '普通体重'
    elif bmi < 30:
        return '過体重'
    else:
        return '肥満'

print(bmi_judge(bmi))