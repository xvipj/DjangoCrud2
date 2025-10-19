from django.db.models.signals import post_save
from .models import NoticeModel
from .models import ExampleModel
from django.dispatch import receiver

# capturar el eveneto
@receiver(post_save, sender=ExampleModel)
def Notice_Example(sender, instance, created, **kwargs):
    if created:
        NoticeModel.objects.create(
            title=f"{instance.name} se ha creado"
        )