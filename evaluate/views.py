from django.shortcuts import render,redirect
import requests
import latex2mathml.converter
import html2text
from bs4 import BeautifulSoup
import re

#from logic.logic import SymPyGamma
# Create your views here.
#http://ravigitte.pythonanywhere.com/solve/?exp=integrate(2*x%20+%20y,x)
def input(request):
    if(request.method=='GET'):
        return render(request,'input.html',{'input':True})
    elif(request.method=='POST'):
        input=request.POST['input']
        URL = "http://ravigitte.pythonanywhere.com/solve"
        PARAMS = {'exp': input}
        #print(PARAMS)
        r = requests.get(url=URL, params=PARAMS)
        #print(r)
        data = r.json()
        #print(len(data))
        #print(data)
        expression = data[0]['input']

        if(len(data)>2):
            for i in data:
                if i['title']=='Integral Steps':
                    htmltxt = i['output']
        elif(data[1]['title']=='Error'):
            htmltxt = data[1]['error']
        else:
            htmltxt = data[1]['output']

    #print(data[0]['output'])
        #htmltxt=data[1]['output']
        #print(htmltxt)
        html= render(request, 'input.html', {'input': False,'latex': htmltxt,'expression':expression})
        return html


