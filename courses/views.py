from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from datetime import datetime
import logging


def index(req):
	'''This is the homepage. It display all currently stored course assignments'''
	courses = Course.objects.all()
	return render(req, 'courses/all_courses.html', {'courses': courses})


def get_course_data(req):
	'''On this page the user inputs the generic course info. This is not for Course or Project details/ comments'''
	return render(req, 'courses/get_course_data.html')


def add_course(req):
	'''This is the form submission view'''
	if req.method == "POST":
		form = CourseForm(req.POST)
		if form.is_valid():
			logging.info('Form is valid')
			course = Course()
			course.course_name = form.cleaned_data['course_name']
			course.lab_points = form.cleaned_data['lab_points']
			course.exam_points = form.cleaned_data['exam_points']
			course.project_points = form.cleaned_data['project_points']
			course.project_title = form.cleaned_data['project_title']
			course.project_deadline = form.cleaned_data['project_deadline']
			course.save()
	return redirect('index')


def get_course_details(req):
	'''This view is accessed when the user clicks the course name. A form pops up that takes in details about the course'''
	pass


def get_project_details(req):
	'''This view is accessed when the user clicks the project title. A form pops up that takes in details about the project'''
	pass