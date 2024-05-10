from django.shortcuts import render,HttpResponse
import requests

# Data upload


from django.http import JsonResponse

def get_data(request):
    try:
        with open(r'D:\Backup\deployment\initial app\myproject\api_.txt', 'r') as file:
            data = file.read()
        return JsonResponse({'data': data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# Get data from api
def index(request):
    # api_url = "https://data.covid19india.org/v4/min/data.min.json"
    api_url = 'http://127.0.0.1:8000/api/data/'   # local api

    response = requests.get(api_url)
    print("Api","-"*50)
    print(response)

    if response.status_code == 200:
        data = response.json()
        # Process the data here (e.g., render it in a template)
        return render(request, 'index.html', {'data': data})
    else:
        # Handle API error
        return HttpResponse("Error: API request failed")


def home(request):
    return render(request, 'home.html')

def respond_to_message(request):
    user_message = request.GET.get('message')
    response = "Hello! You said: {}".format(user_message)
    return JsonResponse({'response': response})

# def index(request):
#     return render(request, 'index.html')