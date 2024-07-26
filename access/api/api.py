from flask.views import MethodView
from flask_smorest import Blueprint

blueprint = Blueprint("access", __name__, description="Access Control API")


@blueprint.route("/api/access/grant")
class Access(MethodView):
    def post(self, payload):
        return "access denied", 201
