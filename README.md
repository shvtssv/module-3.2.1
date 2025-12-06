# Парсер статей

Программа читает HTML-файл и извлекает заголовки и ссылки статей.

## Что делает программа

1. Читает HTML-файл
2. Находит карточки статей
3. Извлекает заголовок и ссылку
4. Выводит результат в JSON

## Файлы проекта

- **parse_pedagogy.py** — основной скрипт
- **requirements.txt** — необходимые библиотеки
- **.gitignore** — игнорируемые файлы
- **page.html** — HTML-файл (нужно скачать)

## Как получить HTML-файл

1. Откройте https://pedsovet.org/ в браузере
2. Откройте страницу со статьями
3. Сохраните страницу как `page.html` в папку с программой
   - Правый клик → "Сохранить как"
   - Формат: "Веб-страница, только HTML"

## Установка

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск программы

1. Убедитесь, что `page.html` в той же папке

2. Активируйте виртуальное окружение:

   **macOS / Linux:**

   ```bash
   source venv/bin/activate
   ```

   **Windows:**

   ```bash
   venv\Scripts\activate
   ```

3. Запустите:
   ```bash
   python parse_pedagogy.py
   ```

## Пример вывода

```json
[
  {
    "title": "Права воспитателя детского сада по закону",
    "link": "https://pedsovet.org/article/prava-vospitatelya-detskogo-sada-po-zakonu"
  },
  {
    "title": "Нагрузка учителя в 2025 году: как влияет на оплату",
    "link": "https://pedsovet.org/article/nagruzka-ucitela-v-2025-godu-kak-vliaet-na-oplatu"
  }
]
```
