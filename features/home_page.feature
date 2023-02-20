Feature: Test the click for 3 elements in the Internet page

  Background:
    Given Home page: I am on The internet page

@Test1
  Scenario: Check that the user can click on the element  Form Authentication
    When Home page: I click to Form Authentication
    Then Home page: I go to the Login page

@Test2
  Scenario: Check that the user can select an option  on the Dropdown List
    When Home page: I click to Dropdown
    Then Dropdown page: I select Option 1 and i check if it is the first option

@Test3
  Scenario: Check the error message on the Login page, when the user is incorrect
    When Home page: I go to the Login page
    When Login page: Enter the incorrect user and password
    When Login page: Click on the Login button
    Then Login page: The error message must be diplayed

@Test4
  Scenario: Check the Secure page
    When Home page:I click to elem Form Authentication
    When Login page: Enter the correct user and password
    When Login page: I click on the Login button
    When Secure page: I check if the success message is displayed
    Then Secure page: I click on the Logout button
