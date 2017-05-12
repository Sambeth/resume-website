from django.shortcuts import render, get_object_or_404
from .models import *
from django.contrib import messages
from .forms import PersonalInfoForm, WorkExperienceForm, EducationForm, SkillsForm
# Create your views here.

# View CV
def details(request):
	title = "Resume"
	user = request.user
	personalinfo = PersonalInfo.objects.filter(user=user)
	workexperience_detail = WorkExperience.objects.filter(personal_info=personalinfo)
	education_detail = Education.objects.filter(personal_info=personalinfo)
	skills_detail = Skills.objects.filter(personal_info=personalinfo)

	context = {'personalinfo': personalinfo,
			   'workexperience_detail': workexperience_detail,
			   'education_detail': education_detail,
			   'skills_detail': skills_detail,
			   'title': title
				}

	return render(request, "cv/details.html", context)




# creates new CV
def create(request):
	title = "Create CV"
	personalinfoform = PersonalInfoForm(request.POST or None, request.FILES or None)
	workexperienceform = WorkExperienceForm(request.POST or None)
	educationform = EducationForm(request.POST or None)
	skillsform = SkillsForm(request.POST or None)

	if personalinfoform.is_valid() and workexperienceform.is_valid() and educationform.is_valid() and skillsform.is_valid():
		instance = personalinfoform.save(commit=False)
		instance.user = request.user
		instance.save()
		workexperience = workexperienceform.save(commit=False)
		workexperience.personal_info = instance
		workexperience.save()
		education = educationform.save(commit=False)
		education.personal_info = instance
		education.save()
		skills = skillsform.save(commit=False)
		skills.personal_info = instance
		skills.save()

	context = {'personalinfoform': personalinfoform,
			   'workexperienceform': workexperienceform,
			   'educationform': educationform,
			   'skillsform': skillsform,
			   'title': title
				}

	return render(request, "cv/create.html", context)


# Updates CV

def update(request, id=None):
	title = "Update CV"
	instance = get_object_or_404(PersonalInfo, id=id)
	personalinfoform = PersonalInfoForm(request.POST or None, request.FILES or None, instance=instance)
	instance = get_object_or_404(WorkExperience, id=id)
	workexperienceform = WorkExperienceForm(request.POST or None, instance=instance)
	instance = get_object_or_404(Education, id=id)
	educationform = EducationForm(request.POST or None, instance=instance)
	instance = get_object_or_404(Skills, id=id)
	skillsform = SkillsForm(request.POST or None, instance=instance)

	if personalinfoform.is_valid() and workexperienceform.is_valid() and educationform.is_valid() and skillsform.is_valid():
		instance = personalinfoform.save(commit=False)
		instance.user = request.user
		instance.save()
		workexperience = workexperienceform.save(commit=False)
		workexperience.personal_info = instance
		workexperience.save()
		education = educationform.save(commit=False)
		education.personal_info = instance
		education.save()
		skills = skillsform.save(commit=False)
		skills.personal_info = instance
		skills.save()

	context = {'personalinfoform': personalinfoform,
			   'workexperienceform': workexperienceform,
			   'educationform': educationform,
			   'skillsform': skillsform,
			   'title': title
				}

	return render(request, "cv/create.html", context)









