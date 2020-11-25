from django.db import models


class Student(models.Model):
	name = models.CharField(max_length = 100, help_text = "Full Name")
	grad_year = models.IntegerField(help_text = "Form e.g '2022'")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('student-detail', args=[str(self.id)])

#QUERYSET get histroy of performances
	def all_performances(self):
		return Performance.objects.filter(student__pk__exact=self.pk)

#DOUBLE get average performance scores
	def average_performance_score(self):
		total_score = 0
		count = 0
		for performance in self.all_performances():
			count = count + 1
			total_score = total_score + performance.score
		if (count > 0):
			return round(total_score/count, 2)
		else:
			return -1

#LIST get histroy of rounds
	def all_rounds(self):
		my_rounds = []
		for single_performance in self.all_performances():
			for single_round in Round.objects.filter(performance__pk__exact=single_performance.pk):
				my_rounds.append(single_round)
		return my_rounds

#LIST get all advanced rounds
	def advanced_rounds(self):
		all_rounds = self.all_rounds()
		advanced_rounds = [one_round for one_round in all_rounds if one_round.division == "A"]
		return advanced_rounds

#LIST get all novice rounds
	def novice_rounds(self):
		all_rounds = self.all_rounds()
		novice_rounds = [one_round for one_round in all_rounds if one_round.division == "N"]
		return novice_rounds

#DOUBLE get average score for all rounds
	def average_round_score(self):
		count = 0
		score = 0
		for single_round in self.all_rounds():
			count = count + 1
			score = score + single_round.score
		if (count == 0):
			return -1
		else:
			return round(score/count, 2)


#DOUBLE get average scores for advanced rounds
	def average_advanced_round_score(self):
		count = 0
		score = 0
		for single_round in self.advanced_rounds():
			count = count + 1
			score = score + single_round.score
		if (count == 0):
			return -1
		else:
			return round(score/count, 2)

#DOUBLE get average scores for novice rounds
	def average_novice_round_score(self):
		count = 0
		score = 0
		for single_round in self.novice_rounds():
			count = count + 1
			score = score + single_round.score
		if (count == 0):
			return -1
		else:
			return round(score/count, 2)

#DOUBLE average rank in room(kinda cheese TBH)
	def average_rank_in_room(self):
		count = 0
		score = 0
		for single_round in self.all_rounds():
			count = count +1
			score = score + single_round.rank_in_room
		if (count == 0):
			return -1
		else:
			return round(score/count, 2)

#DOUBLE win/loss ratio
	def win_loss_ratio(self):
		wins = 0
		losses = 0
		for single_round in self.all_rounds():
			if (single_round.win == 1):
				wins = wins + 1
			elif (single_round.win == 0):
				losses = losses + 1
		if (losses == 0):
			return "Undefeated"
		else:
			return round(wins/losses, 2)



#a person's performance in an entire tournament
class Performance(models.Model):
	student = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
	tournament = models.ForeignKey('Tournament', on_delete = models.DO_NOTHING, null = True)

	def __str__(self):
		return self.student.name + " at " + str(self.tournament)

	def score(self):
		score = 0
		for single_round in Round.objects.filter(performance__pk__exact = self.pk):
			score = score + single_round.score
		return score

	def rank_in_room_total(self):
		total = 0
		for single_round in Round.objects.filter(performance__pk__exact = self.pk):
			total = total + single_round.rank_in_room
		return total

	def wins(self):
		total = 0
		for single_round in Round.objects.filter(performance__pk__exact = self.pk):
			if (single_round.win < 0): #bypass if N.A
				pass
			else:
				total = total + single_round.win
		return total

class Round(models.Model):
	form = models.ForeignKey("Type", help_text = "Type of competition", on_delete = models.DO_NOTHING, null = True)
	round_number = models.IntegerField()
	division = models.CharField(max_length = 30, help_text = "A, N, or U")
	comment = models.TextField(max_length = 3000, null = True, blank = True)
	win = models.IntegerField(help_text = "0 for loss, 1 for win, -1 for N.A", default = -1)
	rank_in_room = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0)
	score = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0)
	performance = models.ForeignKey(Performance, on_delete = models.DO_NOTHING, null = True)

	def __str__(self):
		return str(self.performance) + " (round " + str(self.round_number) + ")"

	def student(self):
		return self.performance.student.name

from datetime import datetime
class Tournament(models.Model):
	school = models.CharField(max_length = 300)
	date = models.DateField(null = True)

	def __str__(self):
		return self.school + " " + str(self.date.month) + "/" + str(self.date.day) + "/" + str(self.date.year)

class Type(models.Model):
	type_of_debate = models.CharField(max_length = 400)
	def __str__(self):
		return self.type_of_debate

class Award(models.Model):
	performance = models.ManyToManyField(Performance)
	placement = models.CharField(max_length = 400)
	holders = models.ManyToManyField(Student)
	tournament = models.ForeignKey(Tournament, on_delete = models.DO_NOTHING, null = True)
	form = models.ForeignKey(Type, on_delete = models.DO_NOTHING, null = True)

	def __str__(self):
		students_string = ""
		for student in self.holders.all():
			students_string = students_string + student.name + ", "
		return students_string


#former code
"""
class Student(models.Model):
	name = models.CharField(max_length = 100, help_text = "Full Name")
	form = models.IntegerField(help_text = "Form e.g '2022'")

	def history(self):
		return Performance.objects.filter(student__pk__exact = self.pk)

	def get_absolute_url(self):
		return reverse('student', args=[str(self.id)])

	def __str__(self):
		return self.name + " " + str(self.form)

class Performance(models.Model):
	student = models.ForeignKey(Student, on_delete = models.CASCADE)
	tournament = models.ForeignKey('Tournament',   on_delete = models.SET_NULL, null = True)

	def get_absolute_url(self):
		return reverse('performance', args=[str(self.id)])

class Tournament(models.Model):
	school = models.CharField(max_length = 100)
	data = models.DateField()

	def get_absolute_url(self):
		return reverse('tournament', args=[str(self.id)])


class Round(models.Model):
	round_number = models.IntegerField()
	performance = models.ForeignKey(Performance, on_delete = models.CASCADE)
	def get_absolute_url(self):
		return reverse('round', args=[str(self.id)])
"""