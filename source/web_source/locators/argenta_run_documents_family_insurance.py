# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:09:04 2022

@author: bbalushev
"""


""" This file contains all locators related with 'Argenta Offer Add Home' UI flow """

# ================================================ Mandatory elements ================================================
# Loading Div (mandatory)
loading_page_element = '.loadingDiv'

# Dictionary which contains all dropdowns values
dropdown_lists = {
    'offer': ('home insurance', 'car insurance', 'family insurance', 'motorcycle insurance')
}

# Dictionary which contains all options area values
options_area_lists = {
    'home_branch_owner': ('nc', 'fc'),
    'add_family_page_family_situation': ('family', '60 plus', 'single'),
    'billing_page_type': ('direct credit', 'direct debit'),
    'billing_page_frequency': ('monthly', 'quarterly', 'semi annual', 'annual'),
    'add_family_add_home_risk_evaluation_page_evaluation_method': ('gim', 'by questions', 'manual')
}

# ===================================================== Locators =====================================================

# OmniChannel login page
login_username = 'input#authUsername'
login_password = 'input#authPassword'
login_button = 'button#loginBtn'

# Send to the back office page
submit_documents_button = 'button#create-documents-button'

# Distributor search page
distributor_search_page_general_info_description = '#toggle-0 mat-panel-description'
distributor_search_page_distributor_id_field = 'input#distributor-search-distributor-id-text'
distributor_search_page_distributor_button_reset = 'button#btnreset'
distributor_search_page_distributor_button_search = 'button#btnfilter'
distributor_search_page_distributor_id_tuple = '#_@index@__DISTRIBUTOR_ID'
distributor_search_page_distributor_total_count = '.paginator-totalcount'
distributor_search_page_distributor_button_ok = 'button#modal__ok'
distributor_search_page_distributor_button_cancel = 'button#modal__close'

# Main Page
offer_dropdown = 'div#navbarSupportedContent:nth-of-type(4)'
offer_dropdown_tuple = (
    '#cdk-overlay-0>div>div>button:nth-of-type(1):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(2):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(3):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(4):not(aria-disabled)'
)

search_person_link = 'a#person-search-undefined-anchor'
search_organization_link = 'a#organization-search-undefined-anchor'


person_search_page_first_name_input = 'input#person-search-first-name-text'
person_search_page_last_name_input = 'input#person-search-last-name-text'
person_search_page_client_id_input = 'input#person-search-client-identifier-text'
person_search_page_date_of_birth_input = 'input#person-search-client-date-date_input'
person_search_page_search_button = 'button#btnfilter'
person_search_page_reset_button = 'button#btnreset'

referential_first_search_result = '#_0'
risk_button = 'button#risk-management-undefined-button'
billing_button = 'button#billing-undefined-button'

# Billing page
billing_page_type_options_tuple = (
    'button[id="billing-billing-payment-type-toggle_Direct Credit_-button"]',
    'button[id="billing-billing-payment-type-toggle_Direct Debit_-button"]'
)

billing_page_frequency_options_tuple = (
    'button[id="billing-billing-frequency-toggle_Monthly_-button"]',
    'button[id="billing-billing-frequency-toggle_Quaterly_-button"]',
    'button[id="billing-billing-frequency-toggle_Semi-Annual_-button"]',
    'button[id="billing-billing-frequency-toggle_Annual_-button"]'
)

billing_page_renewal_day_input = 'input#billing-billing-main-due-day-text'
billing_page_renewal_month_input = 'input#billing-billing-main-due-month-text'
risk_acceptance_button = 'button#risk-acceptance-undefined-button'

# Coverage / Tariffs page
summary_button = 'button#summary-undefined-button'
submission_button = 'button#submission-undefined-button'
risk_acceptance_answer_button = 'button#ques-ans-item-question-answer-answer-boolean-toggle__FALSE_05-button'

# Family
search_owner_page_first_name_input = 'input#person-search-first-name-text'
search_owner_page_search_button = 'button#btnfilter'
add_family_button = 'button#add-family-risk-undefined-button-modal'
add_family_page_ok_button = 'button#modal__ok'
coverage_tariffs_button = 'button#coverages-tariffs-undefined-button'
add_family_page_risk_acceptance_answer_no_button = 'button#ques-ans-item-question-answer-answer-boolean-toggle__FALSE_00-button'
offer_congratulations_message = '.propositionMessage>a>h3'

add_family_page_family_situation_options_tuple = (
    'button[id="quote-risk-family-family-situation-toggle_Family_-button"]',
    'button[id="quote-risk-family-family-situation-toggle_60+_-button"]',
    'button[id="quote-risk-family-family-situation-toggle_Single_-button"]'
)
