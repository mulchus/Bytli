# Bitly URL shortener

1. The script is designed to create a short link based on the long link you entered as an argument (data)

2. Also, the script, when entering a previously created short link, shows the number of clicks that have already
been made on this short link at the moment


### How to install

Python3 should already be installed. 
Then use pip (or pip3, there is a conflict with Python2) to install dependencies.
Open the command line with the Win + R keys and enter:
```
pip install -r requirements.txt
```
It is recommended to use virtualenv/venv to isolate the project.
(https://docs.python.org/3/library/venv.html)


### Setting environment variables

Before starting, you need to create a file ".env" in PATH_TO_THE_FOLDER_WITH_SCRIPT\ 
and configure the environment variables by writing in it:
```
BITLY_TOKEN = 'Your token for the API of the bit ly service',
```
which is located in the personal account of the bitly service at the link:
```
https://app.bitly.com/settings/api/
```


### The command to run the script looks like this:
```
python PATH_TO_THE_FOLDER_WITH_SCRIPT\маіп.ру [-h] url
```
where, 

 -h, --help - view a short script help page
 
 url - long link (starting with http(s)://) or previously created short link (bitlink)
 
If you have installed a virtual environment, then the command must be entered without a path to the script.

#### Example 1:
```
python c:\PythonProjects\Bytli\main.py https://www.np-ciz.ru
```
The result of the script execution:
Bitlink: bit.ly/3w1xPGj

#### Example 2:
```
python c:\PythonProjects\Bytli\main.py bit.ly/3w1xPGj
```
The result of the script execution:
By the link bit.ly/3w1xPGj clicked 3 times(a)


### Project Goals
This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).




# Обрезка ссылок с помощью Битли

1. Скрипт предназначен для создания короткой ссылки на основании введенной вами в качестве аргумента (данных) 
длинной ссылки
  
2. Также скрипт при вводе ранее созданной короткой ссылки показывает количество переходов, которое на данный момент уже
осуществлялось по данной короткой ссылке


### Как установить?

Python3 должен быть уже установлен. 
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей.
Открываем командную строку клавишами Win+R и вводим:
```
pip install -r requirements.txt
```
Рекомендуется использовать virtualenv/venv для изоляции проекта.
(https://docs.python.org/3/library/venv.html)


### Настройка переменных окружения

До запуска необходимо создать файл ".env" в папке ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\
и настроить переменные окружения, прописав в нем:
```
BITLY_TOKEN = 'Ваш токен для API сервиса bitly', 
```
который расположен в личном кабинете сервиса bitly по ссылке:
```
https://app.bitly.com/settings/api/
```


### Команда на запуск скрипта выглядит так:
```
python ПУТЬ_К_ПАПКЕ_СО_СКРИПТОМ\main.py [-h] url
```
где,

  -h, --help - просмотр короткой страницы помощи по скрипту
  
  url - длинная ссылка (начиная с http(s)://) или ранее созданная короткая ссылка (bitlink)

Если вы установили виртуальное окружение, то команда надо вводить без пути к скрипту
  
#### Пример 1:
```
python c:\PythonProjects\Bytli\main.py https://www.np-ciz.ru
```
Результат выполнения скрипта:
Битлинк:  bit.ly/3w1xPGj

#### Пример 2:
```
python c:\PythonProjects\Bytli\main.py bit.ly/3w1xPGj
```
Результат выполнения скрипта:
По ссылке bit.ly/3w1xPGj перешли 3 раз(а)


### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
