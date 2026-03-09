from django.db import models
from django.db.models import Q
from . import BaseModel
from . import DeptName
from . import DeptYear


class DepartmentMember(BaseModel):

    ROLE_HEAD = "HEAD"
    ROLE_STAFF = "STAFF"
    ROLE_ASSISTANT = "ASSISTANT"

    ROLE_CHOICES = (
        (ROLE_HEAD, "Head Of Department"),
        (ROLE_STAFF, "Staff"),
        (ROLE_ASSISTANT, "Assistant"),
    )

    department = models.ForeignKey(
        DeptName.DepartmentName,
        on_delete=models.PROTECT,
        related_name="members"
    )

    user_id = models.UUIDField(db_index=True)

    year = models.ForeignKey(
        DeptYear.Year,
        on_delete=models.PROTECT,
        related_name="department_members"
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields=["department", "user_id", "year"],
                name="unique_department_member"
            ),

            models.UniqueConstraint(
                fields=["department", "year"],
                condition=Q(role="HEAD"),
                name="one_head_per_department_year"
            )

        ]

    def __str__(self):
        return f"{self.department.code} - {self.user_id} - {self.year}"