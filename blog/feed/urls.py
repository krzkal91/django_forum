



# Create your views here.
from django.conf.urls import url, include
from .views import main_feed, edit_post, delete_post, new_post, add_post, add_comment, new_comment, edit_comment, delete_comment


urlpatterns = [
    url(r'^$', main_feed, name="main_feed"),
    url(r'detail/(?P<id>\d+)/$', edit_post, name='edit_post'),
    url(r'detail/(?P<id>\d+)/delete/$', delete_post, name='delete_post'),
    url(r'detail/new/$',  new_post, name='new_post'),
    url(r'detail/new/add(?P<id>\d+)/$', add_post, name='add_post'),
    url(r'detail/comment/(?P<comment_id>\d+)/$', edit_comment, name='edit_comment'),
    url(r'detail/(?P<post_id>\d+)/comment/new/$', new_comment, name='new_comment'),
    url(r'detail/comment/(?P<comment_id>\d+)/add/$', add_comment, name='add_comment'),
    url(r'detail/comment/(?P<comment_id>\d+)/delete/$', delete_comment, name='delete_comment'),

]