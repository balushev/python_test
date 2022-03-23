@nightly_run
Feature: Create Documents
""" This feature contains all scenarios for documents creation """

  @sanity_check
  Scenario: Create a Documents for Home insurance (Add Home)
  """ This UI scenario testing creation of a documents for Home insurance (Add Home) """

    * Set resource name for locators Argenta Run => Documents => Home insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Pause for 5 seconds
    * Choose English for language options area
    * Choose Home insurance for Documents drop-down menu
