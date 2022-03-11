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
    'add_motorcycle_vehicle_details_page_vehicle_type': ('motorcycle', 'three wheel motorcycle', 'four wheel motorcycle'),
    'add_moped_vehicle_details_page_vehicle_type': ('class a', 'class b', 'three wheel moped', 'four wheel moped', 'speed pedelec'),
    'quote': ('home insurance', 'car insurance', 'family insurance', 'motorcycle insurance'),
    'add_motorcycle_add_claim_page_nature': ('accident', 'corporal claim', 'damage to third', 'fire', 'glass breakage',
                                             'material claim', 'other', 'parking', 'theft'),
    'add_moped_add_claim_page_nature': ('accident', 'corporal claim', 'damage to third', 'fire', 'glass breakage',
                                        'material claim', 'other', 'parking', 'theft'),
    'add_motorcycle_add_claim_page_liability': ('0 percent', '50 percent', '100 percent'),
    'add_moped_add_claim_page_liability': ('0 percent', '50 percent', '100 percent'),
    'add_motorcycle_add_claim_page_driver_type': ('primary', 'secondary', 'occasional'),
    'add_moped_add_claim_page_driver_type': ('primary', 'secondary', 'occasional')
}

# Dictionary which contains all options area values
options_area_lists = {
    'add_motorcycle_vehicle_details_page_registration_type': ('euro plate', 'normal plate', 'bz plate', 'trader plate', 'transit plate'),
    'add_moped_vehicle_details_page_registration_type': ('euro plate', 'normal plate', 'bz plate', 'trader plate', 'transit plate'),
    'add_motorcycle_vehicle_details_page_fuel_type': ('diesel oil', 'electric', 'natural gas for vehicles', 'petrol'),
    'add_moped_vehicle_details_page_fuel_type': ('diesel oil', 'electric', 'natural gas for vehicles', 'petrol'),
    'add_motorcycle_vehicle_details_page_usage_type': ('private', ),
    'add_moped_vehicle_details_page_usage_type': ('private', ),
    'add_motorcycle_add_driver_driver_license_page_license_category': ('a', 'a1', 'a2'),
    'add_moped_add_driver_driver_license_page_license_category': ('am', 'a', 'a1', 'a2', 'b', 'b1', 'be', 'c', 'c1',
                                                                  'ce', 'c1e', 'd', 'd1', 'de', 'd1e'),
    'billing_page_type': ('direct credit', 'direct debit'),
    'billing_page_frequency': ('monthly', 'quarterly', 'semi annual', 'annual'),
    'add_motorcycle_coverage_tariffs_page_coverages': ('civil liability', 'free assistance',
                                                       'legal assistance basis', 'legal assistance safe'),
    'add_moped_coverage_tariffs_page_coverages': ('civil liability', 'free assistance',
                                                  'legal assistance basis', 'legal assistance safe'),
    'add_motorcycle_add_claim_page_risk_fully_repaired': ('no', 'yes'),
    'add_moped_add_claim_page_risk_fully_repaired': ('no', 'yes')
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
quote_dropdown = 'div#navbarSupportedContent:nth-of-type(2)'
quote_dropdown_tuple = (
    '#cdk-overlay-0>div>div>button:nth-of-type(1):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(2):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(3):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(4):not(aria-disabled)'
)

# Search Owner page
search_owner_button = '#search-owner-undefined-anchor'
search_person_link = 'a#person-search-undefined-anchor'
search_organization_link = 'a#organization-search-undefined-anchor'
search_owner_page_first_name_input = 'input#person-search-first-name-text'
search_owner_page_last_name_input = 'input#person-search-last-name-text'
search_owner_page_client_id_input = 'input#person-search-client-identifier-text'
search_owner_page_date_of_birth_input = 'input#person-search-client-date-date_input'
referential_first_search_result = '#_0'

search_owner_page_search_button = 'button#btnfilter'
search_owner_page_reset_button = 'button#btnreset'

risk_button = 'button#risk-management-undefined-button'

# Billing page
billing_page_type_options_tuple = (
    'button[id="billing-billing-payment-type-toggle_Direct Credit_-button"]',
    'button[id="billing-billing-payment-type-toggle_Direct Debit_-button"]'
)

billing_page_frequency_options_tuple = (
    'button#billing-billing-frequency-toggle_Monthly_-button',
    'button#billing-billing-frequency-toggle_Quaterly_-button',
    'button#billing-billing-frequency-toggle_Semi-Annual_-button',
    'button#billing-billing-frequency-toggle_Annual_-button'
)

billing_renewal_day_input = 'input#billing-billing-main-due-day-text'
billing_renewal_month_input = 'input#billing-billing-main-due-month-text'
billing_button = 'button#billing-undefined-button'
billing_page_renewal_day_input = 'input#billing-billing-main-due-day-text'
billing_page_renewal_month_input = 'input#billing-billing-main-due-month-text'

risk_acceptance_button = 'button#risk-acceptance-undefined-button'
coverage_tariffs_button = 'button#coverages-tariffs-undefined-button'
offer_congratulations_message = '.propositionMessage>a>h3'
summary_button = 'button#summary-undefined-button'
submission_button = 'button#submission-undefined-button'
proceed_to_offer_button = 'button#proceed-to-offer-undefined-button'

# Add Motorcycle
add_motorcycle_button = 'button#add-motorcycle-risk-undefined-button-modal'

add_motorcycle_vehicle_details_page_make_input = 'input#quote-risk-motorcycle-make-text'
add_motorcycle_vehicle_details_page_model_input = 'input#quote-risk-motorcycle-model-text'

add_motorcycle_vehicle_details_page_vehicle_type_dropdown = '#quote-risk-motorcycle-type-select'
add_motorcycle_vehicle_details_page_vehicle_type_dropdown_tuple = '#quote-risk-motorcycle-type-select_@index@'

add_motorcycle_vehicle_details_page_cubic_capacity_input = 'input#quote-risk-motorcycle-cubic-capacity-number'
add_motorcycle_vehicle_details_page_registration_number_input = 'input#quote-risk-motorcycle-registration-number-text'
add_motorcycle_vehicle_details_page_chassis_number_input = 'input#quote-risk-motorcycle-serial-number-text'

add_motorcycle_vehicle_details_page_registration_type_options_tuple = (
    'button[id="quote-risk-motorcycle-registration-type-toggle_Euro Plate_-button"]',
    'button[id="quote-risk-motorcycle-registration-type-toggle_Normal Plate_-button"]',
    'button[id="quote-risk-motorcycle-registration-type-toggle_BZ Plate_-button"]',
    'button[id="quote-risk-motorcycle-registration-type-toggle_Trader Plate_-button"]',
    'button[id="quote-risk-motorcycle-registration-type-toggle_Transit Plate_-button"]'
)

add_motorcycle_vehicle_details_page_fuel_type_options_tuple = (
    'button[id="quote-risk-motorcycle-fuel-type-toggle_Diesel Oil_-button"]',
    'button[id="quote-risk-motorcycle-fuel-type-toggle_Electric_-button"]',
    'button[id="quote-risk-motorcycle-fuel-type-toggle_Natural Gas for Vehicles_-button"]',
    'button[id="quote-risk-motorcycle-fuel-type-toggle_Petrol_-button"]'
)

add_motorcycle_vehicle_details_page_usage_type_options_tuple = ('button#quote-risk-motocycle-usage-type-toggle_Private_-button',)

add_motorcycle_claim_history_page_next_button = 'a#undefined-4-anchor'
add_motorcycle_add_driver_driver_license_page_license_category_options_tuple = (
    'button#driver-quote-driver-license-category-toggle_A_-button',
    'button#driver-quote-driver-license-category-toggle_A1_-button',
    'button#driver-quote-driver-license-category-toggle_A2_-button'
)

add_motorcycle_add_driver_driver_license_page_next_button = '#cdk-accordion-child-8 a#undefined-3-anchor'
add_motorcycle_add_driver_address_page_next_button = '#cdk-accordion-child-9 #undefined-4-anchor'
add_motorcycle_add_driver_page_ok_button = '#mat-dialog-3 button#modal__ok'
add_motorcycle_page_ok_button = 'button#modal__ok'
add_motorcycle_coverage_tariffs_page_coverages_options_tuple = '#package-quote-product-component-selected-checkbox0@index@'
add_motorcycle_risk_acceptance_page_answer_no_button = 'button#ques-ans-item-question-answer-answer-boolean-toggle__FALSE_05-button'
add_motorcycle_vehicle_details_page_next_button = 'a#undefined-3-anchor'
add_motorcycle_claim_history_page_add_claim_button = 'button#add-claim-undefined-button-modal'

add_motorcycle_add_claim_page_nature_dropdown = '#claim-history-property-recorded-claim-claim-type-select'
add_motorcycle_add_claim_page_nature_dropdown_tuple = ('#accident', '#corporal_responsible', '#damage_to_third', '#fire',
                                                       '#glass_breakage', '#material_responsible', '#other', '#parking', '#theft')

add_motorcycle_add_claim_page_date_input = 'input#claim-history-property-recorded-claim-date-date_input'

add_motorcycle_add_claim_page_liability_dropdown = '#claim-history-property-recorded-claim-liability-select'
add_motorcycle_add_claim_page_liability_dropdown_tuple = '#claim-history-property-recorded-claim-liability-select_@index@'

add_motorcycle_add_claim_page_driver_type_dropdown = '#claim-history-property-recorded-claim-driver-type-select'
add_motorcycle_add_claim_page_driver_type_dropdown_tuple = '#claim-history-property-recorded-claim-driver-type-select_@index@'

add_motorcycle_add_claim_page_driver_date_of_birth_input = 'input#claim-history-property-recorded-claim-driver-birth-date-date_input'
add_motorcycle_add_claim_page_amount_input = 'input#claim-history-property-recorded-claim-amount-text'

add_motorcycle_add_claim_page_risk_fully_repaired_options_tuple = (
    'button#claim-history-property-recorded-claim-is-repaired-toggle__FALSE_-button',
    'button#claim-history-property-recorded-claim-is-repaired-toggle__TRUE_-button'
)

add_motorcycle_add_claim_page_joker_used_options_tuple = (
    'button#claim-history-property-recorded-claim-joker-used-toggle__FALSE_-button',
    'button#claim-history-property-recorded-claim-joker-used-toggle__TRUE_-button'
)

add_motorcycle_add_claim_page_ok_button = 'button:nth-of-type(1)#modal__ok'
add_motorcycle_drivers_page_add_driver_button = 'button#quote-drivers-undefined-button-modal'
add_motorcycle_add_driver_page_next_button = 'a#undefined-2-anchor'
add_motorcycle_driver_license_page_license_id_input = 'input#driver-driving-category-info-license-id-text'
add_motorcycle_add_driver_driver_license_page_license_date_input = 'input#driver-quote-driver-license-date-date_input'
add_motorcycle_add_driver_contact_page_next_button = '#cdk-accordion-child-12 #undefined-5-anchor'

# Add Moped
add_moped_button = 'button#add-moped-risk-undefined-button-modal'

add_moped_vehicle_details_page_vehicle_type_dropdown = '#quote-risk-moped-type-select'
add_moped_vehicle_details_page_vehicle_type_dropdown_tuple = '#quote-risk-moped-type-select_@index@'

add_moped_vehicle_details_page_make_input = 'input#quote-risk-moped-make-text'
add_moped_vehicle_details_page_model_input = 'input#quote-risk-moped-model-text'
add_moped_vehicle_details_page_cubic_capacity_input = 'input#quote-risk-moped-cubic-capacity-number'
add_moped_vehicle_details_page_registration_number_input = 'input#quote-risk-moped-registration-number-text'
add_moped_vehicle_details_page_chassis_number_input = 'input#quote-risk-moped-serial-number-text'

add_moped_vehicle_details_page_registration_type_options_tuple = (
    'button[id="quote-risk-moped-registration-type-toggle_Euro Plate_-button"]',
    'button[id="quote-risk-moped-registration-type-toggle_Normal Plate_-button"]',
    'button[id="quote-risk-moped-registration-type-toggle_BZ Plate_-button"]',
    'button[id="quote-risk-moped-registration-type-toggle_Trader Plate_-button"]',
    'button[id="quote-risk-moped-registration-type-toggle_Transit Plate_-button"]'
)

add_moped_vehicle_details_page_fuel_type_options_tuple = (
    'button[id="quote-risk-moped-fuel-type-toggle_Diesel Oil_-button"]',
    'button[id="quote-risk-moped-fuel-type-toggle_Electric_-button"]',
    'button[id="quote-risk-moped-fuel-type-toggle_Natural Gas for Vehicles_-button"]',
    'button[id="quote-risk-moped-fuel-type-toggle_Petrol_-button"]'
)

add_moped_vehicle_details_page_usage_type_options_tuple = (
    'button#quote-risk-moped-usage-type-toggle_Private_-button',
)

add_moped_claim_history_page_next_button = 'a#undefined-4-anchor'
add_moped_vehicle_details_page_next_button = add_motorcycle_vehicle_details_page_next_button
add_moped_claim_history_page_add_claim_button = add_motorcycle_claim_history_page_add_claim_button

add_moped_add_claim_page_nature_dropdown = add_motorcycle_add_claim_page_nature_dropdown
add_moped_add_claim_page_nature_dropdown_tuple = add_motorcycle_add_claim_page_nature_dropdown_tuple

add_moped_add_claim_page_date_input = add_motorcycle_add_claim_page_date_input

add_moped_add_claim_page_liability_dropdown = add_motorcycle_add_claim_page_liability_dropdown
add_moped_add_claim_page_liability_dropdown_tuple = add_motorcycle_add_claim_page_liability_dropdown_tuple

add_moped_add_claim_page_driver_type_dropdown = add_motorcycle_add_claim_page_driver_type_dropdown
add_moped_add_claim_page_driver_type_dropdown_tuple = add_motorcycle_add_claim_page_driver_type_dropdown_tuple

add_moped_add_claim_page_driver_date_of_birth_input = add_motorcycle_add_claim_page_driver_date_of_birth_input
add_moped_add_claim_page_amount_input = add_motorcycle_add_claim_page_amount_input
add_moped_add_claim_page_risk_fully_repaired_options_tuple = add_motorcycle_add_claim_page_risk_fully_repaired_options_tuple
add_moped_add_claim_page_ok_button = add_motorcycle_add_claim_page_ok_button
add_moped_drivers_page_add_driver_button = add_motorcycle_drivers_page_add_driver_button
add_moped_add_driver_page_next_button = add_motorcycle_add_driver_page_next_button
add_moped_add_driver_driver_license_page_license_date_input = add_motorcycle_add_driver_driver_license_page_license_date_input

add_moped_add_driver_driver_license_page_license_category_options_tuple = (
    'button#driver-quote-driver-license-category-toggle_AM_-button',
    'button#driver-quote-driver-license-category-toggle_A_-button',
    'button#driver-quote-driver-license-category-toggle_A1_-button',
    'button#driver-quote-driver-license-category-toggle_A2_-button',
    'button#driver-quote-driver-license-category-toggle_B_-button',
    'button#driver-quote-driver-license-category-toggle_B1_-button',
    'button#driver-quote-driver-license-category-toggle_BE_-button',
    'button#driver-quote-driver-license-category-toggle_C_-button',
    'button#driver-quote-driver-license-category-toggle_C1_-button',
    'button#driver-quote-driver-license-category-toggle_CE_-button',
    'button#driver-quote-driver-license-category-toggle_C1E_-button',
    'button#driver-quote-driver-license-category-toggle_D_-button',
    'button#driver-quote-driver-license-category-toggle_D1_-button',
    'button#driver-quote-driver-license-category-toggle_DE_-button',
    'button#driver-quote-driver-license-category-toggle_D1E_-button'
)

add_moped_add_driver_driver_license_page_next_button = add_motorcycle_add_driver_driver_license_page_next_button
add_moped_add_driver_address_page_next_button = add_motorcycle_add_driver_address_page_next_button
add_moped_add_driver_page_ok_button = add_motorcycle_add_driver_page_ok_button
add_moped_page_ok_button = add_motorcycle_page_ok_button
add_moped_coverage_tariffs_page_coverages_options_tuple = add_motorcycle_coverage_tariffs_page_coverages_options_tuple
add_moped_risk_acceptance_page_answer_no_button = add_motorcycle_risk_acceptance_page_answer_no_button
