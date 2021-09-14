from django.contrib import admin
from ratelimit.decorators import ratelimit


@ratelimit(key='ip', rate='2/h', block=True)
def extend_admin_login(request, extra_context=None):
    return admin.site.login(request, extra_context)
