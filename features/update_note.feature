Feature: Update a note by ID

  Scenario: Update a note with a valid ID
    Given there is a note with title "Старая заметка" and content "Старый контент"
    When I send a request to create the note

    When I send a request to update the note with id "{last_note_id}" to title "Новая заметка" and content "Новый контент"
    Then the response status code should be 200
    And the response should contain the correct title "Новая заметка"
    And the response should contain the correct content "Новый контент"

  Scenario: Try to update a note with an invalid ID

    When I send a request to update the note with id "999999" to title "Любая заметка" and content "Любой контент"
    Then the response status code should be 404