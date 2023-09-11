import string
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    return HttpResponse('Home\n<a href="https://docs.djangoproject.com/en/4.2/topics/http/urls/">Django URLS</a>   <a href="http://127.0.0.1:8000/urlapp/left">Go to Left</a>     <a href="http://127.0.0.1:8000/urlapp/right">Go to Right</a><a href="http://127.0.0.1:8000/urlapp/main">Go to MAIN</a>')
def left(request):
    return HttpResponse('This is Left<a href="http://127.0.0.1:8000/urlapp/">                     Back</a>')
def right(request):
    return HttpResponse('This is right<a href="http://127.0.0.1:8000/urlapp/">                    Back</a>')

def main(request):
    param = {'name':'Deva','place':'Chennai'}
    return render(request,"urlapp/main.html",param)

def analyze(request):
    txt = (request.POST.get('text','default'))
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    sp_rem=request.POST.get('sp_rem','off')
    counter = request.POST.get('counter','off')
    print(removepunc)
    print(txt)
    analyzed=txt
    text =""
    
        
        
    if removepunc=='on':
        for char in txt:
            if char not in string.punctuation:
                text = text + char
            
        analyzed=text
        params ={'purpose':'Remove Punctuations','analysedtext':analyzed}
        
    if(fullcaps=='on'):
        text=""
        for i in analyzed:
            text+=i.upper()
        analyzed=text
      
        params ={'purpose':'Capitalize','analysedtext':analyzed}
        
    if sp_rem=='on':
        text=""
        for i in analyzed:
            if i!=" ":
                text+=i
        analyzed=text
        params ={'purpose':'Space remover','analysedtext':analyzed}
        
    if counter=='on':
        c = len(analyzed)
        c=str(c)
        analyzed+=" "+"count = "+c
        params ={'purpose':'Character Counter','analysedtext':analyzed
                 }
    if   removepunc!='on' and  fullcaps!='on' and sp_rem!='on' and counter!='on':
        t= "Your text : "+txt
        params = {'analysedtext':t}
        return render(request,"urlapp/norem_punc.html",params)    
    else:
        return render(request,'urlapp/analyse.html',params)
            
   
        