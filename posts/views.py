"""Posts views"""

# django
from django.shortcuts import render

# utils
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Shanti Guzman',
            'picture': 'https://picsum.photos/200/200/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=1036',
    }
]

# Create your views here.
def list_posts(request):
    return render(request, "posts/feed.html", {'posts': posts})
