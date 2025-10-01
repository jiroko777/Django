from django.http import HttpRequest,HttpResponse
from django.shortcuts import render 


def main(request):
        '''jmeno = "jitka"
        cislo = 22
        barva = "modra"
        return render(request,'index.html',{
                'jmeno':jmeno,
                'cislo':cislo,
                'barva':barva
        })'''
        seznam = ["barva","jmeno","vek"]
        return render(request,'index.html',{
                'seznam':["he","he"]
                
        })

def idk(request: HttpRequest) -> HttpResponse:
        return HttpResponse("idk")