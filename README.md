# msg-in-a-bottle

### 📄 `README.md`


# 📬 Message in a Bottle (Mensagens Anônimas) - Aplicação Cliente-Servidor com Flask + Sockets

Este projeto é uma aplicação de rede baseada em arquitetura **cliente-servidor**, onde usuários podem **enviar** e **ler mensagens anônimas** através de uma **interface web**. Foi desenvolvido para fins didáticos na disciplina de **Redes de Computadores (2025)**.


## 🧠 Funcionalidades

- Envio de mensagens anônimas via navegador
- Leitura aleatória de mensagens (consumo único)
- Histórico de mensagens enviadas e lidas salvo localmente (`historico.txt`)
- Comunicação paralela via socket TCP
- Captura de pacotes com Wireshark para análise de rede

---

## 🛠️ Tecnologias

- Python 3
- Flask (microframework web)
- Socket TCP (biblioteca `socket`)
- HTML + CSS (interface simples)
- Wireshark (captura e análise de tráfego)

---

## ⚙️ Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/mensagens-anonimas.git
   cd mensagens-anonimas

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o servidor:

   ```bash
   python servidor.py
   ```

4. Acesse a aplicação em:

   ```
   http://localhost:5000
   ```

   Ou via IP local em outros dispositivos da rede.

---

## 🧪 Testando o servidor TCP (opcional)

Use o script `cliente_socket.py` para enviar mensagens diretamente via socket TCP:

```bash
python cliente_socket.py
```

---

## 🌐 Estrutura do Projeto

```
.
├── servidor.py              # Backend Flask + socket TCP
├── cliente_socket.py        # Cliente de teste via socket
├── requirements.txt         # Dependências
├── historico.txt            # Armazena mensagens enviadas e lidas
├── templates/
│   ├── index.html           # Interface principal
│   └── tutorial.html        # Página de ajuda
└── static/
    └── style.css            # Estilo da interface
```

---

## 🕵️‍♂️ Captura com Wireshark

Para observar o tráfego entre clientes e servidor:

1. Abra o Wireshark
2. Aplique o filtro:

   ```
   tcp.port == 5000 || tcp.port == 12345
   ```
3. Inicie a captura e interaja com a aplicação
4. Exporte as evidências para o relatório da disciplina

---

## 👨‍💻 Autores

* João Davi Ribeiro Tavares Leite – 222001322

Disciplina: Redes de Computadores - 2025.1

Professora: Priscila Solís Barreto

---

## 📜 Licença

Uso acadêmico e educacional.
