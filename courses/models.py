from django.db import models
from datetime import datetime


class Course(models.Model):
	'''This is the generic course assignment structure'''
	course_name = models.CharField(max_length=200)
	lab_points = models.CharField(max_length=200)
	exam_points = models.CharField(max_length=200)
	project_points = models.CharField(max_length=200)
	project_title = models.CharField(max_length=200)
	project_deadline = models.DateField(default=datetime.now())
	# team_members = models.CharField(max_length=200)


class CourseDetails(models.Model):
	'''This is the details section of the course. Here you can find comments and other notes'''
	pass


class ProjectDetails(models.Model):
	'''This is the details section of the project. Here you can find the project description'''
	pass
