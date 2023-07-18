from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test To-Do Item')
        self.assertFalse(item.done)

    def test_item_string_mehtod_returns_name(self):
        item = Item.objects.create(name='Test To-Do Item')
        self.assertEqual(str(item), 'Test To-Do Item')
