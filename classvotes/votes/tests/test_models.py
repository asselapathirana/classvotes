from django.core.exceptions import ValidationError
from django.test import TestCase

from votes.models import Vote

class VotesModelsTest(TestCase):

    def test_can_not_save_empty_vote_name(self):
        vote_ = Vote(vote_name='')
        with self.assertRaises(ValidationError):
            vote_.save()
            vote_.full_clean()
    
