Feature: Get a single note by ID

  Scenario: Get a note with a valid ID
    Given there is a note with title "Заметка для удаления" and content "Контент"
    When  I send a request to create the note
    When I send a request to get the last created note
    Then the response status code should be 200
    And the response should contain the correct title "Заметка для удаления"
    And the response should contain the correct content "Контент"

  Scenario: Try to get a note with an invalid ID
    When I send a request to get the note with id "999999"
    Then the response status code should be 404