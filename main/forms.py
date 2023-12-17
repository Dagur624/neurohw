from allauth.account.forms import SignupForm
from . import models
from django import forms

class CustomSignupForm(SignupForm):
    phone = forms.CharField(max_length=12, label='Телефон (опционально)', required=False)
    user_type = forms.ModelChoiceField(queryset=models.UserType.objects.all(), label="Тип пользователя")
    #user_school_code = forms.CharField(max_length=255, label="Код, выданный школой")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.phone_number = self.cleaned_data['phone']
        user.user_type = self.cleaned_data["user_type"]
        #user.user_school.code = self.cleaned_data["user_school_code"]
        user.save()
        return user
    
    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'user_type', 'phone_number', "user_school_code",)

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ("__all__")

class GiveTaskForm(forms.ModelForm):
    students = forms.MultipleChoiceField(label="Ученики", choices= models.Student.objects.values_list('id', 'user__first_name'))
    class Meta:
        model = models.StudentTask
        fields = ("task", "limite_date")

class CheckTaskForm(forms.ModelForm):
    class Meta:
        model = models.StudentTask
        fields = ("is_right", "teaher_comment")

class DoTaskForm(forms.ModelForm):
    class Meta:
        model = models.StudentTask
        fields = ("student_answer",)
        labels = {
            "student_answer": "Введите ответ:"
        }

