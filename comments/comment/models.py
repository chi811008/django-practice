from django.db import models

# Create your models here.
from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')

print(comment.content)


from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

comment = Comment(email='leila@example.com', content='foo bar')

serializer = CommentSerializer(comment)

from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)
print(json)