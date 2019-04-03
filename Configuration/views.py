import pandas
from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
import requests
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from pandas._libs import json

from .models import rtsp, idconfig, user


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
    terminal_id = request.GET.get('terminal_id')
    rtsp.objects.create(res_id=id1, res_name=res_name, camid=camid, rtsp=rtsp1, cam_name=cam_name,
                        terminal_id=terminal_id)
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
    terminal_id = request.GET.get('terminal_id')
    idconfig.objects.create(res_id=res_id, config=config, capturedserver=capturedserver, interval=interval, terminal_id=terminal_id)
    response = {"res": "ok"}
    return JsonResponse(response, safe=False)


@require_http_methods(['GET'])
def login(request):
    username = request.GET.get('name')
    password = request.GET.get('psw')
    res = user.objects.filter(user_name=username, user_password=password)
    if res:
        response = {"info": "ok"}
    else:
        response = {"info": "no"}
    return JsonResponse(response, safe=False)


@require_http_methods(['GET'])
def search_terminal(request):
    response = []
    results = idconfig.objects.all()
    for result in results:
        response.append(model_to_dict(result))
    return HttpResponse(json.dumps(response), content_type="application/json")


@require_http_methods(['GET'])
def search_idconfig_by_terminal(request):
    response = []
    maozi = '关'
    kouzhao = '关'
    mouse = '关'
    picture = '关'
    terminal = request.GET.get('terminal')
    id_config = idconfig.objects.filter(terminal_id=terminal)
    if id_config:
        res_id = id_config.first().res_id
        config = id_config.first().config
        capturedserver = id_config.first().capturedserver
        interval = id_config.first().interval
        name = rtsp.objects.filter(res_id=res_id)
        res_name = name.first().res_name
        for i in range(int(len(config) / 45)):
            maozi = '关'
            kouzhao = '关'
            mouse = '关'
            picture = '关'
            i = i * 45
            cam_id = config[i + 1:i + 4]
            p_1 = config[i + 5:i + 7]
            p_2 = config[i + 15:i + 17]
            p_3 = config[i + 25:i + 27]
            p_4 = config[i + 35:i + 37]
            if p_1 == '11':
                maozi = '开'
            if p_2 == '21':
                kouzhao = '开'
            if p_3 == '31':
                mouse = '开'
            if p_4 == '41':
                picture = '开'
            response.append(
                {'res_id': res_id, 'res_name': res_name, 'cam_id': cam_id, 'maozi': maozi, 'kouzhao': kouzhao,
                 'mouse': mouse, 'picture': picture})
    else:
        response.append({'res': 'no'})
    return JsonResponse(response, safe=False)


@require_http_methods(['GET'])
def del_rtsp_idconfig_by_terminal(request):
    terminal_id = request.GET.get('terminal_id')
    rtsp.objects.filter(terminal_id=terminal_id).delete()
    idconfig.objects.filter(terminal_id=terminal_id).delete()
    response = {'res': 'yes'}
    return JsonResponse(response, safe=False)
