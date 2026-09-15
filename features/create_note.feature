Feature: Create a note

  Scenario: Successfully create a note
    Given a valid note payload
    When I send a request to create the note
    Then the response status code should be 200
    And the response should contain the correct title "Тестовая заметка"
    And the response should contain the correct content "Содержание заметки"

  Scenario: Fail to create a note without title field
    Given an invalid note payload
    When I send a request to create the note
    Then the response status code should be 422


