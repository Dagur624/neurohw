import datetime

from . import models


def student_result_base(user, start_date, end_date=datetime.date.today()):
    student_tasks = models.StudentTask.objects.filter(student__user=user).filter(
            get_date__gte=start_date,
            get_date__lte=end_date)
    student_tasks_right = student_tasks.filter(is_right=True).count()
    student_tasks_wrong = student_tasks.filter(is_right=False).count()
    student_tasks_len = len(student_tasks)
    student_tasks_no_check = student_tasks_len - student_tasks_right - student_tasks_wrong
    return {
        'student_tasks_right': student_tasks_right,
        "student_tasks_wrong": student_tasks_wrong,
        'student_tasks_len': student_tasks_len,
        'student_tasks_no_check': student_tasks_no_check
    }