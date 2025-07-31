from libtcpudp.protocolos.servidores import ServidorTCP
import psutil

# 1 - Quantidade de processadores
cpus_fisicas = psutil.cpu_count(logical = False)
cpus_logicas = psutil.cpu_count(logical = True)
threads_por_nucleo_fisico = cpus_logicas / cpus_fisicas
print(cpus_fisicas, cpus_logicas, threads_por_nucleo_fisico)