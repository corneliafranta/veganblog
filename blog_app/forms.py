from django import forms
from blog_app.models import Post,Comments, Recipe, Product
from .models import ThumbnailImage



class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text', 'image', 'category', 'thumbnail_image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'image': forms.FileInput(),
            'category': forms.Select(attrs={'class': 'foo'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
     }

class RecipeForm(forms.ModelForm):

    class Meta():
        model = Recipe
        fields = ('author', 'title', 'category', 'description', 'description2', 'ingredients', 'text', 'image', 'thumbnail_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'description': forms.Textarea(attrs={'class': 'editable medium-editor-textarea recipedescription'}),

            'ingredients': forms.Textarea(attrs={'class': 'editable medium-editor-textarea recipeingredients'}),
            'description2': forms.Textarea(attrs={'class': 'editable medium-editor-textarea recipedescription2'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea recipecontent'}),
            'image': forms.FileInput(),
            #'image2': forms.FileInput(),
            #'image3': forms.FileInput(),
            'category': forms.Select(attrs={'class': 'foo'})
        }

class ProductForm(forms.ModelForm):

    class Meta():
        model = Product
        fields = ('author', 'title', 'category', 'text', 'image', 'ingredients', 'company', 'thumbnail_image')


        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'company':forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea productcontent'}),
            'image': forms.FileInput(),
            'category': forms.Select(attrs={'class': 'foo'}),
            'ingredients': forms.Textarea(attrs={'class': 'editable medium-editor-textarea procuctingredients'}),
            'products': forms.TextInput(attrs={'class': 'textinputclass'}),
        }

class ThumbnailImageForm(forms.ModelForm):
    class Meta:
        model = ThumbnailImage
        fields = ('thumbnail_name', 'thumbnail_image',)


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_subject = forms.CharField()
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_subject'].label = "What do you want to talk about?"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label ="What do you want to say?"