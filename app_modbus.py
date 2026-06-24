#### LCS Automação Industrial #### 
### Lucas P. de Sousa_03/06/2026 ###
### Aplicativo criado para fazer a leitura e escrita do CLP ###

# Importa as bibliotecas
from modbus import read_modbus, write_modbus
import time

#Define as variaveis de IP para configuração do bloco
IP_leitura="192.168.100.2"
IP_escrita="192.168.100.2"
#Define valores de escrita no CLP
valores_escrita=[75,20,30,40,50,60]


#Tenta execução do APP, se falha print msg de erro
try:
    while True:
        #Faz a chamada do bloco read_mosbus
        LEITURA=read_modbus(IP_leitura)
        print(LEITURA)
        #Faz a chamada do bloco write_mosbus
        ESCRITA=write_modbus(IP_escrita, valores_escrita)
        print(ESCRITA)
        #Temporizador de 1 segundo para proxima execução
        time.sleep(1)
except:
    print("Falha no APP")   
    

    