from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Comment
from .forms import CommentForm
from posts.models import Post
from django.shortcuts import get_object_or_404, redirect
from django.views import View

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.author = self.request.user  
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})
