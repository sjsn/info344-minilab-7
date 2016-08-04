from rest_framework import serializers
from books_api.models import Author, Publisher, Book

class AuthorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Author
		fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model = Publisher
		fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
	author = AuthorSerializer(read_only=True, many=True)
	publisher = PublisherSerializer(read_only=True, many=True)

	class Meta:
		model = Book
		fields = '__all__'
			