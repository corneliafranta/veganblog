from django.conf.urls import url
from blog_app import views


urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$',views.AboutView.as_view(), name='about'),
    url(r'documentaries/$', views.DocumentarieView.as_view(), name='documentaries'),
    url(r'faq/$', views.FaqView.as_view(), name='faq'),
    url(r'^contact/$', views.ContactView, name='contact'),
    url(r'impressum/$', views.ImpressumView.as_view(), name='impressum'),


    url(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.CreatePostView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(),name='post_delete' ),
    url(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comments_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),

    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),


    url(r'^recipes/$', views.RecipeListView.as_view(), name='recipe_list'),
    url(r'^recipe/(?P<pk>\d+)$', views.RecipeDetailView.as_view(), name='recipe_detail'),
    url(r'^recipe/new/$', views.CreateRecipeView.as_view(), name='recipe_new'),
    url(r'^recipe/(?P<pk>\d+)/edit/$',views.RecipeUpdateView.as_view(), name='recipe_edit' ),
    url(r'^recipe/(?P<pk>\d+)/delete/$', views.RecipeDeleteView.as_view(),name='recipe_delete' ),
    url(r'^recipe_drafts/$', views.RecipeDraftListView.as_view(), name='recipe_draft_list'),
    url(r'^recipe/(?P<pk>\d+)/publish/$', views.recipe_publish, name='recipe_publish'),

    url(r'^products/$', views.ProductListView.as_view(), name='product_list'),
    url(r'^products/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^products/new/$', views.CreateProductView.as_view(), name='product_new'),
    url(r'^products/(?P<pk>\d+)/edit/$',views.ProductUpdateView.as_view(), name='product_edit' ),
    url(r'^products/(?P<pk>\d+)/delete/$', views.ProductDeleteView.as_view(),name='product_delete' ),
    url(r'^product_drafts/$', views.ProductDraftListView.as_view(), name='product_draft_list'),
    url(r'^products/(?P<pk>\d+)/publish/$', views.product_publish, name='product_publish'),

    url(r'^thumbnail_image', views.ThumbnailImageUploadView, name='thumbnail_image_upload'),
]