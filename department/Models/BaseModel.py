from django.db import models
import uuid

"""
    BaseModel --> bu model yordamida Models package dagi barcha filelrda takrorlanishi 
                  kutilayotgan fildlarni qisqartirdik. Ma'ni factor qilib oldik. Bu yordamida 
                  takrorlanishlar oldini olindi. 
"""

class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    is_active = models.BooleanField(default=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.UUIDField(null=True, blank=True)
    updated_by = models.UUIDField(null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]
