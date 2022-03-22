from django.core.exceptions import ValidationError
from django.test import TestCase

from testing_project.common.models import Profile


class ProfileTests(TestCase):
    VALID_USER_DATA = {
        'first_name': 'Gergana',
        'last_name': 'Tuleshkova',
        'age': 26,
    }

    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        profile = Profile(**self.VALID_USER_DATA)
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contains_a_digit__expect_to_fail(self):
        first_name = 'Ger9ana'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )
        with self.assertRaises(ValidationError) as context:
            # IMPORTANT!!! This is called in modelForms implicitly
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_dollar_sign__expect_to_fail(self):
        first_name = 'Gergana$'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )
        with self.assertRaises(ValidationError) as context:
            # IMPORTANT!!! This is called in modelForms implicitly
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_space__expect_to_fail(self):
        first_name = 'Ger ana'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_USER_DATA['last_name'],
            age=self.VALID_USER_DATA['age'],
        )
        with self.assertRaises(ValidationError) as context:
            # IMPORTANT!!! This is called in modelForms implicitly
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name__when_valid__expect_to_correct_full_name(self):
        profile = Profile(**self.VALID_USER_DATA)
        expected_fullname = f'{self.VALID_USER_DATA["first_name"]} {self.VALID_USER_DATA["last_name"]}'
        self.assertEqual(expected_fullname, profile.full_name)
