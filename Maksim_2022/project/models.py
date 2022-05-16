from django.db import models

# Создали модель, с именем: project, для таблицы в базе данных, в которой будет 4 колонки:
# 1)title, 2)description, 3)technology, 4)image
class Project(models.Model):
    # Создали поле: title
    # Заголовок не может быть больше 100 символов.
    title=models.CharField(max_length=100)
    # Создали ещё одно поле: description
    description=models.TextField()
    # Ещё одно поле: technology
    technology=models.CharField(max_length=50)
    # И последнее поле: image
    # Поле с файлом каким-то будет храниться и этот файл будет сохранён в папку: img
    image=models.FileField(upload_to='img/')