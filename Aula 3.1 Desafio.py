'''

Oficina Aula 3.1

Chegou o momento de você colocar em prática tudo o que aprendeu sobre dividir e reutilizar códigos. Para isso, imagine um programa de agenda, que utiliza uma lista para armazenar os eventos inseridos por um usuário, cuja uma de suas finalidades é imprimir uma lista dos eventos que acontecerão entre duas datas especificadas também pelo usuário. Os eventos são representados por tuplas, em que:

    O primeiro elemento é uma tupla de três números: ano, mês e dia;
    O segundo elemento é uma tupla de dois números: hora e minuto e;
    O terceiro elemento é uma string que descreve brevemente o evento.

Um exemplo dos dados desta agenda é representado pelo trecho abaixo:

agenda = [
      ((2020, 1, 13), (11, 50), 'Renovar identidade'),
      ((2020, 1, 15), (16, 30), 'Fazer compras'),
      ((2020, 1, 25), (8, 45), 'Autenticar documentos'),
      ((2020, 2, 29), (14, 15), 'Prestar concurso'),
      ((2020, 3, 15), (17, 50), 'Buscar bolo pro aniversário da vovó'),
      ((2020, 3, 17), (13, 20), 'Consulta de revisão com dentista'),
]

Você deve completar a função imprimir_eventos, rascunhada abaixo, que recebe como parâmetros uma lista de eventos neste formato e dois parâmetros adicionais, de_data e ate_data, que dão as datas inicial e final:

def imprimir_eventos(eventos, de_data=(1, 1, 1), ate_data=(9999, 12, 31)):

Os valores padrão das datas indicam que o comportamento padrão é imprimir todos os eventos. É possível restringir a data inicial, a data final, ou ambas, usando estes parâmetros. Por exemplo, o resultado da chamada imprimir_eventos(agenda, (2020, 1, 20)) é a impressão do seguinte trecho:

25/jan/2020 - 08:45: Autenticar documentos
29/fev/2020 - 14:15: Prestar concurso
15/mar/2020 - 17:50: Buscar bolo pro aniversário da vovó
17/mar/2020 - 13:20: Consulta de revisão com dentista

e o resultado da chamada imprimir_eventos(agenda, ate_data=(2020, 3, 15)) é a impressão de:

13/jan/2020 - 11:50: Renovar identidade
15/jan/2020 - 16:30: Fazer compras
25/jan/2020 - 08:45: Autenticar documentos
29/fev/2020 - 14:15: Prestar concurso
15/mar/2020 - 17:50: Buscar bolo pro aniversário da vovó

Para te auxiliar na conclusão deste problema, você deve criar também duas funções adicionais:

    formatar_data, que recebe uma tupla de números na forma (ano, mes, dia) e retorna uma string na forma dd/mes/aaaa, substituindo o mês pelas três letras iniciais do nome do mês, por extenso. Por exemplo, formatar_data((2020, 1, 3)) deve retornar "03/jan/2020".
    formatar_hora, que recebe uma tupla de números na forma (hora, minuto) e retorna uma string na forma hh:mm em formato de 24h. Por exemplo, formatar_hora((16, 30)) deve retornar "16:30"

Então agora é o momento de você unir todas essas informações ao que você já sabe sobre funções para completar o programa de acordo com as orientações passadas. Boa prática!



'''