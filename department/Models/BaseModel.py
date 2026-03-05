from uuid import UUID

from django.db import models
import uuid

"""
    BaseModel --> bu model yordamida Models package dagi barcha filelrda takrorlanishi 
                  kutilayotgan fildlarni qisqartirdik. Ma'ni factor qilib oldik. Bu yordamida 
                  takrorlanishlar oldini olindi. 
"""

class BaseModel(models.Model):
    pass
