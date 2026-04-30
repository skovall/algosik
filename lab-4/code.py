import hashlib
import re

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.code_length = 4
    
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
    
    def delete_url(self, short_code):
        if short_code in self.url_mapping:
            del self.url_mapping[short_code]
            return True
        return False
    
    def get_all_urls(self):
        if not self.url_mapping:
            return {}
        return self.url_mapping.copy()
    
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
    
    def get_stats(self):
        return {
            "total_links": len(self.url_mapping),
            "code_length": self.code_length
        }
