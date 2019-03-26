from django.http import JsonResponse
import requests
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
from pandas import json


@require_http_methods(["GET"])
def find_company_id(request):
    response = {}
    res_id = request.GET.get('res_id')
    s = requests.session()
    a = s.get(
        'http://skyhawkapi.huilab.cn/api/company/list?token=gAAAAABb7QceFcdkZOZhOcwT9MOn_r6uwmHbPPfWDe3_eY65YvK0rP2LevULA6R9eiXYk4bvYX7jonI7b6RhdaIyNGQpXjSnBKuoEvNF4rBgP01nyKlfLnBFruRN7HvX4uXDSIhV7-R-24HoTTN5lUYJQ_sph9xXQA%3D%3D')
    j = json.loads(a.text)
    for company in j['companyList']:
        if company['id'] == int(res_id):
            response = {"id": res_id, "name": company['brand']}
            break

    if response == {}:
        response = {"name": "wrong"}
    return JsonResponse(response)
