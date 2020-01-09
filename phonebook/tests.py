from django.test import TestCase, Client
from . import models

# Create your tests here.


class PhoneBookTestCase(TestCase):
    def setUp(self):
        models.Entry.objects.create(phone='+71234567890', name='First')
        models.Entry.objects.create(phone='+61234567890', name='Second')
        self.c = Client()

    def test_search_entry_by_name(self):
        first = models.Entry.objects.get(name='First')
        response = self.c.get('/search/', {'query': 'First'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['entry_list'][0], first)

    def test_search_entry_by_phone(self):
        second = models.Entry.objects.get(phone='+61234567890')
        response = self.c.get('/search/', {'query': '+61234567890'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['entry_list'][0], second)

    def test_add_valid_entry(self):
        response = self.c.post('/add/', {'name': 'Third', 'phone': '+51234567890'})
        self.assertEqual(response.status_code, 302)
        entry = models.Entry.objects.get(name='Third')
        self.assertIsInstance(entry, models.Entry)

    def test_add_invalid_entry(self):
        response = self.c.post('/add/', {'name': 'invalid name *&$%)@!', 'phone': 'invalid phone number'})
        entry_exists = models.Entry.objects.filter(phone='invalid phone number').exists()
        self.assertEqual(response.status_code, 200)
        self.assertFalse(entry_exists)

    def test_entry_detail(self):
        first = models.Entry.objects.get(name='First')
        response = self.c.get(f'/detail/{first.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['entry'], first)

    def test_delete_entry(self):
        second = models.Entry.objects.get(name='Second')
        self.c.post(f'/delete/{second.id}/')
        entry_exists = models.Entry.objects.filter(pk=second.pk).exists()
        self.assertFalse(entry_exists)

    def test_edit_entry(self):
        first = models.Entry.objects.get(name='First')
        response = self.c.post(f'/edit/{first.id}/', {'name': 'First update', 'phone': '+99999999999'})
        self.assertEqual(response.status_code, 302)
        changed_entry = models.Entry.objects.get(pk=first.pk)
        self.assertEqual(changed_entry.name, 'First update')
        self.assertEqual(changed_entry.phone, '+99999999999')
