from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import Restaurant, Menu, Employee, Vote
from django.utils import timezone


class RestaurantModelTestCase(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            description="Test Description",
            rating=4
        )

    def test_str_representation(self):
        self.assertEqual(str(self.restaurant), "Test Restaurant")


class MenuModelTestCase(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            description="Test Description",
            rating=4
        )
        self.menu = Menu.objects.create(
            restaurant=self.restaurant,
            dishes="Test Dish",
            description="Test Menu Description",
            date=timezone.now().date()
        )

    def test_str_representation(self):
        expected_str = f"{self.restaurant} - {self.menu.date}"
        self.assertEqual(str(self.menu), expected_str)


class EmployeeModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.employee = Employee.objects.create(employee=self.user)

    def test_str_representation(self):
        self.assertEqual(str(self.employee), "testuser")


class VoteModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant",
            description="Test Description",
            rating=4
        )
        self.employee = Employee.objects.create(employee=self.user)
        self.vote = Vote.objects.create(
            employee=self.employee,
            restaurant=self.restaurant,
            date=timezone.now().date()
        )

    def test_str_representation(self):
        expected_str = f"{self.employee} - {self.restaurant}"
        self.assertEqual(str(self.vote), expected_str)
