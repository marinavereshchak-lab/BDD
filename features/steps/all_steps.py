from behave import then, given, when
from pages.notes_api import NotesAPI
from factories.note_factory import (create_valid_note, create_invalid_note, create_updated_note)


@given('a valid note payload')
def step_prepare_valid_payload(context):
    context.payload = create_valid_note()

@given('an invalid note payload')
def step_prepare_invalid_payload(context):
    context.payload = create_invalid_note()

@given('an updated note payload')
def step_prepare_updated_payload(context):
    context.payload = create_updated_note()

@given('all notes are deleted')
def step_delete_all_notes(context):
    resp = context.api.get_all_notes()
    notes = resp.json()
    if not notes:
        return
    for note in notes:
        note_id = note["id"]
        resp_del = context.api.delete_note(note_id)

@when('I send a request to create the note')
def step_send_create_request(context):
    context.response = context.api.create_note(payload=context.payload)
    if context.response.status_code in [200, 201]:
        body = context.response.json()
        context.last_note_id = body["id"]
    else:
        context.last_note_id = None

@when('I send a request to get the last created note')
def step_send_get_last_note(context):
    if not hasattr(context, 'last_note_id'):
        raise AssertionError("Сначала нужно создать заметку!")
    note_id = context.last_note_id
    context.response = context.api.get_note_by_id(note_id)

@when('I send a request to get the note with id "{note_id}"')
def step_send_get_note_by_id(context, note_id):
    context.response = context.api.get_note_by_id(note_id)

@when('I send a request to get the list of notes')
def step_send_get_notes(context):
    context.response = context.api.get_all_notes()

@when('I send a request to delete the last created note')
def step_send_delete_last_note(context):
    if not hasattr(context, 'last_note_id'):
        raise AssertionError("Сначала нужно создать заметку, чтобы у неё появился ID!")

    note_id = context.last_note_id
    context.response = context.api.delete_note(note_id)

@when('I send a request to delete the note with id "{note_id}"')
def step_send_delete_note_by_id(context, note_id):
    context.response = context.api.delete_note(note_id)

@when('I send a request to update the last created note with the updated payload')
def step_send_update_with_payload(context):
    if not hasattr(context, 'last_note_id') or context.last_note_id is None:
        raise AssertionError(
            "Сначала нужно создать заметку! В контексте нет last_note_id."
        )

    note_id = context.last_note_id
    payload = context.payload

    context.response = context.api.update_note(note_id, payload["title"], payload["content"])

@when('I send a request to update the note with id "{note_id}" using the current payload')
def step_send_update_by_id_with_payload(context, note_id):
    payload = context.payload
    context.response = context.api.update_note(note_id, payload["title"], payload["content"])

@then('the response status code should be {status_code:d}')
def step_check_status(context, status_code):
    assert context.response.status_code == status_code, \
        f"Ожидали статус {status_code}, а получили {context.response.status_code}"

@then('the response should contain the correct title "{title}"')
def step_check_title(context, title):
    body = context.response.json()
    assert body["title"] == title, \
        f"Ожидали title '{title}', а получили '{body['title']}'"


@then('the response should contain the correct content "{content}"')
def step_check_content(context, content):
    body = context.response.json()
    assert "content" in body, f"В ответе нет поля 'content'. Ответ: {body}"
    assert body["content"] == content, \
        f"Ожидали content '{content}', а получили '{body['content']}'"

@then('the response should contain an empty list of notes')
def step_check_empty_list(context):
    body = context.response.json()
    assert isinstance(body, list), "Ожидался список, а пришло что-то другое"
    assert len(body) == 0, f"Список не пустой: {body}"

@then('the response should contain a list with at least one note')
def step_check_non_empty_list(context):
    body = context.response.json()
    assert isinstance(body, list), "Ожидался список"
    assert len(body) >= 1, f"Список пуст, хотя должна быть заметка. Получено: {body}"
