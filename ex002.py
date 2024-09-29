red = '\033[091m'
reset = '\033[0m'
green = '\033[0;32m'
blue = '\033[0;34m'


nome = input('Digite seu nome:')
while True:
    sexo = input('Qual é seu genero?(M/F ou Masculino e Feminino)').strip().lower()
    if sexo in ['M','m','Masculino', 'homem', 'Homem', 'masculino']:
        sexo = 'M'
        break
    elif sexo in ['f','F', 'Mulher', 'mulher', 'Feminino', 'feminino']:
        sexo= 'F'
        break
    else:
        print(f'{red}Dados invalidos{reset}, digite novamente seu genero!!!')


peso = float(input('Digite seu peso em (KG):'))
altura = float(input('Digite sua Altura em (M):'))
idade = int(input('Qual é sua idade?'))

while True:
    print('Qual é seu objetivo?\n ',
          f'{red}1.{reset}Ganhar Peso\n ',
          f'{red}2.{reset}Perder Peso\n',
          f'{red}3.{reset}Manter Peso\n')
    objetivo = input('Digite o seu objetivo:').strip().lower()
    if objetivo in['ganhar', '1', 'ganhar peso']:
        calorias = 500
        break
    elif objetivo in ['perder','perder peso', '2']:
        calorias = -500
        break
    elif objetivo in ['3','manter peso','manter']:
        calorias = 0
        break
    else:
        print(f'{red}Opçao invalida, tente novamente!!!{reset}')




if sexo == 'M':
    tmb = 66 + (6.23 * peso) + (12.7 * (altura * 100)) - (6.8*idade)
else:
    tmb = 655 + (4.35 * peso) + (9.6 * (altura * 100)) - (4.7 * idade)


print('Qual é seu nivel de atividade fisica?\n',
      f' {red}1.{reset}Sedentario\n '
      f'{red}2.{reset}Leve \n '
      f'{red}3.{reset}Moderado\n'
      f' {red}4.{reset}Intenso')
nvt = input(f'Digite o numero correspondente ao seu nivel de {green}atividade fisica{reset}:')

if nvt == '1':
    calorias += tmb * 1.2
elif nvt == '2':
    calorias += tmb * 1.375
elif nvt == '3':
    calorias += tmb * 1.55
elif nvt == '4':
    calorias += tmb * 1.725
else:
    calorias += tmb * 1.2


s = peso / (altura**2)

print(f'{green}Seja bem vindo{reset} {nome}')
print(f'Seu imc é de: {s:.2f}')
if s < 18.5:
    print(f'{red} CUIDADO!!!{reset} Voce esta Abaixo do peso!')
elif 18.5 <= s < 24.9:
    print(f'{green} Seu Peso esta Normal!{reset}')
elif 25 <= s < 29.9:
    print(f'{green} Voce esta com Sobre peso{reset}')
else:
    print(f'{red} CUIDADO!!!{reset} voce esta com OBESIDADE')

print(f"{blue}SEU OBJETIVO:{reset}")


if objetivo  in['ganhar','1','Ganhar peso']:
        print(f'\n Para {green}Ganhar Peso{reset} voce vai precisar consumir cerca de {green}{calorias:.2f}{reset} calorias por dia.')
elif objetivo in['perder','perder peso', '2']:
        print(f'\n Para {green}Perder Peso{reset}, voce deve consumir cerca de {green}{calorias:.2f}{reset} calorias por dia.')
elif objetivo in['3', 'manter peso', 'manter']:
        print(f'\n Para manter seu peso, voce deve consumir cerca de {green}{calorias:.2f}{reset} calorias por dia.')

print(f"{blue} SEU SONO E QUANTIDADE DE AGUA!!!{reset}")

agua = peso * 35
horas_sono = "7 a 8 Horas de sono"

print(f'A quantidade recomendada de Agua por dia é {green}{agua:.2f}{reset} ml.')
print(f'Voce deve dormir entre {green}{horas_sono}{reset} por noite')










