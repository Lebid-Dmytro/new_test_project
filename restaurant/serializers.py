from rest_framework import serializers

from .models import Employee, Restaurant, Menu, Vote


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    your_read_only_field = serializers.ReadOnlyField()

    class Meta:
        model = Vote
        fields = '__all__'

    def create(self, validated_data):
        employee = self.context['request'].user.employee

        validated_data['employee'] = employee
        your_read_only_field_value = validated_data.get('your_read_only_field', None)
        validated_data.pop('your_read_only_field', None)

        vote = Vote.objects.create(**validated_data)

        return vote


class MaxVoteResultSerializer(serializers.Serializer):
    max_votes_for_restaurant = serializers.IntegerField()
    max_date = serializers.DateField()
    restaurant_name = serializers.CharField()
