Feature: Delete the note

  Scenario: Delete a note with valid ID
    Given a valid note payload
    When I send a request to create the note
    When I send a request to delete the last created note
    Then the response status code should be 200


  Scenario: Try to delete a note with invalid ID

    When I send a request to delete the note with id "999999"
    Then the response status code should be 404
