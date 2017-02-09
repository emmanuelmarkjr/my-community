from django.contrib import admin
from questions.models import Question, Answer, Tag


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)