# 8. Dados os pontos A, de coordenadas ﻿A parêntese esquerdo x com 1 subscrito vírgula y com 1 subscrito parêntese direito﻿ e B de coordenadas ﻿B parêntese esquerdo x com 2 subscrito vírgula y com 2 subscrito parêntese direito﻿, escreva um programa que determine a distância entre os dois pontos. Considere que: ﻿texto distancia fim do texto igual a raiz quadrada de parêntese esquerdo x com 2 subscrito menos x com 1 subscrito parêntese direito ao quadrado mais parêntese esquerdo y com 2 subscrito menos y com 1 subscrito parêntese direito ao quadrado fim da raiz﻿
x1 = float(input("Digite a coordenada x do ponto A: "))
y1 = float(input("Digite a coordenada y do ponto A: "))
x2 = float(input("Digite a coordenada x do ponto B: "))
y2 = float(input("Digite a coordenada y do ponto B: "))

distancia =  round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2), 2)

print("A distância entre os pontos A", x1, ",", y1, "e B", x2, "," , y2, "é:", distancia)
