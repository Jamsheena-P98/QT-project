Feature: Login Functionalities

  Scenario: To verify Login functionality
    Given I am logged into QT
    Then System should display the QT site
    When I click on the login icon
    And I enter email
    And I enter password
    And I click on signin