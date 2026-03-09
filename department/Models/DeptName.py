from django.db import models
from django.core.validators import RegexValidator
from . import BaseModel

"""
    DeptName --> bu model yordamida department nomlarini saqlash uchun yaratilgan model.
                 Yengil validation yordamida department code shakillanadi va keyinchalik
                 qo'llaniladi.
"""

code_validator = RegexValidator(
    regex=r'^[A-Z]{3,5}\/[A-Z]{2,3}-dept$',
    message="Code formati: AUZ/IT-dept ko‘rinishida bo‘lishi kerak"
)


class DepartmentName(BaseModel):
    name = models.CharField(max_length=50,unique=True)
    code = models.CharField(max_length=20,unique=True,validators=[code_validator])
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"