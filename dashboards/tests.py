from django.test import TestCase, Client, RequestFactory
from myaccount.models import User
from .views import dashboard, main_page

class TestDashboardViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        User.objects.create(username='testuser', password='testpassword', nickname='testnickname', lottery_type='super lotto', telephone='00000000000', first_name='testfirst', last_name='testlast')

    def test_dashboard_GET(self):
        request = self.factory.get('')
        request.user = User.objects.get(username='testuser')
        response = dashboard(request)
        self.assertEqual(response.status_code, 200)

    def test_main_page_GET(self):
        request = self.factory.get('/main/')
        request.user = User.objects.get(username='testuser')
        response = main_page(request)
        self.assertEqual(response.status_code, 200)
