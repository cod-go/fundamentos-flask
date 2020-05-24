# Fundamentos Flask

#### Primeiros passos em Flask

1. Criar ambiente virtual
    ```
    python3 -m venv venv
    ```
2. Ativar ambiente virtual
    ```
    source venv/bin/activate
    ```
   2.1. Atualizar o pip
   ```
    pip install --upgrade pip
    ```
3. Instalar o Flask
    ```
    pip install Flask
    ```
4. Criar estrutura de pastas do projeto
    
    4.1. Criar diretório app
    ```
   mkdir app
    ```
   4.2. Criar arquivo `views.py` no diretório app
   ```python
   from app import app

   @app.route('/')
   def index():
       return 'Hello world'
    ```
   
   4.3. Criar arquivo `__init__.py` no diretório app
    ```python
   from flask import Flask
    
   app = Flask(__name__)
    
   from app import views
    ```
    
    4.4 Criar arquivo `run.py` na raiz do projeto
    ```python
   from app import app

   if __name__ == '__main__':
       app.run(debug=True)
    ```
5. Executar o script `run.py`
```
python run.py
```