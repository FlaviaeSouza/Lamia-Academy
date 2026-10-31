lockdown = True
grana = 30


#status = 'em casa' if lockdown else 'Uhuuuu' em casa se lockdown for true, caso contrario 'Uhuuuu'
status = 'em casa' if lockdown or grana <= 100 else 'uhuuuu'

print(status)


