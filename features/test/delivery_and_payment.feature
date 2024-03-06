Feature: Verify delivery and payment page title

  Scenario: Switch to Ukrainian language and verify the title on delivery and payment page

    When I navigate to Homepage

    Then I switch ua language

    Given I am on the delivery and payment page

    Then I should see the correct title