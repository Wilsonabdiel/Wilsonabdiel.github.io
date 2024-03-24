# script_executor/views.py
from django.http import HttpResponse
import webbrowser

def index(request):
    # Your Python script execution logic here
    url = 'https://codefather.tech/blog/'
    webbrowser.open(url)
    return HttpResponse("Python script executed successfully!")
