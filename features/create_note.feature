Feature: Create a note

  Scenario: Successfully create a note
    Given there is a note with title "Тестовая заметка" and content "Содержание заметки"
    When I send a request to create the note
    Then the response status code should be 200
    And the response should contain the correct title "Тестовая заметка"

  Scenario: Fail to create a note without title field
    Given there is a note without title
    When I send a request to create the note
    Then the response status code should be 422


