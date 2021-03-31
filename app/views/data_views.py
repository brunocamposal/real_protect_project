from flask import Blueprint, request
from http import HTTPStatus
from ..services.data_services import *

#linha que define a Blueprint que permitira a importação das rotas para o arquivo de distribuição __init__.py
bp_data = Blueprint('bp_data', __name__)

#Função responsavel por gerar a rota Home a qual nos retorna atravez do metodo GET um dicionario de chave unica data e valor sendo uma lista de mensagens
@bp_data.route("/", methods=['GET'])
def get_all_data():
    
    data = get_all_data_services()

    return {"data": data},HTTPStatus.OK

#Função responsavel por gerar as rotas de Filtragem a qual nos retorna atravez do metodo GET um dicionario de chave unica data e valor sendo uma lista de mensagens
@bp_data.route("/<string:filter>", methods=['GET'])
def data_filter(filter):

    filters = ("date", "hours", "message_code", "message",)

    if not filter in filters:

        return {
            "message": f"url not found, verify if your url is one of this {filters}"
            }, HTTPStatus.BAD_REQUEST

    data = request.get_json()

    filtered = get_filtered_data(data, filter)
    
    return {"data": filtered},HTTPStatus.OK