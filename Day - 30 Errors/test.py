height = float(input("height"))
weight = int(input('Weight'))

bmi = weight / height ** 2



if weight > 3:
    raise ValueError('Your Height is to tall, human cant be that call')
print(bmi)