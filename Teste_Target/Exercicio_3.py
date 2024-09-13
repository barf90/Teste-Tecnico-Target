# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import pandas as pd

df = pd.read_json('Teste_Target/dados.json') # lendo o arquivo com pandas
df_sem_zero = df[df['valor'] != 0] # data frame desconsiderando os dias com valor = 0

# pegando menor faturamento e o dia do menor faturamento
menor_valor = df['valor'].min() 
dia_menor_valor = df[df['valor'] == menor_valor]['dia'].values[0]

# pegamdo o maior faturamento e o dia do maior faturamento
maior_valor = df['valor'].max()
dia_maior_valor = df[df['valor'] == maior_valor]['dia'].values[0]

media = df_sem_zero['valor'].mean() # calcula da média do faturamento desconsiderando os dicas com valor 0
dias_acima_media = df_sem_zero[df_sem_zero['valor'] > media] # filtrando os dias maiores que a média
count_dias_acima_media = len(dias_acima_media) # contagem dos dias maiores que a média


print(f"O dia do menor faturamento: {dia_menor_valor}")
print(f"O menor faturamento: {menor_valor}")

print("-"*20)

print(f"O dia do maior faturamento: {dia_maior_valor}")
print(f"O maior faturamento: {maior_valor}")

print("-"*20)

print(f"Número de dias acima da média: {count_dias_acima_media}")
