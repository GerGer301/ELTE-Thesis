# Test the main functions of the project
# Path: lotteryTracker/tests.py

from django.test import TestCase, Client, RequestFactory
from myaccount.models import User
from apps.models import LotteryTicket, HistoricalLotteryTicket
from apps.views import ticket_list, ticket_add, ticket_edit, ticket_delete, main_page, display_historical_lottery, check_lottery, dynamic_template_apps_calendar_view

class TestAccountSystem(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create(username='test', email='123@abc.com', password='test')
        self.user.save()

    def test_login(self):
        response = self.client.post('/accounts/login/', {'username': 'test', 'password': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.post('/accounts/logout/')
        self.assertEqual(response.status_code, 302)

    def test_registration(self):
        response = self.client.post('/accounts/signup/', {'username': 'test2', 'email': '123@abc.com', 'password': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_password_change(self):
        self.client.login(username='test', password='test')
        response = self.client.post('/accounts/password/change/', {'old_password': 'test', 'password1': 'test2', 'password2': 'test2'})
        self.assertEqual(response.status_code, 302)

    def test_password_reset(self):
        response = self.client.post('/accounts/password/reset/', {'email': '132@abc.com'})
        self.assertEqual(response.status_code, 302)

class TestTemplates(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create(username='test', email='123@abc.com', password='test')
        self.user.save()

    def test_main_page(self):
        request = self.factory.get('/')
        request.user = self.user
        response = main_page(request)
        self.assertEqual(response.status_code, 200)
    
class TestUserDatabase(TestCase):

    def setUp(self):
        User.objects.create(username='test', password='test')
        User.objects.create(username='test2', password='test2')

    def test_user_database(self):
        querySet = User.objects.all()
        self.assertEqual(querySet.count(), 2)

class TestLotteryTicketDatabase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create(username='test', password='test')
        self.user.save()
        LotteryTicket.objects.create(user=self.user, red_1=1, red_2=2, red_3=3, red_4=4, red_5=5, red_6=6, blue_1=7, purchase_date='2021-01-01', price=2, won_amount=0)
        LotteryTicket.objects.create(user=self.user, red_1=1, red_2=2, red_3=3, red_4=4, red_5=5, red_6=6, blue_1=7, purchase_date='2021-01-01', price=2, won_amount=0)

    def test_lottery_ticket_database(self):
        querySet = LotteryTicket.objects.all()
        self.assertEqual(querySet.count(), 2)
    
class TestHistoricalLotteryTicketDatabase(TestCase):
    
    def setUp(self):
        HistoricalLotteryTicket.objects.create(draw_id=1, draw_date='2021-01-01', red_1=1, red_2=2, red_3=3, red_4=4, red_5=5, red_6=6, blue_1=7)
        HistoricalLotteryTicket.objects.create(draw_id=2, draw_date='2021-01-02', red_1=1, red_2=2, red_3=3, red_4=4, red_5=5, red_6=6, blue_1=7)

    def test_historical_lottery_ticket_database(self):
        querySet = HistoricalLotteryTicket.objects.all()
        self.assertEqual(querySet.count(), 2)

class TestAppsCalendar(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create(username='test', password='test')

    def test_apps_calendar(self):
        request = self.factory.get('/apps/calendar/')
        request.user = self.user
        response = dynamic_template_apps_calendar_view(request, 'apps-calendar-month-grid')
        self.assertEqual(response.status_code, 200)

class TestFunctionality(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create(username='test', password='test')
        self.user.save()
        LotteryTicket.objects.create(user=self.user, red_1=1, red_2=2, red_3=3, red_4=4, red_5=5, red_6=6, blue_1=7, purchase_date='2021-01-01', price=2, won_amount=0)

    def test_login_failed(self):
        self.client.login(username='test', password='test1')
        response = self.client.post('/accounts/login/', {'username': 'test', 'password': 'test1'})
        self.assertEqual(response.status_code, 200)

    def test_add_ticket(self):
        self.client.login(username='test', password='test')
        response = self.client.post('/apps/lotterytracker/ticket_add/', {'red_1': 1, 'red_2': 2, 'red_3': 3, 'red_4': 4, 'red_5': 5, 'red_6': 6, 'blue_1': 7, 'purchase_date': '2021-01-01', 'price': 2, 'won_amount': 0})
        self.assertEqual(response.status_code, 302)

    

    
