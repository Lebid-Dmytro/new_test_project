from django.urls import path

from restaurant import views


urlpatterns = [
    path('employees/', views.EmployeeViewSet.as_view({'get': 'list'})),
    path('restaurants/create/', views.RestaurantCreateView.as_view(), name='restaurant-create'),
    path('restaurants/<int:restaurant_id>/menu/create/', views.MenuCreateView.as_view(), name='menu-create'),
    path('restaurant/', views.RestaurantListView.as_view(), name='restaurants'),
    path('restaurant/<int:pk>/', views.MenuListView.as_view(), name='restaurant-menu'),
    path('vote/create/', views.VoteCreateView.as_view(), name='vote-create'),
    path('vote/', views.VoteView.as_view(), name='vote-list'),
    path('favorite_menu/', views.MaxVoteAPIView.as_view(), name='favorite_menu')

]