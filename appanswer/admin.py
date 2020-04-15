from django.contrib import admin
from .models import FirstPage, ImageOfFirstPage, SecondPage, Answer, Password

# Register your models here.

admin.site.register(FirstPage)
admin.site.register(ImageOfFirstPage)
admin.site.register(SecondPage)
admin.site.register(Answer)
admin.site.register(Password)
