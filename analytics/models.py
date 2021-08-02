from django.db import models

# user - пользователь в отношении которого производится анализ

#Таблица которая хрнаит аккаунты для подключения к инстаботу
class Account(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    comment = models.TextField(default='')

    def __str__(self):
        return self.login


#Таблица которая отображает аналитику по пользователям
class AnalyticRecord(models.Model):
    account = models.ForeignKey('Account', on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    date = models.DateField()


#Таблица которая хранит информацию о подписках пользователя 
#в отношении которого производится аналитика
class UserSubscriber(models.Model):
    pass


#Таблица которая хранит информацию о подписчиках пользователя
class UserSubscripaion(models.Model):
    pass


#Таблица которая хранит информацию о лайках пользователя на страницах других пользователей
class UserLike(models.Model):
    pass


#Таблица котораях хранит информацию о лайках пользователей на
# странице пользователя в отношении которого производится аналитика
class UserLikes(models.Model):
    pass


#Таблица которая хранит информацию о комментариях пользователя на страницах других пользователей
class UserComment(models.Model):
    pass

#Таблица которая хранит информацию о комментариях пользователей на странице пользователя
class UserComments(models.Model):
    pass