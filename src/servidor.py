from libtcpudp.protocolos.servidores import ServidorTCP
import base64

servidor = ServidorTCP("ipv4", "127.0.0.1", 54545, 90, 2048)
servidor.aceitarConexao()
base64_recebido = servidor.receberBase64PorPartes()
print(base64.b64decode(base64_recebido))