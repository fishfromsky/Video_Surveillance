from django.http import JsonResponse
import requests
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from pandas import json
from .models import rtsp, idconfig


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


@require_http_methods(['GET'])
def add_rtsp(request):
    id1 = request.GET.get('id')
    res_name = request.GET.get('res_name')
    camid = request.GET.get('camid')
    rtsp1 = request.GET.get('rtsp')
    cam_name = request.GET.get('cam_name')
    rtsp.objects.create(res_id=id1, res_name=res_name, camid=camid, rtsp=rtsp1, cam_name=cam_name)
    response = {"res": "ok"}
    return JsonResponse(response)


@require_http_methods(['GET'])
def see_rtsp(request):
    response = []
    res_id = request.GET.get('res_id')
    rtsps = rtsp.objects.filter(res_id=res_id)
    for s_rtsp in rtsps:
        response.append({'rtsp': s_rtsp.rtsp})
    return JsonResponse(response, safe=False)


@require_http_methods(['GET'])
def add_idconfig(request):
    res_id = request.GET.get('res_id')
    config = request.GET.get('config')
    capturedserver = request.GET.get('capturedserver')
    interval = request.GET.get('interval')
    idconfig.objects.create(res_id=res_id, config=config, capturedserver=capturedserver, interval=interval)
    response = {"res": "ok"}
    return JsonResponse(response, safe=False)
