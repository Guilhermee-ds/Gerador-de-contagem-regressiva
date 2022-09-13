from threading import Timer
import time

def contagem(t):
    while t:
        minutos,segundos = divmod(t, 60)
        contagem  = '{:02d}:{:02d}'.format(minutos,segundos)
        print(contagem, end ="\r")
        time.sleep(1)
        t -=1

    print('Temporizador completo!')

t = input('Entre com o tempo em segundos:')
 
contagem(int(t))




#passo a passo  
# 1 = importei a biblioteca time  que com ela trabalhamos segundos , minutos e horas , dias , meses .
# 2 = defini uma função e nomeamos ela como contagem e fizemos isso para pegar o parâmetro que é (t)
# 3 = depois  demostramos que (t) é a quantidade de segundos
# 4 = 