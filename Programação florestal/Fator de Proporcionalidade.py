A = float(input('Qual é o tamanho total da área (m²)? '))
a = float(input('Qual é o tamanho da unidade amostral(m²)? '))
Fat =  A/a
print("O fator de proporcionalidade é de {:.2f} parcelas por hectare.".format(Fat))
print('Fim.')
