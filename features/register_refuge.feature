Feature: Register Restaurant
  In order to keep track of the existent refuges
  As a user
  I want to register a refuge

  Background: There is a registered user
    Given Exists an user "user" with password "password"

  Scenario: Can't create a refuge as a registered user.
    Given I login as user "user" with password "password"
    Then There is no "dogapp:refuge_create" link available
    And There are 0 refuges