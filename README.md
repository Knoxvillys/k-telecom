

Для того, чтобы выполнить миграцию бд, выполните команды:
```
docker-compose run web python manage.py makemigrations
```

```
docker-compose run web python manage.py migrate
```
Для запуска : 

```
docker-compose up
```


Вывод оборудования
```
GET:/api/equipment
```

Вывод оборудования по id 
```
GET:/api/equipment/{id}
```

Создание новых записей
```
POST:/api/equipment
```

Редактирование
```
PUT:/api/equipment/{id}
```

Удаление
```
DELETE:/api/equipment/{id}
```

Редактирование
```
PUT:/api/equipment/{id}
```
