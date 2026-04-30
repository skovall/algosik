# Лабораторная №4
**Выполнила Стецкова Алина, ИДБ-25-07**

### Сервис сокращения ссылок
Система должна уметь:
- сохранять длинную ссылку
- выдавать ей короткий код
- по короткому коду возвращать исходную ссылку

Пример работы:
- длинная ссылка: https://example.com/articles/python-basics
- короткий код: a1b2
- результат хранения: a1b2 -> https://example.com/articles/python-basics

### Обязательная часть
- Добавление новой ссылки (add_url)
- Получение длинной ссылки по короткому коду (get_url)
- Проверка существования короткого кода (exists)
- Вывод всех сокращённых ссылок (display_all)

```python
    def _generate_code(self, long_url):
        hash_object = hashlib.md5(long_url.encode())
        hash_hex = hash_object.hexdigest()
        code = hash_hex[:self.code_length]
        return code
    
    def _is_valid_url(self, url):
        pattern = re.compile(
            r'^https?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return pattern.match(url) is not None
    
    def add_url(self, long_url):
        if not self._is_valid_url(long_url):
            raise ValueError("Некорректный URL")
        
        short_code = self._generate_code(long_url)
        
        if short_code in self.url_mapping:
            if self.url_mapping[short_code] == long_url:
                return short_code
            else:
                self.code_length += 1
                short_code = self._generate_code(long_url)
        
        self.url_mapping[short_code] = long_url
        return short_code
    
    def get_url(self, short_code):
        if short_code in self.url_mapping:
            return self.url_mapping[short_code]
        return None
    
    def exists(self, short_code):
        return short_code in self.url_mapping
    
    def display_all(self):
        if not self.url_mapping:
            print("Сохранённых ссылок нет")
            return
        
        print("\n" + "="*80)
        print("Сохранённые ссылки:")
        print("="*80)
        for code, url in self.url_mapping.items():
            print(f"{code} -> {url}")
        print("="*80 + "\n")
```

### Вариативная часть (на выбор)
Реализовать 3 функцию:

*3. Добавить удаление ссылки по короткому коду*

### Дополнительные методы
```python
    def get_all_urls(self):
        if not self.url_mapping:
            return {}
        return self.url_mapping.copy()
    
    def get_stats(self):
        return {
            "total_links": len(self.url_mapping),
            "code_length": self.code_length
        }
```
