from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentApiViewModel
from .serializers import StudentApiViewSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

##### FUNCTION BASED API_VIEW ---------------------------

# @api_view(['GET'])
# def api_view(request):
#     return Response({'msg': 'hello world'})


# @api_view(['POST'])
# def api_view(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg': 'THIS IS POST REQUEST'})

# @api_view(['GET', 'POST'])
# def api_view(request):
#     if request.method == 'GET':
#         return Response({'msg': 'THIS GET REQUEST'})

#     if request.method == 'POST':
#         return Response({'msg': 'THIS IS POST REQUEST'})

###### CRUD WITH API VIEW

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def api_view(request, pk=None):
    if request.method == 'GET':
        id = pk

        if id is not None:
            stu = StudentApiViewModel.objects.get(pk=id)
            serializer = StudentApiViewSerializer(stu)
            return Response(serializer.data)

        stu = StudentApiViewModel.objects.all()
        serializer = StudentApiViewSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        serializer = StudentApiViewSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data post'}
            return Response(res, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk

        stu = StudentApiViewModel.objects.get(pk=id)
        serializer = StudentApiViewSerializer(stu, data= request.data)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data update'}
            return Response(res)

        return Response(serializer.errors)
    
    if request.method == 'PATCH':
        id = pk

        stu = StudentApiViewModel.objects.get(pk=id)
        serializer = StudentApiViewSerializer(stu, data= request.data , partial=True)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'data update'}
            return Response(res)

        return Response(serializer.errors)
    
    
    if request.method == 'DELETE':
        id = pk
        stu = StudentApiViewModel.objects.get(pk=id)

        stu.delete()
        res = {'msg': 'data delete'}
        return Response(res)
    
    return Response({'msg': 'data is not delete'})