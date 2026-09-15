import random

def create_valid_note():
    return {
        "title": "Тестовая заметка",
        "content": "Содержание заметки"
    }

def create_invalid_note():
    return {
        "content": "Заметка без заголовка"
    }

def create_updated_note():
    return {
        "title": "Обновлённая заметка",
        "content": "Текст после редактирования"
    }