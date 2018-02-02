# -*- coding: utf 8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse,HttpResponseRedirect
from api.models import *

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from django.http import JsonResponse

from datetime import datetime
from datetime import date
from django.db.models import Max, Sum, Min, Count
from api.models import *
from django.core import serializers

@api_view(['POST','GET'])
@permission_classes((AllowAny, ))
def alunos(request):
    al={}
    if request.method == 'GET':
        al = serializers. serialize('json', Aluno.objects.all())
        
	return HttpResponse(al[0])
