from flask import Blueprint
from ..services.data_services import get_all_Data_services

bp_data = Blueprint('bp_data', __name__)

@bp_data.route("/", methods=['GET'])
def get_all_data():
    
    data = get_all_Data_services()

    return data