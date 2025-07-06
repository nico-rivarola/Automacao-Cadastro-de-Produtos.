# 🤖 Automação de Cadastro de Produtos Web

Automatize o cadastro de produtos em sistemas web com eficiência, segurança e escalabilidade! Este projeto utiliza **Python**, **Selenium** e **Pandas** para ler arquivos CSV e inserir dados automaticamente via interface web. Ideal para equipes que lidam com cadastros repetitivos em sistemas internos ou e-commerces.

---

## 🚀 Funcionalidades

✅ Login automático no sistema web  
✅ Leitura de produtos a partir de arquivos CSV  
✅ Preenchimento de formulários com dados reais  
✅ Submissão automática e iterativa de cadastros  
✅ Registro de logs de execução  
✅ Navegação segura entre campos  
✅ Estrutura modular e escalável

---

## 🖥️ Pré-requisitos

- Python 3.8+
- Google Chrome
- ChromeDriver compatível com sua versão do navegador

---

## 1. ⚙️ Instalação



```bash
git clone https://github.com/seu-usuario/automacao-cadastro-produtos.git
cd automacao-cadastro-produtos 
```
## 2. Crie um ambiente virtual 

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
## 3. Instale as dependências
```bash
pip install -r requirements.txt
```
## 4. Configure as credenciais e URL 
 
  Crie um arquivo .env com: 
 ```env
 URL=https://sistema-ficticio.com/login
EMAIL=seu_email@exemplo.com
SENHA=sua_senha_secreta
```

## 📦 Estrutura do Projeto
```bash 
automacao-cadastro-produtos/
│
├── data/
│   └── produtos.csv           # Arquivo com os produtos
│
├── src/
│   └── cadastro.py            # Script principal
│
├── .env                       # Variáveis de ambiente
├── requirements.txt           # Bibliotecas necessárias
└── README.md
```
## 🛠️ Como Usar
### Execute o script passando o caminho do CSV:
```bash
python src/cadastro.py --arquivo data/produtos.csv
``` 
Você verá logs informando o progresso de cada produto cadastrado.
## 🧪 Exemplo de Arquivo CSV
```csv
codigo,marca,tipo,categoria,preco,custo,observacoes
1234,Nike,Tênis,Esporte,299.90,150.00,Lançamento 2025
5678,Adidas,Camiseta,Casual,99.90,50.00,Algodão orgânico
```

🧩 Tecnologias Utilizadas

    Python

    Selenium

    Pandas

    python-dotenv

    ChromeDriver
    



---

## 👤 Sobre mim

Me chamo Nicolás, e sou apaixonado por análise de dados e machine learning.  
Conecte-se comigo no LinkedIn clicando no botão abaixo! 👇

<p align="center">
  📬 Me adicione no <a href="https://www.linkedin.com/in/nicol%C3%A1s-rivarola-011223176/" target="_blank">LinkedIn</a> !
</p>


---


⚠️ Avisos
Este script simula ações humanas em páginas web. Certifique-se de que o uso está de acordo com as políticas da plataforma alvo.

Não compartilhe arquivos .env com informações sensíveis.


