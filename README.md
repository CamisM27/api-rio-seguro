# API Rio Seguro

API desenvolvida em Python para um aplicativo de monitoramento da qualidade da água em comunidades ribeirinhas. 
A proposta tem como objetivo principal fornecer uma ferramenta acessível e intuitiva para o registro e acompanhamento de dados ambientais, contribuindo para a conscientização e preservação dos recursos hídricos.


# Tecnologias Utilizadas

- Python
- FastAPI
- SQLAlchemy
- MySQL
- JWT Authentication
- Uvicorn

---

# Principais Endpoints


---

# Integrantes

- Bianca Siqueira Massaroto
- Camilla Ribeiro Campos
- Marcos Vinícius Esaú dos Santos

---

# Configuração do Projeto

## 1. Criar ambiente virtual

python -m venv venv

## 2. Ativar ambiente virtual

Windows:
venv\Scripts\activate

## 3. Instalar dependências

pip install -r requirements.txt

## 4. Criar arquivo .env

Exemplo do .env:
```
DATABASE_URL=

KEY=

ALGORITHM=

TOKEN_EXPIRE=
```
## 5. Rodar projeto

uvicorn app.main:app --reload