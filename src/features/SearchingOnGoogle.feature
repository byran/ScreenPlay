Feature: Searching the internet
  Anything can be searched for on Google

  The results are displayed in order of Page Rank

  Scenario: Wikipedia is shown on the first page of results as it has a high page rank
    Given Byran has opened Google
    When they search for "Hello World"
    Then they should see a result for '"Hello, World!" program - Wikipedia'
