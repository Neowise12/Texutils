#created by me
from ast import Str
from string import punctuation
from tokenize import String
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # prams = {'name':'anni','place':'mars'}
    # return HttpResponse('''<h1>hello</h1> <a href = "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> click click</a>''')
    # return render(request,'index.html',prams)
    return render(request,'index.html')



# def about(request):
#     return HttpResponse("hellob anniiii")


def analyze(request):


    djtext=request.POST.get('text','default')

    #<-------to check to checkboxes------->

    removepunc=request.POST.get('removepunc','off')
    allcaps=request.POST.get('allcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
    charcount=request.POST.get('charcount','off')
    
    
    # analyzed= djtext
    punctuations=''',:;…–(){}<>/?|\~`+=[]@#$%^&*_'''
    analyzed=""

    #<--------------checks
    if removepunc=="on":
        for char in djtext:
            if char not in punctuations :
                analyzed=analyzed+char
        params ={'purpose':'Removed punctuations','analyzed_text':analyzed}


    elif allcaps=="on":
        for char in djtext:
            analyzed=analyzed + char.upper()  
        params ={'purpose':'Changed to all caps','analyzed_text':analyzed}             
    elif newlineremover=="on":
        for char in djtext:
            if char != '\n':
                analyzed = analyzed+char
        params ={'purpose':'New line remove','analyzed_text':analyzed}             
    elif extraspaceremove=="on":
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char   
        params ={'purpose':'Extra space remove','analyzed_text':analyzed}      
    elif charcount=="on":
        c=0
        for char in djtext:
            if (char!= " "):
                c=c+1
        m= str(c)
        analyzed = "Number of letters are "+ m 
        params ={'purpose':'character count','analyzed_text':analyzed}             
    else:
        return HttpResponse("Error")
    
    print(djtext)
    print(removepunc)
    # return HttpResponse("removepunc")
    return render(request,'analyze.html',params)

# def removepunc(request):
#     print(request.GET.get('text','default'))
#     return HttpResponse("removepunc")
# def allcaps(request):
#     return HttpResponse("allcaps")
