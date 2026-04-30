from url_shortener import URLShortener


def main():
    shortener = URLShortener()
    
    print("=== Добавление ссылок ===\n")
    
    url1 = "https://www.python.org/downloads"
    code1 = shortener.add_url(url1)
    print(f"Длинная ссылка: {url1}")
    print(f"Короткий код: {code1}\n")
    
    url2 = "https://github.com/features/copilot"
    code2 = shortener.add_url(url2)
    print(f"Длинная ссылка: {url2}")
    print(f"Короткий код: {code2}\n")
    
    url3 = "https://docs.python.org/3/library/hashlib.html"
    code3 = shortener.add_url(url3)
    print(f"Длинная ссылка: {url3}")
    print(f"Короткий код: {code3}\n")
    
    url4 = "https://stackoverflow.com/questions/tagged/python"
    code4 = shortener.add_url(url4)
    print(f"Длинная ссылка: {url4}")
    print(f"Короткий код: {code4}\n")
    
    print("=== Вывод всех ссылок ===")
    shortener.display_all()
    
    print("=== Получение длинной ссылки по короткому коду ===")
    test_code = code1
    long_url = shortener.get_url(test_code)
    if long_url:
        print(f"Код '{test_code}' -> {long_url}\n")
    else:
        print(f"Код '{test_code}' не найден\n")
    
    print("=== Проверка существования кода ===")
    print(f"Существует ли код '{code2}'? {shortener.exists(code2)}")
    print(f"Существует ли код 'xyz9'? {shortener.exists('xyz9')}\n")
    
    print("=== Удаление ссылки ===")
    print(f"Удаляем код '{code3}'")
    success = shortener.delete_url(code3)
    if success:
        print(f"Ссылка с кодом '{code3}' удалена\n")
    else:
        print(f"Не удалось удалить код '{code3}'\n")
    
    print("=== Ссылки после удаления ===")
    shortener.display_all()
    
    print("=== Попытка получить удалённую ссылку ===")
    deleted_url = shortener.get_url(code3)
    if deleted_url is None:
        print(f"Код '{code3}' не найден\n")
    
    print("=== Статистика ===")
    stats = shortener.get_stats()
    print(f"Всего ссылок: {stats['total_links']}")
    print(f"Длина короткого кода: {stats['code_length']}\n")
    
    print("=== Обработка ошибок ===")
    try:
        invalid_url = "not-a-valid-url"
        shortener.add_url(invalid_url)
    except ValueError as e:
        print(f"Ошибка: {e}\n")
    
    print("=== Удаление несуществующего кода ===")
    result = shortener.delete_url("nonexistent")
    print(f"Удаление несуществующего кода: {result}\n")
    
    print("=== Повторное добавление той же ссылки ===")
    same_code = shortener.add_url(url1)
    print(f"Исходный код: {code1}")
    print(f"Полученный код: {same_code}")
    print(f"Коды совпадают: {code1 == same_code}")


if __name__ == "__main__":
    main()
