from django.db.models.fields import GenericIPAddressField
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer

# Create your views here.

from django.http import JsonResponse
from django.db import transaction
from comment.serializers import CommentSerializer
# from comment.models import Comment
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from comment.models import Comment
from comment.serializers import CommentSerializer

# class CommentsView(GenericAPIView):
#     serializer = CommentSerializer(comment)
#     json = JSONRenderer().render(serializer.data)
#     return json

@api_view(["Get"])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['Get'])
def comment_detail(request, pk):
    comments = Comment.objects.get(id=pk)
    serializer = CommentSerializer(comments, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def comment_create(request):
    serializer = CommentSerializer(data=request.query_params)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def comment_update(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment, data=request.data)

    if serializer.is_valid():
        with transaction.atomic():
            serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def comment_delete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return Response('Deleted')
# class CommentsView(GenericAPIView):
#     def get(self, request, *args, **krgs):
#         comment = Comment(email='leila@example.com', content='foo bar')
#         serializer = CommentSerializer(comment)
#         return JSONRenderer().render(serializer.data)