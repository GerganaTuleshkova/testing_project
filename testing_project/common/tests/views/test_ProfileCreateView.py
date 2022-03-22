from django.test import TestCase
from django.urls import reverse

from testing_project.common.models import Profile


class ProfileCreateViewTests(TestCase):
    VALID_PROFILE_DATA = {
            'first_name': 'Gergana',
            'last_name': 'Tuleshkova',
            'age': 25,
        }

    def test_create_profile__when_all_valid__expect_to_be_created(self):
        # create post request
        self.client.post(
            reverse('create profile'),
            data=self.VALID_PROFILE_DATA,
        )

        profile = Profile.objects.first()
        self.assertIsNotNone(profile)
        self.assertEqual(self.VALID_PROFILE_DATA['first_name'], profile.first_name)
        self.assertEqual(self.VALID_PROFILE_DATA['last_name'], profile.last_name)
        self.assertEqual(self.VALID_PROFILE_DATA['age'], profile.age)

    # test redirect
    def test_create_profile__when_all_valid__expect_to_redirect_to_details(self):
        # create post request
        response = self.client.post(
            reverse('create profile'),
            data=self.VALID_PROFILE_DATA,
        )
        profile = Profile.objects.first()
        expected_url = reverse('profile details', kwargs={'pk': profile.pk})
        self.assertRedirects(response, expected_url)



    # test status code