from django.shortcuts import render,redirect
import requests
from django.http import HttpResponseForbidden


def contents(request):
    return render(request,'contents.html')

def integrate(request):
    if(request.method=='GET'):
        return render(request, 'integrate.html', {'input':True})
    elif(request.method=='POST'):
        input1=request.POST['input1']
        input2 = request.POST['input2']
        try:
            URL = "http://ravigitte.pythonanywhere.com/solve"
            PARAMS = {'exp': 'integrate('+input1+','+input2+')'}
           # print(PARAMS)
            r = requests.get(url=URL, params=PARAMS)
            #print(r)
            data = r.json()
            print(len(data))
            print(data)
            expression = data[0]['input']
            htmltxt=''
            if(len(data)>2):
                for i in data:
                    if i['title']=='Integrate Steps':
                        htmltxt = i['output']
            elif(data[1]['title']=='Error'):
                htmltxt = data[1]['error']
            else:
                htmltxt = data[1]['output']

            html= render(request, 'integrate.html', {'input': False, 'latex': htmltxt, 'expression':expression})
            return html
        except:
            return HttpResponseForbidden('500 Internal Server Error', content_type='text/html')

def differentiate(request):
    if(request.method=='GET'):
        return render(request, 'differentiate.html', {'input':True})
    elif(request.method=='POST'):
        input1=request.POST['input1']
        input2=request.POST['input2']
        try:
            URL = "http://ravigitte.pythonanywhere.com/solve"
            PARAMS = {'exp': 'diff('+input1+','+input2+')'}
            r=requests.get(url=URL, params=PARAMS)
            print(r)
            data = r.json()
            print(len(data))
            print(data)
            expression = data[0]['input']
            htmltxt=''
            if(len(data)>2):
                for i in data:
                    if i['title']=='Derivative Steps':
                        htmltxt = i['output']
            elif(data[1]['title']=='Error'):
                htmltxt = data[1]['error']
            else:
                htmltxt = data[1]['output']
            return render(request, 'differentiate.html', {'input': False, 'latex': htmltxt, 'expression':expression})
        except:
            return HttpResponseForbidden('500 Internal Server Error', content_type='text/html')
