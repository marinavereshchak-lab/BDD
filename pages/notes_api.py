import requests
BASE_URL = "http://127.0.0.1:8000"

class NotesAPI:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def get_all_notes(self):
        response = requests.get(f"{self.base_url}/notes")
        return response

    def create_note(self, payload: dict):
        response = requests.post(f"{self.base_url}/notes", json=payload)
        return response

    def get_note_by_id(self, note_id):
        response = requests.get(f"{self.base_url}/notes/{note_id}")
        return response

    def update_note(self, note_id, title, content):
        payload = {"title": title, "content": content}
        response = requests.put(f"{self.base_url}/notes/{note_id}", json=payload)
        return response

    def delete_note(self, note_id):
        response = requests.delete(f"{self.base_url}/notes/{note_id}")
        return response
