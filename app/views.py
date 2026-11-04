from django.shortcuts import render, get_object_or_404

from app import serializers
from app.models import Recipe
from app.serializers import RecipeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, response


# Create your views here.
class RecipeListCreateAPIView(APIView):
    def get(self,request):
        r=Recipe.objects.all()
        serializer_instance=RecipeSerializer(r,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer_instance=RecipeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class RecipeRetriewUpdateDestroy(APIView):
    def get(self,request,pk):
        r=get_object_or_404(Recipe,id=pk)
        serializer_instance=RecipeSerializer(r)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        r=get_object_or_404(Recipe,id=pk)
        serializer_instance=RecipeSerializer(r,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        r=get_object_or_404(Recipe,id=pk)
        serializer_instance=RecipeSerializer(r,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        r=get_object_or_404(Recipe,id=pk)
        r.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


