
#Django lib
from django.shortcuts import render
from rest_framework import viewsets
from general.serializers import *
from general.controllers import *
from django.http import HttpResponse
import pdb
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# Create your views here.

# class GeneralViewSet(viewsets.ModelViewSet, GeneralController):
#     '''
#     API endpoint that allows to get general information about Servers.
#     '''
#     serializer_class = GeneralSerializer

#     def list(self, request, *args, **kwargs):
#         return HttpResponse(self.get_general_info_list(request))
#     def retrieve(self, request, pk=None):
#         return HttpResponse(self.get_general_info(request, pk))
#         pass
#     def create(self, request, *args, **kwargs):
#         pass
#     def update(self, request, *args, **kwargs):
#         pass
#     def destroy(self, request, pk=None):
#         pass

from django.shortcuts import render



def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    return render(request, 'search/index.html')

@api_view(["POST"])
def get_file_details(request):
    
    table_name = request.data["file_name"]

    table_name.replace("\r","")
    
    data = get_general_info_list(request,table_name)
    return Response({"message":"sucess","data":data})





