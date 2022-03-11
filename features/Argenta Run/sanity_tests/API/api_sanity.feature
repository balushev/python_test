@Argentat
Feature: Argenta Person-Home
  Please fill comment here !!!

  Scenario: My first API scenario no UI
    #This is my first API scenario
    Given I get distributor_id from distributors
    When  Quotes created with current distributor id
      | product_id |
      | VZWP01     |
    And I get information for the owners
#    And I create the process ???
#    And I update process ???
#    And I Post info ???
    And I get information for the owners with some ID
    And I Get info for person with last name
      | last_name |
      | HAZARD    |
    And I Get info for person with first name
      | first_name |
      | Eden       |
    And I update information using owner url and person uri in body
    And I calculate quote risk
    And I get extension element for quot risk uri
    And I get questionnaire_uri, id_risk_evaluation_question_answer and quote_risk_questionnaire_question_answer_uri from quote risk uri
#    And I update info in quote risk uri, dwelling_type, dwelling_usage_type
#      | dwelling_type | dwelling_usage_type |
#      | ????          | ????                |
#    And I Patch for extension element uri
#      | extension_element:value |
#      | home                    |
#      | no                      |
#      | flmbl_no                |
#    And Post for quote risk uri evaluate value - status code 405
#    And I get question uri
#      | question_number |
#      | 2               |
#    And I Patch questionnaires question answer
#    And I get evaluate value - status code 400
#    And I get for questionnaire uri
#    And I get questionnaires question answer
#    And I update question_answers for question uri
#    And I Post evaluate value
#    And I Post tariff calculation
#    And I Post quotes risk created
#    And I Patch quotes risk
#    And I get quote risk
#    And I get product components
#    And I get product components for some component ID
#    And I get quote risk for family uri
#    And I get family product components
#    And I get product components for some family product component ID
#    And I get tariff adjustments
#    And I get output documents
#    And I Post operators transfer to offer
#    And I get reference for product
#    And I get party roles
#    And I get billings for the offer
#    And I get party role person uri
#    And I get postal address uri
#    And I get risk for the offer
#    And I get extension elements for the offer uri
#    And I get bank accounts
#    And I get offer questionnaire uri
#    And I get offer question answers uri
#    And I Patch offer question answers uri
#    And I get notes
#    And I Post validate
#    And I Post transfer to contract