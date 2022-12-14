from django.shortcuts import redirect


def auth_middleware(get_response):
    def middleware(request):
        if not request.session.get('customer_id'):
            return redirect('login')

        reponse= get_response(request)
        return reponse
    return middleware