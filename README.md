# sniffer42

Analisador de tráfego de rede.

## Instalação

São necessários o Python 3 e o pacote ```pyshark```.
Clone o repositório e entre no diretório resultante:

~~~
git clone https://github.com/MarcosSchlickmann/sniffer42.git
cd sniffer42
~~~

Pode-se instalar em um ```virtualenv```, ou especificar o interpretador do sistema, versão 3.
Escolha uma das seções abaixo, e siga apenas uma.

### Global (sistema)

Instalar o ```pyshark```:

~~~
pip3 install pyshark
~~~


### Virtualenv

Criar e ativar um ```virtualenv```:

~~~
virtualenv -p python3 venv 
source venv/bin/activate
~~~


Instalar o ```pyshark```:

~~~
pip install pyshark
~~~

## Utilização

Pode-se utilizar atributos para filtrar por IP:

**Filtrando IPs do DNS do IFC**

~~~
python3 sniffer42.py 191.52.54.4 191.52.52.6
~~~
