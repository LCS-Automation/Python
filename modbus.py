
#### LCS Automação Industrial ####

#Importa a biblioteca Modbus Client para o programa
from pyModbusTCP.client import ModbusClient

#Define a biblioteca de funções (semelhante a FB)
def read_modbus(IP):
    #Configura a comunicação Modbus Cliente com o CLP
    comm_config=ModbusClient(host= IP, port = 502, unit_id= 1, timeout = 500.0 , auto_open = True, auto_close = True)

    #Executa a leitura de registros do CLP
    regs_read=comm_config.read_input_registers(0,10)

    if regs_read: 
        #Faz a divisão por 100 dos primeiros 5 valores coletados do CLP, para gerar numero real   
        i=0;
        while i<6:
            regs_read[i]=regs_read[i]/100;
            i+=1 #i=i+1   
    else:
        regs_read="Erro na Leitura"
    return regs_read
    

    #Define a biblioteca de funções (semelhante a FB)
def write_modbus(IP, Vars_escrita):
    #Configura a comunicação Modbus Cliente com o CLP
    comm_config=ModbusClient(host= IP, port = 502, unit_id= 1, timeout = 500.0 , auto_open = True, auto_close = True)

    #Executa a escrita de registros do CLP (Vars_escrita vem de uma variavel externa do bloco)
    regs_write=comm_config.write_multiple_registers(0,Vars_escrita)

    if regs_write:   
        regs_write="Escrita realizada com sucesso"
    else:
        regs_write="Erro na Escrita"
    return regs_write
    
            
  
                

            
