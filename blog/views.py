from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import generic

from .forms import newPostForm
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, generic.CreateView):
    form_class = newPostForm
    template_name = 'blog/create_post.html'
    login_url = reverse_lazy('account_login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, _('Your post has been published.'))
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = newPostForm
    template_name = 'blog/create_post.html'
    login_url = reverse_lazy('account_login')

    def form_valid(self, form):
        messages.success(self.request, _('Your post has been updated.'))
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog-page')
    login_url = reverse_lazy('account_login')

    def form_valid(self, form):
        messages.success(self.request, _('Your post has been deleted.'))
        return super().form_valid(form)
