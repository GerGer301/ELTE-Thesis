from django.test import TestCase, RequestFactory
from .models import LotteryTicket, HistoricalLotteryTicket
from myaccount.models import User
from .views import ticket_list, ticket_add, ticket_edit, ticket_delete, main_page, display_historical_lottery, check_lottery
from .forms import LotteryTicketForm
import datetime
# Create your tests here.

class TestLotteryTicket(TestCase):
    def setUp(self):
        User.objects.create(username='testuser', password='testpassword', nickname='testnickname', lottery_type='super lotto', telephone='00000000000', first_name='testfirst', last_name='testlast')
        user = User.objects.get(username='testuser')
        LotteryTicket.objects.create(user=user, red_1=1, red_2=2, red_3=3, red_4=4, red_5=5, red_6=6, blue_1=7, purchase_date='2021-01-01', price=2, won_amount=0)
    
    def test_lottery_ticket(self):
        user = User.objects.get(username='testuser')
        ticket = LotteryTicket.objects.get(user=user)
        self.assertEqual(ticket.red_1, 1)
        self.assertEqual(ticket.red_2, 2)
        self.assertEqual(ticket.red_3, 3)
        self.assertEqual(ticket.red_4, 4)
        self.assertEqual(ticket.red_5, 5)
        self.assertEqual(ticket.red_6, 6)
        self.assertEqual(ticket.blue_1, 7)
        self.assertEqual(ticket.purchase_date, datetime.date(2021, 1, 1))
        self.assertEqual(ticket.price, 2)
        self.assertEqual(ticket.won_amount, 0)

    def test_lottery_ticket_str(self):
        user = User.objects.get(username='testuser')
        ticket = LotteryTicket.objects.get(user=user)
        self.assertEqual(str(ticket), f'{user.username}\'s ticket on {ticket.purchase_date}')


class TestHistoricalLotteryTicket(TestCase):
    def setUp(self):
        HistoricalLotteryTicket.objects.create(draw_id=1, draw_date='2021-01-01', red_1=1, red_2=2, red_3=3, red_4=4, red_5=5, red_6=6, blue_1=7)
    
    def test_historical_lottery_ticket(self):
        ticket = HistoricalLotteryTicket.objects.get(draw_id=1)
        self.assertEqual(ticket.draw_date, datetime.date(2021, 1, 1))
        self.assertEqual(ticket.red_1, 1)
        self.assertEqual(ticket.red_2, 2)
        self.assertEqual(ticket.red_3, 3)
        self.assertEqual(ticket.red_4, 4)
        self.assertEqual(ticket.red_5, 5)
        self.assertEqual(ticket.red_6, 6)
        self.assertEqual(ticket.blue_1, 7)

    def test_historical_lottery_ticket_str(self):
        ticket = HistoricalLotteryTicket.objects.get(draw_id=1)
        self.assertEqual(str(ticket), f'Draw ID: {ticket.draw_id} on {ticket.draw_date}')

class TestAppsViews(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        User.objects.create(username='testuser', password='testpassword', nickname='testnickname', lottery_type='super lotto', telephone='00000000000', first_name='testfirst', last_name='testlast')
        user = User.objects.get(username='testuser')
        LotteryTicket.objects.create(user=user, red_1=1, red_2=2, red_3=3, red_4=4, red_5=5, red_6=6, blue_1=7, purchase_date='2021-01-01', price=2, won_amount=0)
        HistoricalLotteryTicket.objects.create(draw_id=1, draw_date='2021-01-01', red_1=1, red_2=2, red_3=3, red_4=4, red_5=5, red_6=6, blue_1=7)

    def test_ticket_list_GET(self):
        request = self.factory.get('/lotterytracker/ticket_list/')
        request.user = User.objects.get(username='testuser')
        response = ticket_list(request)
        self.assertEqual(response.status_code, 200)

    def test_ticket_add_GET(self):
        request = self.factory.get('/lotterytracker/ticket_add/')
        request.user = User.objects.get(username='testuser')
        response = ticket_add(request)
        self.assertEqual(response.status_code, 200)

    def test_main_page_GET(self):
        request = self.factory.get('/lotterytracker/main/')
        request.user = User.objects.get(username='testuser')
        response = main_page(request)
        self.assertEqual(response.status_code, 200)

    def test_display_historical_lottery_GET(self):
        request = self.factory.get('/lotterytracker/his_list/')
        request.user = User.objects.get(username='testuser')
        response = display_historical_lottery(request)
        self.assertEqual(response.status_code, 200)

    def test_check_lottery_GET(self):
        request = self.factory.get('/lotterytracker/check_lottery/')
        request.user = User.objects.get(username='testuser')
        response = check_lottery(request)
        self.assertEqual(response.status_code, 200)

class TestLotteryTicketForm(TestCase):
    def test_lottery_ticket_form(self):
        form = LotteryTicketForm(data={'red_1': 1, 'red_2': 2, 'red_3': 3, 'red_4': 4, 'red_5': 5, 'red_6': 6, 'blue_1': 7, 'purchase_date': '2021-01-01', 'price': 2, 'won_amount': 0})
        self.assertTrue(form.is_valid())

    def test_invalid_lottery_ticket_form_1(self):
        form = LotteryTicketForm(data={'red_1': 1, 'red_2': 45, 'red_3': 3, 'red_4': 4, 'red_5': 5, 'red_6': 6, 'blue_1': 7, 'purchase_date': '2021-01-01', 'price': 2, 'won_amount': 0})
        self.assertFalse(form.is_valid())

    def test_invalid_lottery_ticket_form_2(self):
        form = LotteryTicketForm(data={'red_1': 1, 'red_2': 2, 'red_3': 3, 'red_4': 4, 'red_5': 5, 'red_6': 6, 'blue_1': 7, 'purchase_date': '2021-01-01', 'price': -2, 'won_amount': 0})
        self.assertFalse(form.is_valid())
        form = LotteryTicketForm(data={'red_1': 1, 'red_2': 2, 'red_3': 3, 'red_4': 4, 'red_5': 5, 'red_6': 6, 'blue_1': 7, 'purchase_date': '2021--01', 'price': 2, 'won_amount': 0})
        self.assertFalse(form.is_valid())

class TestViewsFunctionality(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        User.objects.create(username='testuser', password='testpassword', nickname='testnickname', lottery_type='super lotto', telephone='00000000000', first_name='testfirst', last_name='testlast')
        user = User.objects.get(username='testuser')
        LotteryTicket.objects.create(user=user, red_1=1, red_2=2, red_3=3, red_4=4, red_5=5, red_6=6, blue_1=7, purchase_date='2021-01-01', price=2, won_amount=0)
        HistoricalLotteryTicket.objects.create(draw_id=1, draw_date='2021-01-01', red_1=1, red_2=2, red_3=3, red_4=4, red_5=5, red_6=6, blue_1=7)

    def test_check_lottery(self):
        request = self.factory.get('/lotterytracker/check_lottery/')
        request.user = User.objects.get(username='testuser')
        request.GET = {
            'red_1': 1,
            'red_2': 2,
            'red_3': 3,
            'red_4': 4,
            'red_5': 5,
            'red_6': 6,
            'blue_1': 7,
            'draw_red_1': 1,
            'draw_red_2': 2,
            'draw_red_3': 3,
            'draw_red_4': 4,
            'draw_red_5': 5,
            'draw_red_6': 6,
            'draw_blue_1': 7
        }
        response = check_lottery(request)
        self.assertEqual(response.status_code, 200)
