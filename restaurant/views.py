from django.db.models import Count
from django.utils import timezone
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from restaurant.models import Restaurant, Menu, Employee, Vote
from restaurant.serializers import RestaurantSerializer, MenuSerializer, VoteSerializer, \
    MaxVoteResultSerializer, EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    '''List of all employees'''
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class RestaurantCreateView(generics.CreateAPIView):
    '''Greate restaurant'''
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuCreateView(generics.CreateAPIView):
    '''Greate menu for today'''
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        restaurant_id = self.kwargs['restaurant_id']
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        serializer.save(restaurant=restaurant)


class RestaurantListView(generics.ListAPIView):
    '''Restaurant list'''
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuListView(generics.ListAPIView):
    '''Restaurant menu list'''
    today = timezone.now().date()
    queryset = Menu.objects.filter(date=today)
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]


class VoteCreateView(generics.CreateAPIView):
    '''Grete new vote'''
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        employee = self.request.user.employee
        serializer.save(employee=employee)


class VoteView(generics.ListAPIView):
    '''Vote list'''
    today = timezone.now().date()
    queryset = Vote.objects.filter(date=today)
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]


class MaxVoteAPIView(APIView):
    '''Selected favorite menu'''

    def get(self, request):
        try:
            today = timezone.now().date()

            max_votes_for_restaurant = (
                Vote.objects
                    .filter(date=today)
                    .values('restaurant__name')
                    .annotate(max_votes=Count('id'))
                    .order_by('-max_votes')
                    .first()
            )

            max_votes_for_restaurant_value = max_votes_for_restaurant['max_votes']
            max_votes_for_restaurant_name = max_votes_for_restaurant['restaurant__name']

            max_date_value = today

            data = {
                'max_votes_for_employee': None,
                'max_votes_for_restaurant': max_votes_for_restaurant_value,
                'max_date': max_date_value,
                'restaurant_name': max_votes_for_restaurant_name
            }

            serializer = MaxVoteResultSerializer(data=data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
