Feature: List notes

  Scenario: Get list of notes when there are no notes
    Given all notes are deleted
    When I send a request to get the list of notes
    Then the response status code should be 200
    And the response should contain an empty list of notes

  Scenario: Get list of notes when notes exist
    Given a valid note payload
    When I send a request to create the note
    When I send a request to get the list of notes
    Then the response status code should be 200
    And the response should contain a list with at least one note
