

# 1 - ler um conjunto de 4 número e 
# em seguida mostra a média. 

# entrada de dados
s1 = set()
soma = 0

# processamento
for i in range(4):
  valor = int(input(f"informe o valor{i+1}: "))
  soma += valor # soma = soma + valor
  print(f"passo {i+1} = {soma}")
  s1.add(valor)
  
print(f"a media deve ser: {soma/4}")
media = sum(s1)/len(s1)

#saída
print(f"a média foi de {media}")
print("fim do programa!")