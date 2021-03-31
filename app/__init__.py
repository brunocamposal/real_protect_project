from flask import Flask

from .views import init_app

#Criando aplicação flask que resebera as rotas da pasta views, arquivo central do projeto
def create_app():
    app = Flask(__name__)

    init_app(app)

    return app