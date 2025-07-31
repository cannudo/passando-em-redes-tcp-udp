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

# 3 - Espaço livre em disco
particoes_de_disco = psutil.disk_partitions(all = False)
memoria_livre_de_cada_particao = list()

for particao in particoes_de_disco:
    try:
        memoria_da_particao = psutil.disk_usage(particao.mountpoint)
        memoria_livre_de_cada_particao.append({
            "particao": particao.mountpoint,
            "livre": memoria_da_particao.free
        })
    except Exception as e:
        print(f"Não foi possível obter as informações sobre o ponto de montagem {particao.mountpoint}: {e}")
print(memoria_livre_de_cada_particao)