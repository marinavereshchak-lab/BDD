Feature: Get a single note by ID

  Scenario: Get a note with a valid ID
    Given a valid note payload
    When  I send a request to create the note
    When I send a request to get the last created note
    Then the response status code should be 200
    And the response should contain the correct title "Тестовая заметка"
    And the response should contain the correct content "Содержание заметки"

  Scenario: Try to get a note with an invalid ID
    When I send a request to get the note with id "999999"
    Then the response status code should be 404