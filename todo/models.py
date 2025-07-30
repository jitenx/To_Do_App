from django.db.models import Model, CharField, BooleanField, DateTimeField

# Create your models here.


class Task(Model):
    task = CharField(max_length=400)
    is_completed = BooleanField(default=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
