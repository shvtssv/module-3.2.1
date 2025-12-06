import json
from bs4 import BeautifulSoup

# Здесь указываем, как найти карточки со статьями на странице
CARD_SELECTOR = ".popular-article-wrap"
TITLE_SELECTOR = ".popular-title"
BASE_URL = "https://pedsovet.org"
INPUT_FILE = "page.html"


def read_html_file(filename):
    """Просто открываем файл и читаем его содержимое"""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def parse_articles(file_content):
    """Ищем все карточки статей и достаём из них названия и ссылки"""
    soup = BeautifulSoup(file_content, 'html.parser')
    cards = soup.select(CARD_SELECTOR)
    results = []
    
    # Проходимся по каждой карточке
    for card in cards:
        link_elem = card.select_one(TITLE_SELECTOR)
        if not link_elem:
            continue
        
        # Берём текст (название статьи) и ссылку
        title = link_elem.get_text(strip=True)
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
