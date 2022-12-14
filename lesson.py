"""Git - это система контроля версий (записывает изменения файла или набора файлов в течении времени). 
Предназначен для отслеживани ведения истории изменений файлов в проекте. 
Благодаря GIT мы можем вернуть старую версию программы"""

"""GitHub - это онлайн-сервис, предоставляет услуги по хранению репозиториев и управление доступом"""

"""Команды"""
# git init -> инициализация нашего объекта (создает скрытую папку .git(в ней содержатся необходимые файлы нашего репозитория)) 

# git add (./<filename>) -> добавляет файлы с рабочей директории в промежуточное пространство (индекс- специальное промежуточное пространство, 
# в котором хранятся изменения файлов на пути от рабочей папки до репозитория)

# git commit -> добавляет все файлы которые находятся в индексе во внутреннюю базу данных и сохраняет их состояние на данный момент

# git remote add origin url(https/ssh) - добавляет удаленный репозиторий который находится на каком-нибудь сервере

# git push -u origin <branch name> - отправка кода в удаленный репозиторий 

# git branch - показывает список веток

# git branch <name of the branch> - создает ветку с названием <branch name>

# git checkout <branch name> - переключает на ветку <branch name>

# git pull origin <branch name> - стягиваем изменения с ветки <branch name> к себе на локалку

# git status - показывает статус проекта 

# git log - показывает журнал коммитов

# git clone ссылка_на_удаленный_репозиторий(url(ssh)) - склонировать\скопировать\скачать удаленный репозиторий


