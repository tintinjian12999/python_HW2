import os
import random
path = os.getcwd()
path_read_pikachu = path + r'\pikachu.txt'
path_read_eevee = path + r'\eevee.txt'
write_file_name = path + r'\pokedex_training_training.txt'
write_file = open(write_file_name,'w')
file_pikachu = open(path_read_pikachu,'r',encoding="utf-8")
file_eevee = open(path_read_eevee,'r',encoding="utf-8")
pokemon = []
for i in file_pikachu:
    i = i.strip('\n')
    data_pikachu = i.split('/')
    pokemon.append((data_pikachu[6],1))
for i in file_eevee:
    i = i.strip('\n')
    data_eevee = i.split('/')
    pokemon.append((data_eevee[6],0))

random.shuffle(pokemon)
for i in pokemon:
    print(i[0] + ', ' + str(i[1]))
    write_file.write(i[0] + ', ' + str(i[1])+'\n')

