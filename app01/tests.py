from django.test import TestCase

# Create your tests here.
import os

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book.settings')
    import django
    django.setup()

    from app01 import models

    user_obj = models.User.objects.filter(pk=3).first()
    print(user_obj)

    print(user_obj.score)

    print(user_obj.get_score_display())