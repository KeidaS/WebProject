Feature: Register Restaurant
  In order to keep track of the existent refuges
  As a admin
  I want to register a refuge with its location and contact details

  Background: There is a registered user
    Given Exists an user "user" with password "password"

  Scenario: Register just restaurant name
    Given I login as user "user" with password "password"
    When I register refuge
      | name        |
      | Mil Banderes  |
    Then I'm viewing the details page for restaurant by "admin"
      | name        |
      | Mil Banderes  |
    And There are 1 refuges