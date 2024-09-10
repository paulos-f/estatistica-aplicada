from flask import Flask, render_template, request, redirect, url_for
import os
from analise_csvs import analisar_csvs

app = Flask(__name__)

# Pasta para armazenar os uploads
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para upload dos arquivos CSV
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'csvFile' not in request.files:
        return "Nenhum arquivo selecionado", 400

    files = request.files.getlist('csvFile')
    
    # Salvar arquivos enviados
    for file in files:
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    # Obter o fornecedor selecionado
    fornecedor = request.form.get('fornecedor')

    # Chamar a função de análise com base nos arquivos e fornecedor selecionado
    analisar_csvs(UPLOAD_FOLDER, fornecedor)

    # Redirecionar para a página de gráficos
    return redirect(url_for('graficos'))

# Página para exibir os gráficos
@app.route('/graficos')
def graficos():
    return render_template('graficos.html')

if __name__ == '__main__':
    app.run(debug=True)
