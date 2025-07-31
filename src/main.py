from libtcpudp.protocolos.servidores import ServidorTCP
import psutil

# 1 - Quantidade de processadores
cpus_fisicas = psutil.cpu_count(logical = False)
cpus_logicas = psutil.cpu_count(logical = True)
threads_por_nucleo_fisico = cpus_logicas / cpus_fisicas
print(cpus_fisicas, cpus_logicas, threads_por_nucleo_fisico)

# 2 - Memória RAM livre
tupla_da_ram = psutil.virtual_memory()
memoria_ram_imediata = tupla_da_ram[1]
memoria_ram_alocada_e_nao_usada = tupla_da_ram[4]
print(tupla_da_ram, memoria_ram_imediata, memoria_ram_alocada_e_nao_usada)