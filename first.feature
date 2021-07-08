Feature: Learn Behave

  Scenario: Testing diffrent data transfer
    Given Simple function "value of xyz"
    Then Text passing
      """
      My name is vipin
      """
    Then Call by python


  Scenario: Passing Table
    Given Table
      | name | vipin |
      | team | QE    |