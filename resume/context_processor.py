from django.contrib.auth.models import User


def project_context(request):

    context = {
        'author': User.objects.first()
    }

    return context