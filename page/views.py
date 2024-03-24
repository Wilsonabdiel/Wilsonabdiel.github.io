# script_executor/views.py
from django.http import HttpResponseRedirect
import webbrowser

def index(request):
    # Your Python script execution logic here
    url = 'https://codefather.tech/blog/'
    webbrowser.open(url)
    return HttpResponseRedirect(url)
