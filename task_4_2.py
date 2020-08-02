chisla = input('vvedite spisok chisel:')
spisokchisel = chisla.split(' ')
counter = 0
for i in spisokchisel:
    if int(i) % 2 == 0:
        counter += 1
print(*spisokchisel)
print('chetnih chisel v spiske:', counter)
