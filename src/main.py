from libtcpudp.protocolos.servidores import ServidorTCP
import random

eu_vou_passar_em_redes = random.choice([True, False])

print("Olá, mundo" if eu_vou_passar_em_redes else "Que merda, hein?")