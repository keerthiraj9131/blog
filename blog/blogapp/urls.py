from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_view),
    path('tag/<tag_slug>/',views.post_view, name='post_list_by_tag'),
    path('<year>/<month>/<day>/<post>/',views.listdetailview, name='postdetail'),
    path('<id>/share/',views.mail_send_view)
]