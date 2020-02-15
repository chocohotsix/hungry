from django.shortcuts import render

# Create your views here.
#render... 3개인자까지, 1번쨰 고정 request, 2번쨰 template이름, 3번쨰(선택)사전형 dictionary

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def result(request):
    text = request.GET['fulltext'] #글 전문
    words = text.split() #공백기준으로 나눈 것들을 리스트로
    word_dict = {}

    for w in words:
        if w in word_dict:
            word_dict[w]+=1
        else:
            word_dict[w]=1

    return render(request, 'result.html', {'full':text, 'totalwordnum':len(words), 'dict':word_dict.items()} )
