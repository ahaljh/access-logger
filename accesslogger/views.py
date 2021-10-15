from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Min
from .models import AccessLog


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def collect(request, page_name=None):
    saved = False 

    if page_name:
        access = AccessLog()
        access.page = page_name
        access.ip = get_client_ip(request)
        access.user_agent = request.headers.get('User-Agent')
        access.save()
        saved = True

    return render(request, "collect.html", {'page_name': page_name, 'ip': access.ip, 'user_agent': access.user_agent, 'saved': saved})


def report(request, page_name=None):
    access_logs = AccessLog.objects.all()

    all_access_logs = AccessLog.objects.all()
    if page_name:
        access_logs = all_access_logs.filter(page=page_name)
    
    access_logs_nodup = access_logs.values('page', 'ip', 'user_agent').annotate(first_accessed_time=Min('accessed_time')).values('page', 'ip', 'user_agent', 'first_accessed_time').order_by('first_accessed_time')

    return render(request, "report.html", {"accesses": access_logs, "accesses_nodup": access_logs_nodup, "page_name": page_name})


