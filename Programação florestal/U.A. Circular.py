from math import pi
r = float(input('Qual é o valor do raio (m), da unidade amostral?\n'))
A = pi*(r**2)
print("A unidade amostral tem {:.2f} metros quadrados".format(A))
if A >= 700:
        print("É inviável aplicar unidades amostrais circulares acima de 700m².")
else:
        print('A unidade amostral está dentro dos padrões para uma unidade circular.')
print('Fim.')
