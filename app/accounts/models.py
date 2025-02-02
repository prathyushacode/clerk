from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation


class CaseGroups:
    # Can see everything, add coordinators, paralegals from users
    ADMIN = "Admin"
    # Can see everything, add paralegals
    COORDINATOR = "Coordinator"
    # Can see assigned cases
    PARALEGAL = "Paralegal"

    GROUPS = [ADMIN, COORDINATOR, PARALEGAL]


class User(AbstractUser):
    class Meta:
        db_table = "auth_user"

    is_intern = models.BooleanField(default=False)
    issue_notes = GenericRelation("core.IssueNote")

    def __str__(self):
        return self.email
