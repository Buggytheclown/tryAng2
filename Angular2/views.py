import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings


def AngIndex(request):
    return render(request, 'Angular2/index.html')


def Register(request):
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            received_json_data = json.loads(body_unicode)
            username = received_json_data['username']
            password = received_json_data['password']
            email = received_json_data['email']
        except:
            return JsonResponse({'err': 'bad json, incorrect input fields'})
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
        except:
            return JsonResponse({'err': 'Sorry, that user already exists!'})
        user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return JsonResponse({'token': token})
