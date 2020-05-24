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

#### Usando banco de dados
Existem diversas maneiras de se conectar a um banco de dados usando flask, mas hoje vamos abordar a conexão com sqlite3.
Seguindo a documentação, que você pode ler [aqui](https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/),
podemos facilmente fazer a conexão criando um arquivo para isso.

1. Criar um diretório database dentro do diretório app
    ```
    mkdir database
    ```
2. Criar arquivo `base.sql` para gerar o banco
    ```sql
    CREATE TABLE users(
        id integer,
        name varchar(80),
        constraint user_pk primary key(id)
    )
    ```
3. Criar um arquivo `connection.py`
    ```python
    import sqlite3
    from flask import g
    from app import app
    
    DATABASE = '/app/database/database.db'
    
    def get_db():
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sqlite3.connect(DATABASE)
        return db
    
    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    ```
    2.1. Para facilitar as consultas no futuro, é possível faze-las retornar dicionários adicionando o seguinte techo de código ao método get_db() antes do return
    ```python
    def make_dicts(cursor, row):
        return dict((cursor.description[idx][0], value)
                    for idx, value in enumerate(row))
    
    db.row_factory = make_dicts
    ```
4. Adicionar função para iniciar o banco de dados
    ```python
    def init_db():
        with app.app_context():
            db = get_db()
            with app.open_resource('./database/base.sql', mode='r') as f:
                db.cursor().executescript(f.read())
            db.commit()
    
    ```
5. Executar o python shell
    ```
   python3
   ```
   ```python
   from app.database.connection import init_db
   init_db()
    ```

#### Integrando BD com a interface web
Agora com a conexão pronta, podemos criar páginas web que criem, leiam, atualizem e deletem entidades (o famoso CRUD).

#### Links úteis
- [Renderização de template](https://flask.palletsprojects.com/en/1.1.x/api/#template-rendering)
- [Flask Quickstart](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [Flask redirect](https://flask.palletsprojects.com/en/1.1.x/api/#flask.redirect)
- [Flask url_for](https://flask.palletsprojects.com/en/1.1.x/api/#flask.url_for)

#### Configurando arquivos estáticos
Até agora estamos trabalhando com html plano, o que não é muito agradável à vista, portanto vamos configurar os arquivos estáticos

1. Criar diretório static dentro do diretório app
    ```
    mkdir static
    ```
2. Criar arquivo `styles.css`
    ```css
    *{
        margin: 0;
        padding: 0;
    }
    
    body{
        width: 100%;
        height: 100vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-family: 'Roboto', sans-serif;
    }
    ```
3. Adicionar referência ao estilo no `base.html`
    ```html
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    ```
4. Recarregar a página (limpando o cache)

Para outros arquivos estáticos como imagens ou código javascript se utiliza `{{ url_for('static', filename='nome_do_arquivo.extensão') }}` nos respectivos elementos html.
