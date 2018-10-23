Feature: Search

    Scenario: Search Wikipedia
        Given I navigate to the Wikipedia Home page
        When I search for "Python"
        Then I am taken to the Wikipedia Search Results page
        And I see a search result "Python (programming language)"