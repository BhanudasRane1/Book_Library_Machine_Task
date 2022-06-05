
from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.http import JsonResponse


from rest_framework.parsers import JSONParser

from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView





from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class BookAPIView(APIView):
    def get(self,request):
        book = Book.objects.all()
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)


class BookPost(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class BookDetails(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    def get_object(self,id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_400_NOT_FOUND)


    def get(self,request,id):
        book=self.get_object(id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    


    def put(self,request,id):
        book = self.get_object(id)
        serializer = BookSerializer(book,data=request.data)
        print("edittt")
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        book = self.get_object(id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






