from django.db import models
import uuid


printing_type = [
    ('inkjet', 'Inkjet'),
    ('laser', 'Laser')
]


class Printer(models.Model):
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=200, null=True, blank=True)
    printer_type = models.CharField(max_length=24, choices=printing_type, default='inkjet')
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title + " " + self.model
