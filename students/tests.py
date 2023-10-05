from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import StudentProfile


# Create your tests here.
class StudentProfileAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="kiend", password="kien1029"
        )
        self.student_profile = StudentProfile.objects.create(
            user=self.user,
            student_id="12345",
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            date_of_birth="2000-01-01",
        )

    def test_get_student_profile(self):
        self.client.force_authenticate(User=self.user)
        
        response = self.client.get('/api/students/student-profiles/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data[0]['student_id'], '12345')
