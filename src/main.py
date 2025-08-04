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
informacoes_das_particoes = []
particoes = psutil.disk_partitions(all=False)
for particao in particoes:
    try:
        uso = psutil.disk_usage(particao.mountpoint)
        informacoes_das_particoes.append({
            "device": particao.device,
            "mountpoint": particao.mountpoint,
            "fstype": particao.fstype,
            "total_bytes": uso.total,
            "used_bytes": uso.used,
            "free_bytes": uso.free,
            "percent_used": uso.percent
        })
    except Exception as e:
        print(f"Não foi possível obter o uso do disco para {partition.mountpoint}: {e}")

informacoes_do_sistema = {}
informacoes_do_sistema["processadores"] = {
    "logicos": cpus_logicas,
    "fisicos": cpus_fisicas
}
informacoes_do_sistema["ram"] = {
    "imediata": memoria_ram_imediata,
    "alocada_e_nao_usada": memoria_ram_alocada_e_nao_usada
}
informacoes_do_sistema["particoes"] = informacoes_das_particoes