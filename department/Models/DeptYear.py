from django.db import models
from rest_framework.exceptions import ValidationError

from . import BaseModel

"""
    DeptYear --> bu model yordamida department azolarining muayyan qaysi yillarda faoliyat olib borganlarini,
                 yoki borayotganlarini bilishimiz mumkin va buni bazada saqlanishi hech qanday xatolarsiz saqlanib
                 boradi.
"""

class Year(BaseModel):
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()

    is_current = models.BooleanField(default=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["start_year", "end_year"],name="unique_academic_year")]
        ordering = ["-start_year"]

    def clean(self):

        if self.end_year <= self.start_year:
            raise ValidationError(
                "Boshlang'ich yil kichik bo'lishi kerak!"
            )

        if self.end_year != self.start_year + 1:
            raise ValidationError(
                "Academic year 1 yil bo‘lishi kerak!"
            )

    def __str__(self):
        return f"{self.start_year}/{self.end_year}"