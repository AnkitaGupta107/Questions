import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse


def get_json_response(python_dict):
        json_string = json.dumps(python_dict, cls=DjangoJSONEncoder)
        return HttpResponse(json_string, mimetype='application/json')