from django.db import models

# Для блога создали модели
# Для модели Category: Нужен только:
# CharField- в котором будет храниться название категории
class Category(models.Model):
    name = models.CharField(max_length=30)

# ПОЛЯ: title и body-Это те же типы полей, которые использовались в APP: project
class Post(models.Model):

    # Также нужен: CharField-для ЗАГОЛОВКА
    title = models.CharField(max_length=250)

    # Тело, т.е (body), должно быть длинным.
    # Поэтому мы используем: TextField()
    body = models.TextField()

    # Поля: created_on и last_modified, хранят объект:
    # DateTimeField-Содержащий дату и время, когда публикация была создана и изменена соответственно.
    # В строке 20: DateTimeField принимает аргумент: auto_now_add = True.
    # Он назначает текущую дату и время этому полю всякий раз, когда создаётся экземпляр этого класса.
    created_on = models.DateTimeField(auto_now_add=True)

    # В данной строчке аргумент: auto_now=True -
    # Назначает текущую дату и время этому полю всякий раз, когда экземпляр этого класса сохраняется.
    # Это означает, что когда вы редактируете экземпляр этого класса, date_modified обновляется.
    last_modified = models.DateTimeField(auto_now=True)

    # В данной строчке, происходит связка модели для категорий и сообщений, таким образом,
    # чтобы многие категории могли быть назначены многим сообщениям.
    # С помощью типа поля: ManyToManyField, поле связывает модели: Category и Post,
    # тем самым, позволяет создать связь между двумя таблицами
    categories = models.ManyToManyField('Category', related_name='posts')

# Последняя модель: Comment.
class Comment(models.Model):

    # Поле: author добавляет имя.
    author = models.CharField(max_length=70)

    # body- тело комментария.
    body = models.TextField()

    # Поле created_on, идентичное полю created_on в Post модели.
    created_on = models.DateTimeField(auto_now_add=True)

    # В данной строчке используется-реляционное поле ForeignKey.
    # Оно похоже на ManyToManyField, но вместо этого определяет отношение многие к одному.
    # Это объясняется тем, что одному сообщению можно назначить множество комментариев.
    # Но нельзя иметь комментарий, который соответствует многим постам.
    # Поле ForeignKey принимает два аргумента.
    # Первый аргумент – это другая модель в отношениях, в данном случае Post.
    # Второй аргумент: говорит Django, что делать, когда сообщение удалено.
    # Если сообщение удалено, то мы не хотим, чтобы комментарии, связанные с ним, торчали.
    # Поэтому мы хотим также удалить их, поэтому добавим аргумент on_delete=models.CASCADE.
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

# После того как модели созданы, создаём файлы миграции с помощью:
# python manage.py makemigrations blog; python manage.py migrate
