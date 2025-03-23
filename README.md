# HosteyPic [RU]
**MIRRORED FROM [GITLAB REPOSITORY](https://gitlab.com/OnBell/hosteypic)**

HosteyPic — это веб-приложение, которое позволяет пользователям делиться своими изображениями и находить вдохновение в работах других. Пользователи могут легко загружать свои работы, а также просматривать и оценивать творчество, загруженное другими пользователями.

Приложение предлагает удобный интерфейс для поиска интересных изображений по тексту, что позволяет быстро находить то, что вам нужно. Кроме того, у каждого пользователя есть возможность сохранять понравившиеся картинки в своем аккаунте или скачивать их на устройство.

С HosteyPIC вы сможете не только делиться своим творчеством, но и вдохновляться работами других, создавая уникальное сообщество любителей искусства!

Применяемые технологии:
* FastAPI
* Vue.js (сборщик Vite)
* PostgreSQL

Дополнительно:
* Docker
* MTA Postfix
* Nginx

# Дизайн
Дизайн в Figma: https://www.figma.com/design/QbEvjsL7XaaLD1h40qvyTh

Зеркало: https://www.figma.com/design/DSyShlF0uJwIiiJcHUFgNH

Дизайн-проект также доступен в папке __docs__.

# Развертывание
Для локального развертывания используется compose-файл __docker-compose-dev.yml__ (Команда _docker-compose -f docker-compose-dev.yml up_).

Развертывание на сервере через __docker-compose-dev.yml__. При условии настройки .env файла, наличия конфигурационных файлов для postfix и ngnix (опционально). Потребуется самостоятельная настройка фаервола.

# Разработка
В back-end составляющей применяется менеджер Poetry, установка зависимостей — через команду _poetry install_, наличие env/venv рекомендуется в локальной папке проекта. Запуск вне docker-среды — через команду _uvicorn hosteypic_server.main:app --host 0.0.0.0 --reload_. Перед этим применить миграции alembic, требуется инстанс PostgreSQL.

Для front-end требуется наличие node.js и vue.js. Установка зависимостей — через команду _npm install_. Для развертывания вне среды docker использовать http-server (_npm install http-server_).

# Документация
Документация доступна в папке __docs__. Актуальные версии документации находятся в ветке __docs__. Также имеются wiki-страницы с инструкциями.

# Наша команда

* Forkenn ([@OnBell](https://gitlab.com/OnBell "GitLab"), [@forkenn](https://github.com/forkenn "GitHub")) - team lead, back-end dev, sysadmin.
* cerega123 ([@cerega123](https://gitlab.com/cerega123)) - front-end dev.
* AnTiAl TM ([@kolumbia101](https://gitlab.com/)) - designer.
* ru4sdevil ([@ru4sdevil](https://gitlab.com/ru4sdevil)) - documenter.
* Yury Generalov ([@yury_kustik](https://gitlab.com/yury_kustik)) - tester.

# HosteyPic [EN]
**MIRRORED FROM [GITLAB REPOSITORY](https://gitlab.com/OnBell/hosteypic)**

HosteyPic is a web application that allows users to share their images and find inspiration in the work of others. Users can easily upload their own work, as well as view and rate the creativity uploaded by other users.

The app offers an easy-to-use interface to search for interesting images by text, allowing you to quickly find what you need. In addition, each user has the option to save their favorite pictures in their account or download them to their device.

With HosteyPic you can not only share your art, but also be inspired by the works of others, creating a unique community of art lovers!

Technologies used:
* FastAPI
* Vue.js (Vite tool)
* PostgreSQL

Additionally:
* Docker
* MTA Postfix
* Nginx

# Design
Figma: https://www.figma.com/design/QbEvjsL7XaaLD1h40qvyTh

Mirror: https://www.figma.com/design/DSyShlF0uJwIiiJcHUFgNH

The design project is also available in the folder __docs__.

# Deployment
For local deployment, the __docker-compose-dev.yml__ compose file is used (command _docker-compose -f docker-compose-dev.yml up_).

Deploy to the server via __docker-compose-dev.yml__. Setting up the .env file, having configuration files for postfix and ngnix (optional) is important. Self-configuration of firewall will be required.

# Development
The Poetry manager is used in the back-end component, dependencies are installed via the _poetry install_ command, env/venv availability is recommended in the local project folder. Run outside the docker environment via the command _uvicorn hosteypic_server.main:app --host 0.0.0.0.0 --reload_. Before applying alembic migrations, a PostgreSQL instance is required.

Front-end requires node.js and vue.js. Install dependencies via the _npm install_ command. For deployment outside the docker environment, use http-server (_npm install http-server_).

# Documentation
Documentation is available in the __docs__ folder. Wiki pages with instructions are also available.

# Our Team

* Forkenn ([@OnBell](https://gitlab.com/OnBell "GitLab"), [@forkenn](https://github.com/forkenn "GitHub")) - team lead, back-end dev, sysadmin.
* cerega123 ([@cerega123](https://gitlab.com/cerega123)) - front-end dev.
* AnTiAl TM ([@kolumbia101](https://gitlab.com/)) - designer.
* ru4sdevil ([@ru4sdevil](https://gitlab.com/ru4sdevil)) - documenter.
* Yury Generalov ([@yury_kustik](https://gitlab.com/yury_kustik)) - tester.
