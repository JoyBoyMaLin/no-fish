from django.http import JsonResponse


class STDResponse(JsonResponse):

    def __init__(self, *args, **kwargs):
        super(STDResponse, self).__init__(*args, **kwargs)
