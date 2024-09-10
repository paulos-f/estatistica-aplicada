import pandas as pd
import numpy as np

custo_forno = 6.46  
custo_argila_a = 9.90  
custo_argila_b = 12.46  
custo_engobe_a = 5.78  
custo_engobe_b = 5.43  

# Função para gerar dados para um dia
def gerar_dados_dia(dia, mes):
    horas = [f'{h:02}:00' for h in range(24)]  # Gerar lista de horas no formato 00:00, 01:00, etc.
    
    data = []
    for hora in horas:
        registro = {
            'mes': mes,
            'dia': f'Dia {dia}',
            'hora': hora,
            'argila_fornecedor_a': np.random.randint(31, 99),
            'qualidade_engobe_a': np.random.randint(31, 99),
            'qualidade_impressao_a': np.random.randint(31, 99),
            'qualidade_esmaltacao_a': np.random.randint(31, 99),
            'qualidade_forno_a': np.random.randint(31, 99),
            'qualidade_escolha_a': np.random.randint(31, 99),
            'argila_fornecedor_b': np.random.randint(31, 99),
            'qualidade_engobe_b': np.random.randint(31, 99),
            'qualidade_impressao_b': np.random.randint(31, 99),
            'qualidade_esmaltacao_b': np.random.randint(31, 99),
            'qualidade_forno_b': np.random.randint(31, 99),
            'qualidade_escolha_b': np.random.randint(31, 99),
            # Custos para Fornecedor A
            'argila_a_custo': custo_argila_a,
            'engobe_a_custo': custo_engobe_a,
            'impressao_a_custo': 0,  
            'esmaltacao_a_custo': 0,  
            'forno_a_custo': custo_forno,
            'escolha_a_custo': 0,  
            # Custos para Fornecedor B
            'argila_b_custo': custo_argila_b,
            'engobe_b_custo': custo_engobe_b,
            'impressao_b_custo': 0,  
            'esmaltacao_b_custo': 0,  
            'forno_b_custo': custo_forno,
            'escolha_b_custo': 0  
        }
        data.append(registro)
    return pd.DataFrame(data)

# Função para gerar dados de um mês (31 dias)
def gerar_dados_mes(mes):
    return pd.concat([gerar_dados_dia(dia, mes) for dia in range(1, 32)], ignore_index=True)

# Gerando dados para 3 meses diferentes
mes1 = gerar_dados_mes('Mes 1')
mes2 = gerar_dados_mes('Mes 2')
mes3 = gerar_dados_mes('Mes 3')

# Salvando cada mês em um arquivo CSV
mes1.to_csv('mes1.csv', index=False, sep=';')
mes2.to_csv('mes2.csv', index=False, sep=';')
mes3.to_csv('mes3.csv', index=False, sep=';')

print("Arquivos CSV para os 3 meses gerados com sucesso!")
