import pandas as pd
import matplotlib.pyplot as plt
import os

def ler_csvs(upload_folder):
    # Carregar arquivos CSV enviados
    mes1 = pd.read_csv(os.path.join(upload_folder, 'mes1.csv'), sep=';')
    mes2 = pd.read_csv(os.path.join(upload_folder, 'mes2.csv'), sep=';')
    mes3 = pd.read_csv(os.path.join(upload_folder, 'mes3.csv'), sep=';')
    return mes1, mes2, mes3

def plotar_grafico_qualidade_completo(dados, mes, fornecedor):
    dados['hora'] = pd.to_datetime(dados['hora'], format='%H:%M').dt.time
    plt.figure(figsize=(12, 6))

    plt.plot(dados['dia'], dados[f'argila_fornecedor_{fornecedor}'], label=f'Argila {fornecedor.upper()}')
    plt.plot(dados['dia'], dados[f'qualidade_engobe_{fornecedor}'], label=f'Engobe {fornecedor.upper()}')
    plt.plot(dados['dia'], dados[f'qualidade_impressao_{fornecedor}'], label=f'Impressão {fornecedor.upper()}')
    plt.plot(dados['dia'], dados[f'qualidade_esmaltacao_{fornecedor}'], label=f'Esmaltação {fornecedor.upper()}')
    plt.plot(dados['dia'], dados[f'qualidade_forno_{fornecedor}'], label=f'Forno {fornecedor.upper()}')
    plt.plot(dados['dia'], dados[f'qualidade_escolha_{fornecedor}'], label=f'Escolha {fornecedor.upper()}')

    plt.title(f'Variação da Qualidade - {mes} - Fornecedor {fornecedor.upper()}')
    plt.xlabel('Dia')
    plt.ylabel('Qualidade')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()
    
    # Salvar o gráfico em vez de exibir
    plt.savefig(f'./static/{mes}_fornecedor_{fornecedor}.png')
    plt.close()

def calcular_media_qualidade(mes1, mes2, mes3, fornecedor):
    media_mes1 = mes1[[f'argila_fornecedor_{fornecedor}', f'qualidade_engobe_{fornecedor}', 
                       f'qualidade_impressao_{fornecedor}', f'qualidade_esmaltacao_{fornecedor}', 
                       f'qualidade_forno_{fornecedor}', f'qualidade_escolha_{fornecedor}']].mean()
    
    media_mes2 = mes2[[f'argila_fornecedor_{fornecedor}', f'qualidade_engobe_{fornecedor}', 
                       f'qualidade_impressao_{fornecedor}', f'qualidade_esmaltacao_{fornecedor}', 
                       f'qualidade_forno_{fornecedor}', f'qualidade_escolha_{fornecedor}']].mean()
    
    media_mes3 = mes3[[f'argila_fornecedor_{fornecedor}', f'qualidade_engobe_{fornecedor}', 
                       f'qualidade_impressao_{fornecedor}', f'qualidade_esmaltacao_{fornecedor}', 
                       f'qualidade_forno_{fornecedor}', f'qualidade_escolha_{fornecedor}']].mean()

    media_df = pd.DataFrame({
        'Mês 1': media_mes1,
        'Mês 2': media_mes2,
        'Mês 3': media_mes3
    })

    # Gerar gráfico da média de qualidade
    media_df.plot(kind='bar', figsize=(10, 6), title=f'Média da Qualidade - Fornecedor {fornecedor.upper()}', ylabel='Qualidade', xlabel='Variável')
    plt.savefig(f'./static/media_fornecedor_{fornecedor}.png')
    plt.close()

def analisar_csvs(upload_folder, fornecedor):
    mes1, mes2, mes3 = ler_csvs(upload_folder)

    # Gerar gráficos para cada mês
    plotar_grafico_qualidade_completo(mes1, 'Mes 1', fornecedor)
    plotar_grafico_qualidade_completo(mes2, 'Mes 2', fornecedor)
    plotar_grafico_qualidade_completo(mes3, 'Mes 3', fornecedor)

    # Gerar gráfico da média de qualidade
    calcular_media_qualidade(mes1, mes2, mes3, fornecedor)
