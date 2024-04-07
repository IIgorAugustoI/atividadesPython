# Declaração das variáveis
x1 = float(input("Digite a coordenada x do ponto A: "))
y1 = float(input("Digite a coordenada y do ponto A: "))
x2 = float(input("Digite a coordenada x do ponto B: "))
y2 = float(input("Digite a coordenada y do ponto B: "))

# Cálculo da distância
distancia =  round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2), 2)

# Exibição do resultado
print("A distância entre os pontos A", x1, ",", y1, "e B", x2, "," , y2, "é:", distancia)
