Feature: Register admin
  In order to login
  As a admin
  I want to login

  Background: There is a registered admin
    Given Exists an admin "user" with password "password"

  Scenario: Can create a refuge as a registered admin.
    Given I login as user "user" with password "password"
    Then There is "add" link available
    And There are 0 refuges