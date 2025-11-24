from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import DataPoint, Task

class SimpleTests(TestCase):
    def test_datapoint_create(self):
        dp = DataPoint.objects.create(name='t', value=1.0, ts=timezone.now())
        self.assertEqual(dp.name, 't')

    def test_task_owner(self):
        u = User.objects.create_user(username='u1', password='pass')
        t = Task.objects.create(title='X', owner=u)
        self.assertEqual(str(t).split()[0], 'X')
