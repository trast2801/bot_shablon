# bot_shablon

Шаблон бота предназначен, в качестве модели, которую позже можно адаптировать под нужды Заказчика. 
В нем реализован функционал торового бота с использованием библиотеки aiogramm. Работа с БД, корзина покупателя, оформлдение заказа. 

# структура проекта
data - содержит каталог с хранением изображений товара, и самой БД
res - файлы фильтрующие материные слова 
main.py - основной файл бота, регистрация и запуск
setting 
  config.py - конфигурационный файл, токен, логирование, подключение БД
  view.py - сообщения которые выводяться из simple.py

    ---- handlers -  
          events.py - процедуры обслуживающие старт/стоп бота и подключение пользователя
          filter_words.py - цензура ругательств пользователя, 
          send_files.py -  отправка и получения файла по запросу пользователя
    ---- utils -         
          commands.py - описание и регистрация команд бота. Два раздела: при работе с ботом индивидуально и при работе бота в общем чате
          simple.py - отображение сообщений бота
          statesform.py - машина состояний пользователя
          
