from django.db import models

class Template(models.Model):
    pass

    def __str__(self) -> str:
        return f'{self.id}' # type: ignore
    
    class Meta:
        db_table = 'template'