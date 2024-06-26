from allauth.account.forms import SignupForm
from . import models
from django import forms


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=255, label="Реальное имя", widget=forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}))
    last_name = forms.CharField(max_length=255, label="Фамилия", widget=forms.TextInput(attrs={'placeholder': 'Введите вашу фамилию'}))
    phone = forms.CharField(max_length=12, label='Телефон (опционально)', required=False, widget=forms.TextInput(attrs={'placeholder': 'Введите ваш телефон'}))
    user_type = forms.ModelChoiceField(queryset=models.UserType.objects.all(), label="Тип пользователя")
    grade = forms.ModelChoiceField(queryset=models.Grade.objects.all(), label="Класс", required=False)

    # user_school_code = forms.CharField(max_length=255, label="Код, выданный школой")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.phone_number = self.cleaned_data['phone']
        user.user_type = self.cleaned_data["user_type"]
        # user.user_school.code = self.cleaned_data["user_school_code"]
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
    students = forms.MultipleChoiceField(label="Ученики",
                                         choices=models.Student.objects.values_list('id', 'user__first_name'))

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


class ResultDateForm(forms.Form):
    start_date = forms.DateField(label="Начальная дата поиска", widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))
    end_date = forms.DateField(label="Конечная дата поиска", widget=forms.widgets.DateInput(
        attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}))


class GenerateForm(forms.ModelForm):
    class Meta:
        model = models.AIRequests
        fields = ("request",)

    def __init__(self, *args, **kwargs):
        super(GenerateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control '
