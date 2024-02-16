Feature: Killa.ua Website Testing
    As a unregistered user
    I want to test various functionalities of the Killa.ua website
    So that I can ensure its proper operation

    Scenario: Verify homepage title
        Given I am on the Killa.ua homepage
        Then the title should contain "Killa.ua"

    Scenario: Perform a product search
        Given I am on the Killa.ua homepage
        When I search for "iPhone"
        Then the search results page should contain "iPhone"

    Scenario: Add a product to the cart
        Given I am on the Killa.ua homepage
        When I navigate to the iPhone X product page
        And I add the product to the cart
        And I view the cart
        Then the cart should contain "iPhone X"

    Scenario: Login to the website
        Given I am on the Killa.ua login page
        When I enter my username and password
        And I click the login button
        Then I should be redirected to the "My Account" page

    Scenario: Proceed to checkout
        Given I am on the Killa.ua cart page
        When I proceed to checkout
        Then the title should contain "Checkout"