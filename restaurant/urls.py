from django.urls import path

from restaurant import views


urlpatterns = [
    path('employees/', views.EmployeeViewSet.as_view({'get': 'list'})),
    path('restaurant/', views.RestaurantListView.as_view()),
    path('restaurant/<int:pk>/', views.MenuListView.as_view()),
    path('vote/', views.VoteView.as_view()),
    path('favorite_menu/', views.MaxVoteAPIView.as_view()),

]