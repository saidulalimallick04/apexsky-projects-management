from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

from Projects.models import Project
from .serializers import ProjectDetailsSerializer

# @api_view(['GET'])
# def get_projects(request, user_nickname):
    
#     QUERY_SET = Project.objects.filter(nickname = user_nickname)
    
#     if not QUERY_SET:
#         return Response({
#             'message': 'No Project Found!!',
#             'status' : False,
#         },status=status.HTTP_204_NO_CONTENT)
        
        
#     serialized_data = ProjectDetailsSerializer(QUERY_SET, many = True)
    
#     return Response({
#         'message': 'Projects Details Fetched Successfully.',
#         'status' : True,
#         'projects': serialized_data.data
#     },status=status.HTTP_200_OK)