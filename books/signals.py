# https://docs.djangoproject.com/en/6.0/topics/signals/

import os
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Book


@receiver(pre_save, sender=Book)
def my_signal_pre_save(sender, instance: Book, **kwargs):
    # we can modify an instance before saving.
    # instance.title += "Haha funny"
    print("Saving book!.")

@receiver(pre_delete, sender=Book)
def cleanup_image(sender, instance: Book, **kwargs):
    # when a book is about to be deleted, also delete the image saved in the hard drive.
    if instance.image is not None:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
