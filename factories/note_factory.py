import random
import string

def create_valid_note():
    return {
        "title": "Тестовая заметка",
        "content": "Содержание заметки"
    }

def create_random_note():
    suffix = ''.join(random.choices(string.ascii_lowercase, k=6))
    return {
        "title": f"Заметка_{suffix}",
        "content": f"Контент_{suffix}"
    }

def create_invalid_note():
    return {
        "title": "",
        "content": ""
    }

def create_updated_note():
    return {
        "title": "Обновлённая заметка",
        "content": "Текст после редактирования"
    }