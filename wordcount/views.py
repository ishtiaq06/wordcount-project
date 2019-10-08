from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    wordtionary = {}

    for word in wordlist:
        if word in wordtionary:
            wordtionary[word] += 1
        else:
            wordtionary[word]=1



    return render(request,'count.html', {'fulltext':fulltext,'count':len(wordlist),'wordtionary1':wordtionary.items()})
def about(request):

    return render(request,'about.html')
