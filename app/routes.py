from flask import Blueprint

bp = Blueprint("main", __name__)

@bp.route("/")
def home():
    return {"message": "Bem-vindo ao Despensei com Flask!"}
