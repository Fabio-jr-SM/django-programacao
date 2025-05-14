from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import CapturedImage
from django.shortcuts import render

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        img = request.FILES['image']
        CapturedImage.objects.create(image=img)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def camera_stream(request):
    return render(request, 'camera/stream.html')
