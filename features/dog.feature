Feature: Register/Edit/Delete dog from a refuge
  In order to register/edit/delete a dog
  As a admin
  I want to create/edit/delete it

Background: There is a registered admin
    Given Exists an admin "user" with password "password"

  Scenario: Register dog on a refuge as admin
    Given I login as user "user" with password "password"
    And Exists refuge registered and a "user"
     | name |
     | Mil Banderes |
    When I register dog at refuge "Mil Banderes"
     |name |
     | Milba |
    Then There are 1 dogs

  Scenario: Edit refuge as admin
    Given I login as user "user" with password "password"
    And Exists refuge registered and a "user"
     | name |
     | Mil Banderes |
    And Exists dog at refuge "Mil Banderes"
     | name |
     | Milba |
    When I edit the dog "Milba" of the refuge "Mil Banderes"
     | name |
     | Tomas |
     Then There are 1 dogs

  Scenario: Delete refuge as admin
    Given I login as user "user" with password "password"
    And Exists refuge registered and a "user"
     | name |
     | Mil Banderes |
    And Exists dog at refuge "Mil Banderes"
     | name |
     | Milba |
    When I delete the current dog
    Then there are 0 dogs