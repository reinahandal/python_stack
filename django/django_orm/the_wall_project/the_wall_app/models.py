from django.db import models
from login_registration_app.models import User

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def post_message(request):
    message = request.POST['message']
    user = User.objects.get(first_name=request.session['user_first_name'])
    Message.objects.create(message=message, user=user)


def add_comment(request):
    comment = request.POST['comment']
    message = Message.objects.get(id=request.POST['which_message'])
    user = User.objects.get(first_name=request.session['user_first_name'])
    Comment.objects.create(comment=comment,message=message, user=user)

def delete_message(request):
    message_to_delete = Message.objects.get(id=request.POST['delete_msg'])
    message_to_delete.delete()