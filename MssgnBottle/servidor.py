from flask import Flask, request, jsonify, render_template
import random
import os
import threading
import socket

app = Flask(__name__)
mensagens = []
HISTORICO_ARQUIVO = "historico.txt"

# 🔹 Função para registrar ações no histórico
def registrar(evento, mensagem):
    with open(HISTORICO_ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{evento.upper()}: {mensagem}\n")

# 🔹 Rota principal - Interface Web
@app.route('/')
def index():
    return render_template('index.html')

# 🔹 Enviar mensagem
@app.route('/enviar', methods=['POST'])
def enviar():
    msg = request.form['mensagem']
    mensagens.append(msg)
    registrar("enviada", msg)
    return '', 204

# 🔹 Listar todas as mensagens
@app.route('/mensagens', methods=['GET'])
def listar():
    return jsonify(mensagens)

# 🔹 Ler (consumir) uma mensagem aleatória
@app.route('/ler', methods=['GET'])
def ler_mensagem():
    if mensagens:
        msg = random.choice(mensagens)
        mensagens.remove(msg)
        registrar("lida", msg)
        return jsonify({'mensagem': msg})
    else:
        return jsonify({'mensagem': None})

# 🔹 Servidor TCP para testes com Wireshark
def socket_server():
    host = '0.0.0.0'
    port = 12345
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, port))
    servidor.listen()
    print(f"📡 Servidor socket executando em {host}:{port}")
    while True:
        conexao, endereco = servidor.accept()
        print(f"🔌 Conexão recebida de {endereco}")
        dados = conexao.recv(1024).decode()
        if dados:
            print(f"📨 Mensagem recebida via socket: {dados}")
            registrar("socket_recebida", dados)
            conexao.sendall(b"Mensagem recebida com sucesso.")
        conexao.close()

# 🔹 Inicializar histórico (se não existir)
if not os.path.exists(HISTORICO_ARQUIVO):
    with open(HISTORICO_ARQUIVO, "w", encoding="utf-8") as f:
        f.write("=== Histórico de Mensagens ===\n")

@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')


if __name__ == '__main__':
    # Iniciar socket server em thread paralela
    threading.Thread(target=socket_server, daemon=True).start()
    # Iniciar servidor Flask
    app.run(host='0.0.0.0', port=5000)
