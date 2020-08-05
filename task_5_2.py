number = int(input('»> '))
sum = 0
product = 1
while number > 0:
    num = number % 10
    sum = sum + num
    product = product * num
    number = number // 10
print(f'Cумма: {sum}, произведение: {product}')
