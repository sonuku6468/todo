from rest_framework import serializers
 
# import the todo data model
from .models import Todo
 
#  serializer class
class TodoSerializer(serializers.ModelSerializer):
 
    # meta class
    class Meta:
        model = Todo
        fields = ('id', 'title','description','completed')