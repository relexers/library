from django.urls import  path, include
from . import views
from rest_framework import routers
from library.views import UserView, ListAddUser, EditBookDetail


router = routers.DefaultRouter()
router.register(r'reader', views.UserViewSet)
router.register(r'book', views.BookViewSet)

urlpatterns = [
    path('', ListAddUser.as_view(), name = 'users' ),
    path('reader/<reader_id>', UserView.as_view(), name='reader'),
    path('book/<book_id>', EditBookDetail.as_view(), name = 'edit_book'),
#API urls
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]






# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
