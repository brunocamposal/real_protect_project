from .data_views import bp_data

#função que recebe todas as rotas e exporta elas para o arquivo central da aplicação
def init_app(app):
    app.register_blueprint(bp_data)