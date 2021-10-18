from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

UserModel = get_user_model()

class PetstagramTestCase(TestCase):
    def assertListEmpty(self, ll):
        return self.assertListEqual([], ll, 'The list is not empty')

class ProfileDetailsTest(PetstagramTestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = UserModel.objects.create_user(email='damian1999@abv.bg', password='DASSggdee3211!2^')

    def test_get_detailsWhen_logged_in_userShould_get_details(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile details'))

        self.assertListEmpty(list(response.context['pets']))
        self.assertEqual(self.user.id, response.context['profile'].user_id)
