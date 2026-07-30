import os
import stripe
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(['POST'])
def upgrade(request):
    stripe.api_key = os.environ['STRIPE_SECRET_KEY']
    return JsonResponse({'status': 'upgrade stub'})
