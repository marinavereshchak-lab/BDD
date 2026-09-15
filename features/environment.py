from pages.notes_api import NotesAPI

def before_all(context):
    context.api = NotesAPI()