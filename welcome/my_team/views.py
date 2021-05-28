from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request,'input.html')

def result(request):
    sentence=request.GET['names']

    wordList=sentence.split(',')

    return render(request,'result.html',{'fulltext':sentence,'count':len(wordList),'wordlist':wordList})
