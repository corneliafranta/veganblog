from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.urls import reverse_lazy
from blog_app.models import Post,Comments,Recipe, Product
from blog_app.forms import CommentForm, PostForm, RecipeForm, ProductForm, ThumbnailImageForm, ContactForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import get_template

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class DocumentarieView(TemplateView):
    template_name = 'documentaries.html'

class FaqView(TemplateView):
    template_name = 'faq.html'

class ImpressumView(TemplateView):
    template_name = 'impressum.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = PostForm
    model= Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
############################################################################################
######################################-COMMENTS-############################################


def add_comments_to_post(request,pk):
    post= get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment =form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog_app/comment_form.html', {'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comments,pk=pk )
    comment.approved()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment= get_object_or_404(Comments,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


#########################################################################
#############################Recipes#####################################

class RecipeListView(ListView):
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class RecipeDetailView(DetailView):
    model = Recipe

class CreateRecipeView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/recipe_detail.html'
    form_class = RecipeForm
    model= Recipe

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/recipe_detail.html'
    form_class = RecipeForm
    model = Recipe

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe_list')

class RecipeDraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/recipe_draft_list.html'
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(published_date__isnull=True).order_by('created_date')

@login_required
def recipe_publish(request, pk):
    recipe=get_object_or_404(Recipe,pk=pk)
    recipe.publish()
    return redirect('recipe_detail', pk=pk)

################################################################################
################################PRODUCT#########################################

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class ProductDetailView(DetailView):
    model = Product

class CreateProductView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/product_detail.html'
    form_class = ProductForm
    model= Product

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/product_detail.html'
    form_class = ProductForm
    model = Product

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product_list')

class ProductDraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/product_list.html'
    model = Product

    def get_queryset(self):
        return Product.objects.filter(published_date__isnull=True).order_by('created_date')

@login_required
def product_publish(request, pk):
    product=get_object_or_404(Product,pk=pk)
    product.publish()
    return redirect('product_detail', pk=pk)



def ThumbnailImageUploadView(request):
    form = ThumbnailImageForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
    else:
        return JsonResponse({'error': True, 'errors': form.errors})


######################################################################################
###################################Contact############################################

def ContactView(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            contact_subject =request.POST.get(
                'contact_subject', '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('blog_app/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_subject':contact_subject,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['franta-cornelia@gmx.at'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')
    print("HELLO")
    return render(request, 'contact.html', {
            'form': form_class,
    })