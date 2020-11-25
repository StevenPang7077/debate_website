from django.shortcuts import render
from database.models import Student, Performance, Tournament, Round, Award
from django.shortcuts import get_object_or_404

# Create your views here.
def homepage(request):
	return render(request, 'homepage.html', context = {})

def leaderboard(request):
	
	#LIST get top debaters(by all rounds average):
	def top_students():
		ranked_list = []
		for student in Student.objects.all():
			ranked_list.append((student, student.average_round_score())) #name, score
		sorted_list = sorted(ranked_list, key=lambda student:student[1], reverse = True)
		count = 0
		ranked_list = []
		for student in sorted_list:
			count = count + 1
			ranked_list.append((student[0], student[1], count))
		print(ranked_list)
		return ranked_list

	def top_advanced():
		ranked_list = []
		for student in Student.objects.all():
			if (student.average_advanced_round_score() >= 0):
				ranked_list.append((student, student.average_advanced_round_score())) #name, score
		sorted_list = sorted(ranked_list, key=lambda student:student[1], reverse = True)
		count = 0
		ranked_list = []
		for student in sorted_list:
			count = count + 1
			ranked_list.append((student[0], student[1], count))
		print(ranked_list)
		return ranked_list

	def top_novice():
		ranked_list = []
		for student in Student.objects.all():
			if (student.average_novice_round_score() >= 0):
				ranked_list.append((student, student.average_novice_round_score())) #name, score
		sorted_list = sorted(ranked_list, key=lambda student:student[1], reverse = True)
		count = 0
		ranked_list = []
		for student in sorted_list:
			count = count + 1
			ranked_list.append((student[0], student[1], count))
		print(ranked_list)
		return ranked_list

	numbers = range(1,50000)

	top_debaters = top_students()
	top_advanced_debaters = top_advanced()
	top_novice_debaters = top_novice()

	context = {
		'ranked_by_all': top_debaters,
		'ranked_by_advanced': top_advanced_debaters,
		'ranked_by_novice': top_novice_debaters,
		'numbers': numbers,
	}
	return render(request, 'leaderboard.html', context = context)

def student_detail_view(request, pk):
	student = get_object_or_404(Student, pk = pk)
	performances = Performance.objects.filter(student__pk__exact = student.pk)
	context = {
		'student': student,
		'performances': performances,
	}
	return render(request, 'database/student_detail.html', context = context)

def performance_detail_view(request, pk):
	performance = get_object_or_404(Performance, pk = pk)
	awards = Award.objects.filter(performance__pk__exact = performance.pk)
	context = {
		'performance': performance,
		'rounds': Round.objects.filter(performance__pk__exact = performance.pk),
		'awards': awards,
	}
	return render(request, 'database/performance_detail.html', context = context)

def student_list(request):
	students = Student.objects.all()
	context = {
		'students': students,
	}
	return render(request, 'student_list.html', context = context)

def tournament_list(request):
	tournaments = Tournament.objects.all()
	context = {
		'tournaments': tournaments,
	}
	return render(request, 'tournament_list.html', context = context)

def tournament_detail_view(request, pk):
	tournament = get_object_or_404(Tournament, pk = pk)
	performances = Performance.objects.filter(tournament__pk__exact = tournament.pk)
	context = {
		'tournament': tournament,
		'performances': performances,
	}
	return render(request, 'database/tournament_detail.html', context)

