from django.shortcuts import render
from django.http import HttpResponse
import json 
from django.http.response import JsonResponse
from .forms import BookForm
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict


# Create your views here.
def Greet(request):
    return HttpResponse("Hello Buddy!") 

@csrf_exempt
def create_book(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            form = BookForm(data)
            if form.is_valid():
                title = form.cleaned_data['title']
                print(title)
                form.save()
                return JsonResponse({"feedback" : "Book Named " +title+" is created Successfully!"}, status=201)
            return JsonResponse({'error': form.errors}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error" : "Only Http Method -> POST will be Entertained for this Request!"}, status=405)

@csrf_exempt
def get_book(request, id):
    if request.method == "GET":
        try:
            try:
                book_instance = Book.objects.get(id=id)
                title = book_instance.title
                author = book_instance.author
                isbn = book_instance.isbn
                return JsonResponse({
                    'title' : title,
                    'author' : author,
                    'isbn' : isbn
                }, status=201)
            except Book.DoesNotExist:
                return JsonResponse({'error': "No Such Records exists for this Id!"})
        except Exception as e:
            return JsonResponse({"error" :  str(e)}, status=500)
    return JsonResponse({"error" : "Only Get Methods will be Entertained for this Request!"}, status=405)
      
@csrf_exempt
def get_allBooks(request):
    if request.method == "GET":
        try:
            books = Book.objects.all()
            book_data = [model_to_dict(book) for book in books]
            return JsonResponse({"books" : book_data}, status=201)
        except Exception as e:
            return JsonResponse({
                'error' : str(e)
            }, status=500)
    return JsonResponse({
        'error' : 'Only Get Responses will be Entertained Here!'
    }, status=405)
      
@csrf_exempt
def put_book(request, id):
    if request.method in ["PUT", "PATCH"]:
        try:
            book_instance = Book.objects.get(id=id)
            data  = json.loads(request.body)
            for key, value in data.items():
                if key != "id" and hasattr(book_instance, key):
                    setattr(book_instance, key, value)
            book_instance.save()
            return JsonResponse({
                "feedback" : "Book Updated Successfully"
            }, status=201) 
        except Exception as e:
            return JsonResponse({
                'error' : str(e)
            }, status=500)
    return JsonResponse({
        'error' : 'Only PUT request will be entertained here!'
    }, status=405)
    
@csrf_exempt
def delete_book(request, id):
    if request.method == 'DELETE':
        try:
            book_instance = Book.objects.get(id=id)
            book_instance.delete()
            return JsonResponse({'feedBack' : 'Book Deleted Successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error' : str(e)}, status=500)
    return JsonResponse({
        'error' : "Only Delete Method is Entertained Here!"
    }, status=405)
    
    
    
    # ____________________________________________________________________
    
                # DOING CRUD WITH DJANGO REST FRAME_WORK
    #_____________________________________________________________________
    

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
from .models import Book
from .forms import BookForm
import json

@api_view(["POST"])
def book(request):
    return Response("List of Books",  status=status.HTTP_200_OK)



# Class Based View using viewset
class BookView(ViewSet):
    def list(self, request):
        if request.method == 'GET':
            try:
                books = Book.objects.all()
                book_list = [model_to_dict(book) for book in books]
                return Response({'List of Books' : book_list})
            except Exception as e:
                return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'error': 'Only Get request will be entertained Here!'}, status=405)
    
    def create(self, request):
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                form = BookForm(data)
                if form.is_valid():
                   form.save() 
                   return Response({'Success': "Book Instance Created Successfully!"}, status=status.HTTP_201_CREATED)
            except  Exception as e:
                return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'error': 'Only Post Requests will be Entertained Here!'}, status=405)
    
    def update(self, request, id):
        if request.method in ["PUT", "PATCH" ]:
            try:
                instance = Book.objects.get(id=id)
                data_fetched = json.loads(request.body)
                for key, value in data_fetched.items():
                    if key !=id and hasattr(instance, key):
                        setattr(instance, key, value)
                instance.save()
                return Response({'Success' : 'Book Modified Successfully'}, status=status.HTTP_205_RESET_CONTENT)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': 'Book Fully Updated'}, status=405)
    
    # def partial_update(self, request, id):
    #     return Response({'message': 'Book is Partially Updated'}, status=status.HTTP_206_PARTIAL_CONTENT)
    
    def retrieve(self, request, id):
        if request.method == "GET":
            try:
                instance = Book.objects.get(id=id)
                return Response({
                    'title' : instance.title,
                    'author' : instance.author,
                    'isbn' : instance.isbn,
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error' : str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'error': 'Only  Get Requests will be Entertained Here!'}, status=405)
    
    def delete(self, request, id):
        if request.method == "DELETE":
            try:
                instance = Book.objects.get(id=id)
                instance.delete()
                return Response({"Success" : "Object Successfully Deleted!"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error", str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'error': 'Only Delete Method will be Entertained Here!'}, status=405)


# ___________________________________________________________________________________________________________

                        # Step-by-step DRF Conversion of Your Code
# ___________________________________________________________________________________________________________

from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializer import BookSerializer



class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class BookRetrieveView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
    
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
    
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'