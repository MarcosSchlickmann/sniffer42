from collections import defaultdict
import pyshark
import sys
def liveCapture(ips):
	filtro = []
	for ip in ips:
		filtro.append('ip.addr == ' + ip)
	capture = pyshark.LiveCapture(interface='eno1', display_filter=" or ".join(filtro))
	return capture


def extrairAtributos(pacote):
	atr = defaultdict(lambda: "Nenhum")
	atr["number"] = pacote.number
	if hasattr(pacote, "ip"):
		atr["ipDest"] = pacote.ip.dst
		atr["ipSource"] = pacote.ip.src
	if hasattr(pacote, "tcp"):
		atr["portaDest"] = pacote.tcp.dstport
		atr["portaSource"] = pacote.tcp.srcport
	if hasattr(pacote, "udp"):
		atr["portaDest"] = pacote.udp.dstport
		atr["portaSource"] = pacote.udp.srcport

	atr["protocolo"] = pacote.layers[-1].layer_name
	return(atr)

def printarPacote(pacote):
	atr = extrairAtributos(pacote)

	print("Numero:", atr["number"], "Origem:", atr["ipSource"])
	print("Destino:", atr["ipDest"], "Protocolo", atr["protocolo"])
	print("Porta origem:", atr["portaSource"], "Porta destino:", atr["portaDest"])
	print()



	# print(dir(pacote.udp))

def main(args):
	capture = liveCapture(args[1:])
	for pacote in capture.sniff_continuously():
		printarPacote(pacote)

if __name__ == '__main__':
	main(sys.argv)