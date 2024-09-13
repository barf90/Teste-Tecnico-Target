# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

faturamento_mensal = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES":27165.48, "Outros": 19849.53} # Dicionário com estados e faturamento
total = sum(faturamento_mensal.values()) # soma do faturamento dos estados


for estado in faturamento_mensal: # Loop para calcular o percentual que cada estado teve dentro do valor total mensal da distribuidora
    perc = (faturamento_mensal[estado]/total) * 100
    print(f"O estado {estado} representa {perc:.2f}% dentro do valor total da distribuidora")