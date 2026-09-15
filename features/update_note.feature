Feature: Update a note by ID

  Scenario: Update a note with a valid ID
    Given a valid note payload
    When I send a request to create the note

    Given an updated note payload
    When I send a request to update the last created note with the updated payload
    Then the response status code should be 200
    And the response should contain the correct title "Обновлённая заметка"
    And the response should contain the correct content "Текст после редактирования"

  Scenario: Try to update a note with an invalid ID

    Given an updated note payload
    When I send a request to update the note with id "999999" using the current payload
    Then the response status code should be 404
