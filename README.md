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

#### Flask para desenvolvimento web

Para usarmos flask no contexto de web, devemos fazer com que nossas views renderizem algo que os navegadores entendam. Em outras palavras vamos utilizar html.

1. Criar o diretório templates
    ```
    mkdir templates
    ```
2. Criar um arquivo base
    ```html
   <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Practice</title>
    </head>
    <body>
        <div class="content">
            {% block content %}
            {% endblock %}
        </div>
    </body>
    </html>
    ```
3. Criar um arquivo qualquer que herde de base.html
    ```html
    {% extends 'base.html' %}
    {% block content %}
        <h1>{{ title }}</h1>
        <p>{{ paragraph }}</p>
    {% endblock %}
    ```
4. Renderizar a página através das views
    ```python
    @app.route('/')
    def index():
        title = "Olá Mundo"
        paragraph = "Este é o primeiro teste sem preconceito com flask"
        return render_template('home.html', title=title, paragraph=paragraph)
    ```
5. Executar o script `run.py`
    ```
   python run.py
   ```