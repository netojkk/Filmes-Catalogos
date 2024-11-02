from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

filmes_data = [
    {
        "title": "Procurando Nemo", "image":"https://via.placeholder.com/150", "year": "2005"
    },
    {
        "title": "Procurando Dory", "image":"https://via.placeholder.com/150", "year": "2018"
    },
    {
        "title": "Duna", "image":"https://via.placeholder.com/150", "year": "2023"
    },
    {
        "title": "Madagascar", "image":"https://via.placeholder.com/150", "year": "2009"
    },
    {
        "title": "Os incriveis", "image":"https://via.placeholder.com/150", "year": "2007"
    },
]

def busca_filme(request):
    query = request.GET.get("query", "").lower()
    filtered_movies = [filme for filme in filmes_data if query in filme['title'].lower()]
    return JsonResponse(filtered_movies, safe=False)