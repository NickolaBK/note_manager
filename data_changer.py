import datetime
created_date = datetime.date.today() # текущая дата
print(f"Дата создания заметки в формате \"дд-мм-гггг\":{created_date.strftime("%d-%m-%Y")}") # выводим дату в нужный формат
issue_date = input("Дата истечения заметки в формате \"дд-мм-гггг\":") # получаем от пользователя дату
issue_date = (datetime.datetime.strptime(issue_date, "%d-%m-%Y")) # конвертируем дату в объект
print(str(created_date))
print(str(issue_date))

