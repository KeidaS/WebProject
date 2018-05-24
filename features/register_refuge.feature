Feature: Register Restaurant
  In order to keep track of the existent refuges
  As a admin
  I want to register a refuge with its location and contact details

  Background: There is a registered user
    Given Exists an user "user" with password "password"

  Scenario: I don't register a refuge as user
    Given I login as user "user" with password "password"
    Then There is no "dogapp:refuge_create" link available
    And There are 0 refuges