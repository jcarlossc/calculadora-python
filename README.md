📟 Calculadora Gráfica em Python com Tkinter

Interface gráfica de uma calculadora simples, desenvolvida em Python 3 utilizando a biblioteca Tkinter, com suporte às quatro operações básicas: adição, subtração, multiplicação e divisão.

---

🧠 Funcionalidades

- Interface gráfica responsiva com Tkinter
- Entrada de dados numéricos e operadores por botões
- Exibição da expressão matemática em tempo real
- Cálculo automático com botão de =
- Botão C para limpar a entrada
- Tratamento de erros para expressões inválidas

---

## Ferramentas utilizadas

- Python 3.9.13
- Ambiente virtual `venv`
- Módulo `tkinter`
- `unittest` para testes
- Git/GitHub
- Visual Studio Code
- Sistema operacional Windows 10

---

## Como utilizar

```bash
# Clone o repositório
git clone https://github.com/jcarlossc/calculadora-python.git

# Acesse o diretório
cd calculadora-python

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate           # Windows
source venv/bin/activate        # Linux/macOS

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
python app.py

# Para sair do ambiente virtual
deactivate
```

---

## Contribuição:

Se quiser contribuir para este projeto, fique à vontade para enviar um pull request ou relatar problemas na seção de issues.

---

## Licença:

Este projeto é licenciado sob a Licença MIT.

---

## Comandos importantes:

```bash
python -m venv venv               # Cria um ambiente virtual
venv\Scripts\activate             # Ativa o ambiente no Windows
source venv/bin/activate          # Ativa o ambiente no Linux/macOS
deactivate                        # Encerra o ambiente virtual

pip install nome-pacote           # Instala um pacote
pip uninstall nome-pacote         # Remove um pacote
pip freeze > requirements.txt     # Gera (ou atualiza) o arquivo de dependências
pip install -r requirements.txt   # Instala pacotes listados no requirements.txt
pip list                          # Lista pacotes instalados
pip show nome-pacote              # Exibe detalhes de um pacote
```