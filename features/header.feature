Feature: Check headers on all pages
  As unregistered user
  I want to check all button in header
  So I can click on any button in the header
  and redirect to relevant page.

  Scenario: Title on Home page
    When I open Homepage
    Given I see title default "site_title"

  Scenario: Title on About page
    When I open Homepage
    Then I click on About button
    Given I see title default "about_title"