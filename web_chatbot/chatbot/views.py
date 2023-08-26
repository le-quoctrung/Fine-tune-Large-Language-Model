from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def reply(message):
    return 'Hi mian'

def chatbot(request):
    if request.method == 'POST':
        message =  request.POST.get('message')
        #response = 'Hi mian'
        response = reply(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')

