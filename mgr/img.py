from django.http import JsonResponse
import json
from common.models import Customer,Clocktime,Staff
from django.utils import timezone
import os
from datetime import datetime
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
def imgc(request):
    image = request.FILES.get('file',None)
    
    path=default_storage.save('img/'+image.name,ContentFile(image.read()))

    tmp_file = os.path.join(settings.MEDIA_ROOT,path)
   

    record = Staff.objects.create(photo=tmp_file)

    
    return JsonResponse({'ret': 0})


