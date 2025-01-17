from util import sendARequest
import time
import sys

arquito_de_entradas = sys.argv[1]

with open(arquito_de_entradas,'r') as file:
    line = file.readline()
    line = file.readline().replace("\n","")
    while line :
        line_content = line.split(';')
        # 0 - Nome
        # 1 - Genero
        # 2 - Estado
        # 3 - Municipio

        sendARequest(line_content[0], line_content[1],line_content[2],line_content[3])
        time.sleep(1)
        line = file.readline().replace("\n","")





