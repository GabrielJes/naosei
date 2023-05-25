import subprocess
import sys
from time import sleep
import os

# checando todos os processos em andamento durante (5) minutos

def CreateData(): # Cria o arquivo onde salva as informacoes
    data = os.system("mkdir data-diagnostic && cd data-diagnostic && touch data.txt")
    check = int(data)
    if check !=0:
        data = os.system("rm -rf data-diagnostic")
        sleep(1)
        data = subprocess.run(["mkdir data-diagnostic && cd data-diagnostic && touch data.txt"],shell=True,capture_output=True)
    checkdata = subprocess.check_output(["ls data-diagnostic"],shell=True).decode('UTF-8')
    checkdata = len(checkdata)
    if checkdata == 9:
        print('Arquivo criado com sucesso!')
        print()
    else:
        print('Nao foi possivel criar o arquivo! ')
        exit(1)
    return None

def MemoryTotal(): # verifica o tamanho da memoria do computador 
    memory = subprocess.run('free -m | grep Mem',capture_output=True, shell=True)
    memory = str(memory)
    memory = int(memory.split()[7])
    print(f'Tamanho da memoria em MB : {memory}') # remover esse print
    return memory


def cpuThreads(): # Verifica o numero de threads e converte em float, desse jeito conseguimos saber qual "maximo de cpu podemos atingir" 
    cpuThreadsNumber = os.popen('grep -c processor /proc/cpuinfo').read()
    cpuThreadsNumber = float(cpuThreadsNumber)
    print(f'VALOR MAXIMO DE CONSUMO PARA ESSE PROCESSADOR : {cpuThreadsNumber}') # retirar esse print 
    return cpuThreadsNumber

def cpudata(numberthreads):
    numberthreads = float(4.0) # REMOVER 
    time = os.popen('uptime -p').read()
    loadAvarage1min = os.popen('uptime').read().rstrip()[44:48]
    loadAvarage5min = os.popen('uptime').read().rstrip()[50:54]
    loadAvarage15min = os.popen('uptime').read().split()[9]
    countofquit = 0
    sleep(1)
    if float(loadAvarage1min) >= numberthreads:
        countofquit += 1
    elif float(loadAvarage5min) >= numberthreads:
        countofquit += 1
    elif float(loadAvarage15min) >= numberthreads:
        countofquit += 1
    else :
        countofquit = 0
    if countofquit == 0 :
        return loadAvarage1min,loadAvarage5min,loadAvarage15min
    else:
        print('lasco')  # REMOVER Print   


def checkMedia():
    numberthreads = 4.0
    for i in range(100):
        onemin,fivemin,ftmin = cpudata(numberthreads)
        onemin = float(onemin)
        fivemin = float(fivemin)
        ftmin = float(ftmin)
        print(onemin,fivemin,ftmin)
        return onemin,fivemin,ftmin

count = 0
while count <= 20:
    a,b,c = checkMedia()
    count += 1


        

