from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request,'home.html')


def aboutpage(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist =fulltext.split()

    wordictionary={}

    for word in wordlist:
        if word in wordictionary:
            # increase
            wordictionary[word] +=1
        else:
            # add to dictionary
            wordictionary[word] =1

    sortedwords = sorted(wordictionary.items(), key=operator.itemgetter(1), reverse =True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
