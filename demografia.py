import termcolor
from termcolor import colored, cprint
print(colored('VAMOS DESCOBRIR O VALOR DE Tn, Tm, Cv, Dd', 'yellow'))

nascimentos=input(colored('nascimentos: ', 'cyan'))
mortes=input(colored('mortes: ', 'cyan'))
populacao=input(colored('população: ', 'cyan'))
area=input(colored('área: ', 'cyan'))

nascimentos=float(nascimentos)
mortes=float(mortes)
populacao=float(populacao)
area=float(area)

Tn = nascimentos *1000/populacao
Tm = mortes *1000/ populacao
Cv = Tn - Tm
Dd = populacao/area

tn1='Tn:%.2f' % Tn
tm1='Tm:%.2f' % Tm
cv1='Cv:%.2f' %  Cv
dd1='Dd:%.2f' % Dd

arquivo = open('demografia.txt','a')
arquivo.write(str(tn1) + '\n')
arquivo.write(str(tm1) + '\n')
arquivo.write(str(cv1) + '\n')
arquivo.write(str(dd1) + '\n')
arquivo.close()