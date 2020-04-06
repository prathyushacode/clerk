import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_q.tasks import async_task

from questions.models import Submission
from questions.services.slack import send_submission_slack
from questions.services.submission import send_submission_email

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Submission)
def save_submission(sender, instance, **kwargs):
    submission = instance
    if submission.complete:
        logger.info("Dispatching commpletion tasks for Submission<%s]>", submission.id)
        async_task(send_submission_email, str(submission.pk))
        async_task(send_submission_slack, str(submission.pk))
