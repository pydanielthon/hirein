from django import forms
from django.forms import Textarea



class NewJobForm(forms.Form):
    company = forms.CharField(label='Company name')
    website = forms.CharField(label='Website url')
    employ_numbers = forms.CharField(label='Number of employees')
    contract_type = forms.CharField(label='Contract Type')
    salary_st = forms.CharField(label='Salary from')
    salary_end = forms.CharField(label='Salary to')
    title = forms.CharField(label='Job offer title')
    experience_st = forms.CharField(label='Years of experience')
    experience_end = forms.CharField(label='Years of experience')
    description = forms.CharField(label='Job offer description', widget=forms.Textarea())
    location_city = forms.CharField(label='City')
    location_street = forms.CharField(label='Street')

    job_apply = forms.CharField(label='How to apply for a job')
    price = forms.IntegerField(label='Cena pojazdu')
    email = forms.CharField(label='Miasto')