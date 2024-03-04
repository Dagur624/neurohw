from main.models import Theme, Subject, Grade, Lesson
import g4f
import json

g4f.debug.logging = True  # Enable debug logging
g4f.debug.version_check = False  # Disable automatic version checking


class GPT:
    SERVICE_PROMT_THEME = """
        Отвечай в формате JSON вида
        {"response": [ 
        {"name": русский текст, "code": На англиском без пробелов, "grade": Класс}]}
    """

    SERVICE_PROMT_LESSON = """
        Представь что ты учитель и ведешь уроки в школе
        и тебе надо объяснить тему ученику, 
    """

    PROMT_MAIN_THEME = """
        Выведи полный список тем по {subject} за {grade} класс по госту в Российской федерации 
    """

    PROMT_SECOND_THEME = """
        Выведи полный список подтем для темы {theme} по {subject} за {grade} класс по госту в Российской федерации 
    """

    PROMT_LESSON = """
        Раскрой тему (с примерами) {theme} из главной темы {parent_theme} для {grade} класс 
        """
    PROMT_LESSON_2 = """
    Мне нужна помощь в генерации обучающего материала по {theme} из темы {parent_theme} за для {grade} класс школьников. 
    Я предпочитаю формат обучающих материалов с примерами, и ожидаю от 4000 символов. 
    Помоги мне создать информативный и понятный материал, 
    учитывая мои требования или предпочтения.И начинай сразу с темы
    """
    def ask_gpt_json(self, text, promt=SERVICE_PROMT_THEME):
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo_16k,
            messages=[
                {"role": "system", "content": promt},
                {"role": "user", "content": text}],

        )
        response = response.replace("'", '"')
        print(response)
        data = json.loads(response)
        if "response" in data:
            data = data["response"]
        return data

    def ask_gpt_text(self, text, promt=SERVICE_PROMT_LESSON):
        print(text)
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_35_turbo_16k,
            messages=[
                {"role": "system", "content": promt},
                {"role": "user", "content": text}],

        )
        print(response)
        return response

    def ask_gpt_ignore_error(self, text, promt=None):
        data = None
        while True:
            try:
                data = self.ask_gpt_json(text, promt)
                break
            except:
                break
        return data

    def get_main_themes(self):
        for i in range(3, 11):
            grade = str(i)
            subject = 'Математика'
            query = self.PROMT_MAIN_THEME.replace('{subject}', subject)
            query = query.replace('{grade}', grade)
            response = self.ask_gpt_ignore_error(query)
            print(response)
            subject, _ = Subject.objects.get_or_create(name='Математика', code='math')
            for theme in response:
                theme = Theme(name=theme.get('name'), code=theme.get('code'), subject=subject, grade=i)
                theme.save()

    def get_second_theme(self):
        themes = Theme.objects.all()
        for theme in themes[0:4]:
            query = self.PROMT_SECOND_THEME.replace('{theme}', theme.name)
            query = query.replace('{grade}', str(theme.grade))
            query = query.replace('{subject}', str(theme.subject))
            response = self.ask_gpt_ignore_error(query)
            for second_theme in response:
                second_theme = Theme(name=second_theme.get('name'),
                                     code=second_theme.get('code'),
                                     subject=theme.subject,
                                     grade=theme.grade,
                                     parent_id=theme.id
                                     )
                second_theme.save()

    def create_lesson(self):
        themes = Theme.objects.exclude(parent_id=None).reverse()
        for theme in themes:
            query = self.PROMT_LESSON.replace('{theme}', theme.name)
            query = query.replace('{parent_theme}', str(theme.parent.name))
            query = query.replace('{grade}', str(theme.grade))
            response = ''
            for i in range(6):
                try:
                    response = self.ask_gpt_text(query, promt=self.PROMT_LESSON_2)
                    break
                except:
                    continue
            lesson = Lesson(title=theme.name, text=response, theme=theme)
            lesson.save()


def run():
    gpt = GPT()
    #gpt.get_main_themes()
    #gpt.get_second_theme()
    gpt.create_lesson()


