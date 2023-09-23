from rest_framework import serializers

from restaurant.models import Restaurant, Menu, Employee, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'


class MaxVoteResultSerializer(serializers.Serializer):
    max_votes_for_restaurant = serializers.IntegerField()
    max_date = serializers.DateField()
    restaurant_name = serializers.CharField()


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
