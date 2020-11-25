from django.contrib import admin
from .models import Student, Tournament, Round, Performance, Type, Award

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ("name", "grad_year", "pk")

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
	list_display = ("type_of_debate",)

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ("school", "date", "pk")

@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
    list_display = ("student", "score", "form", "division")

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("student", "score", "rank_in_room_total")

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
	list_display = ("placement","form", "__str__", "tournament")