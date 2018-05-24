Feature: Register user
  In order to login
  As a user
  I want to login

  Background: There is a registered user
    Given Exists an user "user" with password "password"

  Scenario: Can't create a refuge as a registered user.
    Given I login as user "user" with password "password"
    Then There is no "dogapp:refuge_create" link available
    And There are 0 refuges
