from .data_views import bp_data

def init_app(app):
    app.register_blueprint(bp_data)