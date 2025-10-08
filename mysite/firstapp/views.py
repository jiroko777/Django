from django.http import HttpRequest,HttpResponse
from django.shortcuts import render 


def main(request):
        return render(request,'index.html',{
                'seznam':["he","he"]
                
        })


def idk(request: HttpRequest) -> HttpResponse:
        return HttpResponse("idk")

def articles(request: HttpRequest,article_id: int) ->HttpResponse:
        return HttpResponse(f"Tohle je article{article_id}")
def unique(request: HttpRequest) -> HttpResponse:
        return HttpResponse("Tohle je unikatni article :d")
def articles(request: HttpRequest,article_id: int, article_name: str="") -> HttpResponse:
        return HttpResponse(
                "This is article n.{}, {}".format(article_id,"Name of this article is {}".format(article_name) if article_name else "this is umamed article")
        )     
def article_main(request: HttpResponse) :
        return render(request,'hl_stranka.html')