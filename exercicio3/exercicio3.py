#Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
#na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem
#ser ignorados no cálculo da média;




import json

with open('faturamento_diario_agosto_2024.json', 'r') as file:
    faturamentos = json.load(file)

valores_faturamento = []
for dia in faturamentos:
    valores_faturamento.append(dia['faturamento'])

maior_faturamento = max(valores_faturamento)
menor_faturamento = min(valores_faturamento)

media_mensal = sum(valores_faturamento) / len(valores_faturamento)

dias_acima_media = 0
for faturamento in valores_faturamento:
    if faturamento > media_mensal:
        dias_acima_media = dias_acima_media + 1



print(f"O MAIOR faturamento do mês de Agosto de 2024 foi de R${maior_faturamento}")
print(f"O MENOR faturamento do mês de Agosto de 2024 foi de R${menor_faturamento}")
print(f"Número de dias com faturamento superior à média mensal: {dias_acima_media}")
