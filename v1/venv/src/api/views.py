from django.http import JsonResponse


def home(req, *args, **kwargs):
    return JsonResponse({'project': 'Django authentication api'})
