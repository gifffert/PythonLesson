zoo_pets = ['lion', 'elephant', 'monkey', 'slunk', 'horse']
count = 0
for animal in zoo_pets:
    print('Сейчас', animal)
    count += len(animal)
    pass
print('Всего букв', count)