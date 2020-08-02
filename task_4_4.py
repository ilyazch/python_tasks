chisla=input('vvedite chisla')
spisokchisel=chisla.split(' ')
stariyspisok=spisokchisel.copy()
element=spisokchisel.pop(0)
spisokchisel.append(element)
print(*stariyspisok,'->',*spisokchisel)

