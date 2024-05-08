# This file is used to test the views and models of the myaccount app.

from django.test import TestCase, Client, RequestFactory
from .models import User
from .forms import profileForm
from .views import profile, profile_update, main_page
# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='testuser', password='testpassword', nickname='testnickname', lottery_type='super lotto', telephone='00000000000', first_name='testfirst', last_name='testlast')

    def test_user(self):
        user = User.objects.get(username='testuser')
        self.assertEqual(user.nickname, 'testnickname')
        self.assertEqual(user.lottery_type, 'super lotto')
        self.assertEqual(user.telephone, '00000000000')
        self.assertEqual(user.first_name, 'testfirst')
        self.assertEqual(user.last_name, 'testlast')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'testpassword')
        self.assertEqual(user.__str__(), 'testuser')
        self.assertEqual(user.__class__.__name__, 'User')
        self.assertEqual(user._meta.ordering, ['id'])
        self.assertEqual(user._meta.app_label, 'myaccount')

    def test_user_save(self):
        user = User.objects.get(username='testuser')
        user.save()
        self.assertEqual(user.__class__.__name__, 'User')
        self.assertEqual(user._meta.verbose_name, 'user_info')

    def test_user_meta(self):
        user = User.objects.get(username='testuser')
        self.assertEqual(user._meta.verbose_name_plural, 'user_info')
        
class TestMyaccountViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create(username='testuser', password='testpassword', nickname='testnickname', lottery_type='super lotto', telephone='00000000000', first_name='testfirst', last_name='testlast')

    def test_profile(self):
        request = self.factory.get('/profile/')
        request.user = self.user
        response = profile(request)
        self.assertEqual(response.status_code, 200)

    def test_profile_update(self):
        request = self.factory.get('/profile/update/')
        request.user = self.user
        response = profile_update(request)
        self.assertEqual(response.status_code, 200)

    def test_main_page(self):
        request = self.factory.get('/profile/main/')
        request.user = self.user
        response = main_page(request)
        self.assertEqual(response.status_code, 200)

class TestProfileForm(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='testpassword', nickname='testnickname', lottery_type='super lotto', telephone='00000000000', first_name='testfirst', last_name='testlast')

    def test_profile_form(self):
        form = profileForm(data={'nickname': 'testnickname', 'first_name': 'testfirst', 'last_name': 'testlast', 'telephone': '00000000000', 'lottery_type': 'super lotto'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('nickname'), 'testnickname')
        self.assertEqual(form.cleaned_data.get('first_name'), 'testfirst')
        self.assertEqual(form.cleaned_data.get('last_name'), 'testlast')
        self.assertEqual(form.cleaned_data.get('telephone'), '00000000000')
        self.assertEqual(form.cleaned_data.get('lottery_type'), 'super lotto')

    def test_invalid_profile_form_1(self):
        form = profileForm(data={'nickname': 'testnickname', 'first_name': 'testfirst', 'last_name': 'testlast', 'telephone': '00000000000000000000000000000000'})
        self.assertFalse(form.is_valid())
