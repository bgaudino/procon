from django.test import TestCase

from .models import Decision, Option, Pro, Con
from users.models import User


class OptionScoreTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com", password="testpassword"
        )
        self.decision = Decision.objects.create(title="Test decision", user=self.user)
        self.option = Option.objects.create(
            decision=self.decision,
            title="Test option",
        )

    def test_postitive_score(self):
        for weight in [1, 3]:
            Pro.objects.create(description="test", option=self.option, weight=weight)
        for weight in [
            1,
            2,
        ]:
            Con.objects.create(description="test", option=self.option, weight=weight)
        self.assertEqual(self.option.get_score(), 1)

    def test_negative_score(self):
        for weight in [2, 5]:
            Con.objects.create(description="test", option=self.option, weight=weight)
        for weight in [
            1,
            4,
        ]:
            Pro.objects.create(description="test", option=self.option, weight=weight)
        self.assertEqual(self.option.get_score(), -2)

    def test_no_pros(self):
        for weight in [1, 2, 3]:
            Con.objects.create(description="test", option=self.option, weight=weight)
        self.assertEqual(self.option.get_score(), -6)

    def test_no_cons(self):
        for weight in [3, 4, 5]:
            Pro.objects.create(description="test", option=self.option, weight=weight)
        self.assertEqual(self.option.get_score(), 12)

    def test_no_pros_no_cons(self):
        self.assertEqual(self.option.get_score(), 0)


class OptionsChooseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@test.com", password="testpassword"
        )
        self.decision = Decision.objects.create(title="Test decision", user=self.user)
        self.choiceA = Option.objects.create(title="A", decision=self.decision)
        self.choiceB = Option.objects.create(title="B", decision=self.decision)
        self.choiceC = Option.objects.create(title="C", decision=self.decision)

    def choose(self, choice):
        choice.choose()
        self.assertEqual(Option.objects.get(pk=choice.pk).is_chosen, True)
        for choice in Option.objects.exclude(pk=choice.pk):
            self.assertEqual(choice.is_chosen, False)

    def test_choose_A(self):
        self.choose(self.choiceA)

    def test_choose_B(self):
        self.choose(self.choiceB)

    def test_choose_C(self):
        self.choose(self.choiceC)
