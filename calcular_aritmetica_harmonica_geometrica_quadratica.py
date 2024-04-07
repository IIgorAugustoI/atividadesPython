# 7 Faça um programa que leia 4 valores reais (﻿a vírgula b vírgula c texto  e  fim do texto d﻿) e determine:
# A média aritmética;
# A média harmônica (MH);
# A média geométrica (MG);
# A média quadrática (MQ).
a = float(input("Digite o valor de a: ")) 
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))

media_aritmetrica = round((a + b + c + d) / 4, 2)
media_harmonica = round(4 / ((1/a) + (1/b) + (1/c) + (1/d)), 2)
media_geometrica = round((a * b * c * d) ** (1/4),2)
media_quadratica = round((a**2 + b**2 + c**2 + d**2) ** (1/2), 2)

print("A média aritmétrica é de: ", media_aritmetrica)
print("A média harmônica é de: ", media_harmonica)
print("A média geométrica é de: ", media_geometrica)
print("A média quadrática é de: ", media_quadratica)
