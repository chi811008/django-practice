from rest_framework import serializers
from comment.models import Comment

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

comment = Comment(email='leila@example.com', content='foo bar')

serializer = CommentSerializer(comment)

from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)
print(json)