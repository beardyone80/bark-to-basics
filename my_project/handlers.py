# handlers.py

from django.http import HttpResponseForbidden

def custom_permission_denied(request, exception=None):
    return HttpResponseForbidden('You need to have permission to add a lesson. Please contact site admin. Use the back button on your browser to return to the previous page.')
