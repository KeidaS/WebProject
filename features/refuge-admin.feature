Feature: Register/Edit/Delete refuge
  In order to register/edit/delete a refuge
  As a admin
  I want to create/edit/delete it

Background: There is a registered admin
    Given Exists an admin "user" with password "password"

  Scenario: Register just refuge name
    Given I login as user "user" with password "password"
    When I register refuge
      | name        |
      | Mil Banderes |
    Then I'm viewing the details page for refuge with "user"
      | name        |
      | Mil Banderes  |
    And There are 1 refuges

  Scenario: Edit refuge as admin
    Given I login as user "user" with password "password"
    And Exists refuge registered and a "user"
     | name |
     | Mil Banderes |
    When I edit the refuge with name "Mil Banderes"
     | name |
     | Tomas |
    Then I'm viewing the details page for refuge with "user"
     | name |
     | Tomas |
    And There are 1 refuges

  Scenario: Delete refuge as admin
    Given I login as user "user" with password "password"
    And Exists refuge registered and a "user"
     | name |
     | Mil Banderes |
    When I delete the refuge with name "Mil Banderes"
     | name |
     | Tomas |
    Then there are 0 refuges