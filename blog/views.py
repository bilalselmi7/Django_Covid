from django.shortcuts import render
from django.http import HttpResponse

"""
posts = [
    {
     'author': 'Katell',
     'title': 'BlogP 1',
     'content': 'First post',
     'date_posted': '28/04/2020'
     },
    {
     'author':'KatellG',
     'title':'Blog P2',
     'content':'2 post',
     'date_posted':'27/04/2020'
     }
    ]
"""

# Create your views here.



def home(request):
    """
    context = {
        'post':posts
        }
    """
    """
    {%for post in posts%}
        <h1>{{post.title}}</h1>
    {% endfor%}
    """
    
    return render(request, 'blog/home.html')
    #return HttpResponse('<h1>Blog Home</h1>')

def demandes(request):
    return render(request, 'blog/demandes.html')
    #return HttpResponse('<h1>Blog About</h1>')

def demandeurs(request):
    return render(request, 'blog/demandeurs.html')
    #return HttpResponse('<h1>Blog About</h1>')







