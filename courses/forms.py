from django import forms


class CourseForm(forms.Form):
	course_name = forms.CharField(max_length=200)
	lab_points = forms.CharField(max_length=200)
	exam_points = forms.CharField(max_length=200)
	project_points = forms.CharField(max_length=200)
	project_title = forms.CharField(max_length=200)
	project_deadline = forms.DateField()
