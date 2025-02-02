from django.db import models

from actionstep.constants import ActionFolder
from core.models import TimestampedModel
from core.models.issue import CaseTopic


def get_s3_key(file_upload, filename):
    return f"{file_upload.UPLOAD_KEY}/{filename}"


class ActionDocument(TimestampedModel):
    """
    A document to be uploaded to Actionstep
    """

    UPLOAD_KEY = "action-documents"
    FOLDER_CHOICES = (
        (ActionFolder.CLIENT, ActionFolder.CLIENT),
        (ActionFolder.PRECENDENTS, ActionFolder.PRECENDENTS),
        (ActionFolder.RESOURCES, ActionFolder.RESOURCES),
    )
    document = models.FileField(upload_to=get_s3_key)
    folder = models.CharField(max_length=32, choices=FOLDER_CHOICES)
    topic = models.CharField(max_length=32, choices=CaseTopic.CHOICES)
    actionstep_id = models.CharField(max_length=64, default="", blank=True)

    def get_filename(self):
        return self.document.file.name.split("/")[-1]
