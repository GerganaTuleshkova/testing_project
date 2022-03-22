from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from testing_project.common.models import Profile
from testing_project.common.views import ProfilesListView

UserModel = get_user_model()


class ProfileListsViewTests(TestCase):
    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('profile lists'))
        self.assertTemplateUsed(response, 'profiles/list.html')

    def test_get__when_two_profiles__expect_to_contains_two_profiles(self):

        profile1 = Profile(first_name='Gergana', last_name='Tuleshkova', age=25)
        profile2 = Profile(first_name='Gerganaa', last_name='Tuleshkovaa', age=35)
        profile1.save()
        profile2.save()
        # second way to create 2 profiles simultaneously with bulk_create, save() is not needed
        # Profile.objects.bulk_create([profile1, profile2])
        response = self.client.get(reverse_lazy('profile lists'))
        profiles = response.context['object_list']
        self.assertEqual(len(profiles), 2)
        # check also for actual profiles

    def test_get__when_no_logged_user__expect_context_user_to_be_No_user(self):
        response = self.client.get(reverse('profile lists'))
        expected_user = 'No user'
        actual_user = response.context['user']
        self.assertEqual(expected_user, actual_user)

    def test_get__when_logged_user__expect_context_user_to_be_username(self):

        # we need to have a user
        user_data = {
            'username': 'gerganat',
            'password': 'asd123',
        }
        # create user with user_data
        UserModel.objects.create_user(**user_data)
        # .client gives us login
        self.client.login(**user_data)
        response = self.client.get(reverse('profile lists'))
        actual_user = response.context['user']
        self.assertEqual(user_data['username'], actual_user)