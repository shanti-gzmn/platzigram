"""Posts views"""

# django
from django.http import HttpResponse

# utils
from datetime import datetime

posts = [
    {
        'name': 'Mont Blanc',
        'user': 'Shanti',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076',
    }
]

# Create your views here.
def list_posts(request):
    """List existing posts"""
    content = []
    for post in posts:
        content.append("""
    <p><strong>{name}</strong></p>
    <p><small>{user} - <i>{timestamp}</i></small></p>
    <figure> <img src = "{picture}"/></figure>
    """.format(**post))
    return HttpResponse('<br>'.join(content))
