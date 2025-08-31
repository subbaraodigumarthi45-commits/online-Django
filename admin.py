from django.contrib import admin
from accounts.models import User
from company.models import Company
from exam.models import Exam

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Exam)