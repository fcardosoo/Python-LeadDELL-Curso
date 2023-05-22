"""
Para fazer a cerca, você usará estacas e arame farpado, da seguinte forma:

    A quantidade de arame farpado por segmento é igual ao tamanho de cada segmento;
    Uma estaca é colocada em cada ponto;
    Em cada segmento, as estacas são colocadas em um intervalo de cerca de 2 metros.

Lembre-se que o comprimento de um segmento s[i] entre os pontos (x[i], y[i]) e (x[i+1], y[i+1])
é dado pelo Teorema de Pitágoras, ou seja: s[i] = ((y[i+1]−y[i])^2+(x[i+1]−x[i])^2)^0.5

E o número de estacas pode ser obtido como a parte inteira de s[i] dividido por 2.

Agora, faça um programa para calcular, e imprimir, as seguintes informações:

    Duas listas: uma com a quantidade de arame usada por segmento, e outra com a quantidade de
    estacas por segmento (não contar as estacas dos extremos);
    O comprimento total de arame farpado utilizado;
    A quantidade total de estacas de madeira utilizada.
"""

terreno = [
    [42.7, 71.9],
    [38.9, 80.3],
    [56.3, 88.9],
    [70.7, 83.9],
    [74.5, 69.7],
    [47.9, 60.4],
    [36.8, 62.6],
    [56.8, 56.5],
]

perimetro = 0
estacas = 0


"""Oi Alan, não consegui evoluir neste exercício... como eu acesso o x1 e y1?
Tentei várias coisas, mas não descobri...
Se puder me ajudar... ao menos dar uma dica para eu poder concluir o exercício.
"""