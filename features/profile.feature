Feature: Log-in

    Scenario: Log in 
        Given I navigate to the Wikipedia Home page
        When I change the language to "Hrvatski"
        Then I am taken to the "Hrvatski" Wikipedia page
        And I log in with credentials "yourUsername" \ "yourPassword" 
        And I log out
        
