lockdown = False 
grana = 30  

# Se 'lockdown' for True OU 'grana' for menor ou igual a 100, o 'status' será 'Em casa'.
# Caso contrário, o 'status' será 'Uhuuuu'.
status = 'Em casa' if lockdown or grana <= 100 else 'Uhuuuu'

print(status) 
