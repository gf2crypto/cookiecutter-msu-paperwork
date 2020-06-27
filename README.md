# cookiecutter-msu-paperwork

Репозиторий содержит `cookiecutter` ([more details](https://cookiecutter.readthedocs.io/en/latest/)) LaTeX-шаблон для различных письменных работ студентов (курсовых работ, выпускных квалификационных работ бакалавров, магистерских диссертаций и т.п.).

Шаблон адаптирован для студентов кафедры информационной безопасности факультета вычислительной математики и кибернетики. Однако он имеет достаточно гибкие настройки и может быть сравнительно легко приспособлен для других кафедр, факультетов и университетов.

__Как использовать шаблон__:
1. Установите `python` и `git`;
2. Установите приложение `cookiecutter`, выполнив в командной строке следующую команду:
   ```bash
   pip install cookiecutter
   ```
4. Для инициализации нового проекта выполните в командной строке:
   ```bash
   cookiecutter https://github.com/gf2crypto/cookiecutter-msu-paperwork.git
   ```
5. Параметры:
     - **project_name**, имя проекта (поддерживается только латиница);
     - **create_gitignore**, требуется ли создать `.gitignore` файл для использования системы контроля версий `git`: 'yes' или 'no'.
6. Для компиляции документа можно использовать команду `make build` (`make.bat build` под `Windows`).

__Установка вручную__:
1. Скачайте или клонируйте с помощью `git clone https://github.com/gf2crypto/cookiecutter-msu-paperwork.git` проект в любую папку.
2. Переместите папку `{{cookiecutter.project_name}}`, переименовав её нужным образом.
3. Замените все вхождения строки `{{cookiecutter.project_name}}` во всех файлах и именах файлов на имя проекта.
4. Удалите файл `options.json`.
5. Если используете систему контроля версий, то рекомендуется переименовать `gitignore` в `.gitignore`; в противном случае просто удалите этот файл.
6. Для компиляции документа можно использовать команду `make` (`make.bat` под `Windows`).

Шаблон поддерживает только `TeXLive` (`MacTeX`) версию `TeX`, так как make файлы используют `latexmk` для компиляции документа. Рекомендуется устанавливать __полную__ версию `LaTeX`, чтобы сэкономить время на отладке и доустановке пакетов!

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a [Creative Commons Attribution 4.0 International
License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
