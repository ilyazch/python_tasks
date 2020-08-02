num=int(input('vvedi chislo'))
list_f=[num,num]
for i in range(15):
    list_f.append(list_f[i]+list_f[i+1])
print(*list_f)