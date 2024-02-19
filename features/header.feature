Feature: Check titles on all pages
  As unregistered user
  I want to check all button in header
  So I can click on any button in the header
  and redirect to relevant page and titles.

  Scenario: Title on Home page
    When I open Homepage
    Given I see title default "site_title"

  Scenario: Title on About page
    When I open Homepage
    Then I click on About button
    Given I see title default "about_title"

#  Scenario Outline: Names on Home page
#    When I open Homepage
#    Given I see title default "<name>"
#    Given I see title default "<result>"
#    Examples:
#      | name | result |
#      | 1    | a      |
#      | 2    | b      |
#      | 3    | c      |
#