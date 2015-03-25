from django.template import loader, Context
from django.http import HttpResponse
from t3_httplog.models import HttpRequestLogEntry


def requests(request):
    entries = HttpRequestLogEntry.objects.all().order_by('-date')[:10]
    t = loader.get_template('requests.html')
    html = t.render(Context(dict(entries=entries)))
    return HttpResponse(html)