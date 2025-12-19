import json   #зависимось JSON — это формат данных, похожий на словарь Python.
from bs4 import BeautifulSoup   #зависимость инструмент для разбора HTML (веб-страниц)

# Здесь указываем, как найти карточки со статьями на странице
CARD_SELECTOR = ".popular-article-wrap" #это CSS-селектор как адрес. 
#Говорит программе: "Ищи на странице все элементы с классом popular-article-wrap"
TITLE_SELECTOR = ".popular-title" #В каждой найденной карточке ищи элемент с классом popular-title".
BASE_URL = "https://pedsovet.org" #базовый адрес сайта. Нужен, чтобы превращать относительные ссылки в полные.
INPUT_FILE = "page.html" #имя файла с сохранённой веб-страницей, который будем читать.


def read_html_file(filename): #создаём функцию с именем read_html_file, которая принимает filename (имя файла).
    #Просто открываем файл и читаем его содержимое
    with open(filename, 'r', encoding='utf-8') as file: 
        #with open(filename, 'r', encoding='utf-8') as file: — открываем файл.
#filename — какой файл открыть (например, "page.html")
#'r' — режим read (только чтение)
#encoding='utf-8' — кодировка (чтобы русские буквы отображались правильно)
#as file: — называем открытый файл переменной file
        return file.read()  #читаем всё содержимое файла и возвращаем его как одну большую строку.


def parse_articles(file_content):
    #Ищем все карточки статей и достаём из них названия и ссылки
    soup = BeautifulSoup(file_content, 'html.parser') #создаём объект BeautifulSoup из HTML-кода. 
    #Теперь soup — это "умная" версия HTML, с которой удобно работать.
    cards = soup.select(CARD_SELECTOR) #ищем ВСЕ карточки статей на странице. select ищет по CSS-селектору ".popular-article-wrap". 
    #Результат — список найденных элементов.
    results = [] #Создаём пустой список, куда будем складывать найденные статьи
    
    # Проходимся по каждой карточке
    for card in cards: #Начинаем перебирать каждую найденную карточку по одной.
        link_elem = card.select_one(TITLE_SELECTOR) #щем внутри карточки ОДИН элемент с классом popular-title. 
        #Если их несколько, берётся первый.
        if not link_elem: 
            continue #пропускаем эту карточку и переходим к следующей.
        
        # Берём текст (название статьи) и ссылку
        title = link_elem.get_text(strip=True) #получаем текст из элемента.
        href = link_elem.get('href', '')
        
        # Если ссылка относительная (начинается с /), добавляем базовый домен
        if href.startswith('/'):
            href = BASE_URL + href
        
        # Сохраняем результат
        results.append({
            "title": title,
            "link": href
        })
    
    return results


def main():
    """Основная функция - здесь всё запускается"""
    html_content = read_html_file(INPUT_FILE)
    results = parse_articles(html_content)
    
    # Выводим результат в формате JSON
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
