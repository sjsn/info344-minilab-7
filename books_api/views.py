from rest_framework import status 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from books_api.models import Author, Publisher, Book 
from books_api.serializers import BookSerializer, AuthorSerializer, PublisherSerializer

# Handles listing the books (get request) or adding new books (post request)
@api_view(['GET', 'POST'])
def book_list(request, format=None):
	if request.method == 'GET':
		books = Book.objects.all()
		book_serializer = BookSerializer(books, many = True)
		return Response(book_serializer.data)
	elif request.method == 'POST':
		book_serializer = BookSerializer(data = request.data)
		if book_serializer.is_valid():
			book_serializer.save()
			return Response(book_serializer.data, status = status.HTTP_201_CREATED)
		else:
			return Response(book_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
	else:
		return Response(book_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Handles displaying the information for a single book (get request)
@api_view(['GET'])
def book_detail(request, pk, format=None):
	try:
		book = Book.objects.get(pk=pk)
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)
	serializer = BookSerializer(book)
	return Response(serializer.data)
