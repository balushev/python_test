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
    'offer': ('home insurance', 'car insurance', 'family insurance', 'motorcycle insurance'),
    'add_car_vehicle_details_page_vehicle_type': ('minibus', 'passenger car', 'station wagon or all terrain vehicle'),
    'add_van_vehicle_details_page_vehicle_type': ('station wagon or all-terrain vehicle', 'truck'),
    'add_old_timer_vehicle_details_page_vehicle_type': ('old timer private car',),
    'add_truck_camper_vehicle_details_page_vehicle_type': ('camping car',),
    'add_car_add_claim_page_nature': ('accident', 'corporal claim', 'damage to third', 'fire', 'glass breakage',
                                      'material claim', 'other', 'parking', 'theft'),
    'add_old_timer_add_claim_page_nature': ('accident', 'corporal claim', 'damage to third', 'fire', 'glass breakage',
                                            'material claim', 'other', 'parking', 'theft'),
    'add_van_add_claim_page_nature': ('accident', 'corporal claim', 'damage to third', 'fire', 'glass breakage',
                                      'material claim', 'other', 'parking', 'theft'),
    'add_truck_camper_add_claim_page_nature': ('accident', 'corporal claim', 'damage to third', 'fire', 'glass breakage',
                                               'material claim', 'other', 'parking', 'theft'),
    'add_car_add_claim_page_liability': ('0 percent', '50 percent', '100 percent'),
    'add_old_timer_add_claim_page_liability': ('0 percent', '50 percent', '100 percent'),
    'add_van_add_claim_page_liability': ('0 percent', '50 percent', '100 percent'),
    'add_truck_camper_add_claim_page_liability': ('0 percent', '50 percent', '100 percent'),
    'add_car_add_claim_page_driver_type': ('primary', 'secondary', 'occasional'),
    'add_old_timer_add_claim_page_driver_type': ('primary', 'secondary', 'occasional'),
    'add_van_add_claim_page_driver_type': ('primary', 'secondary', 'occasional'),
    'add_truck_camper_add_claim_page_driver_type': ('primary', 'secondary', 'occasional')
}

# Dictionary which contains all options area values
options_area_lists = {
    'add_car_vehicle_details_page_registration_type': ('euro plate', 'normal plate', 'bz plate', 'trader plate',
                                                       'transit plate'),
    'add_old_timer_vehicle_details_page_registration_type': ('euro plate', 'normal plate', 'bz plate', 'trader plate',
                                                             'transit plate'),
    'add_van_vehicle_details_page_registration_type': ('euro plate', 'normal plate', 'bz plate', 'trader plate',
                                                       'transit plate'),
    'add_truck_camper_vehicle_details_page_registration_type': ('euro plate', 'normal plate', 'bz plate', 'trader plate',
                                                                'transit plate'),
    'add_car_vehicle_details_page_fuel_type': ('bio ethanol', 'diesel oil', 'electric',
                                               'hybrid / micro hybrid diesel oil', 'hybrid / micro hybrid petrol',
                                               'lpg', 'natural gas for vehicles', 'petrol',
                                               'plug-in hybrid diesel oil', 'plug-in hybrid petrol'),
    'add_old_timer_vehicle_details_page_fuel_type': ('bio ethanol', 'diesel oil', 'electric',
                                                     'hybrid / micro hybrid diesel oil', 'hybrid / micro hybrid petrol',
                                                     'lpg', 'natural gas for vehicles', 'petrol',
                                                     'plug-in hybrid diesel oil', 'plug-in hybrid petrol'),
    'add_van_vehicle_details_page_fuel_type': ('diesel oil', 'electric', 'hybrid (diesel oil / electricity)',
                                               'hybrid (petrol / electricity)','hydrogen', 'lpg',
                                               'natural gas for vehicles', 'petrol', 'unknown'),
    'add_truck_camper_vehicle_details_page_fuel_type': ('diesel oil', 'electric', 'natural gas for vehicles', 'petrol'),
    'add_car_vehicle_details_page_usage_type': ('private', 'professional'),
    'add_old_timer_vehicle_details_page_usage_type': ('private', 'professional'),
    'add_van_vehicle_details_page_usage_type': ('business rounds', 'craftsman', 'private', 'private - Business Journeys',
                                                'taxi', 'transport of goods', 'professional'),
    'add_truck_camper_vehicle_details_page_usage_type': ('professional', 'private'),
    'add_car_add_claim_page_joker_used': ('no', 'yes'),
    'add_old_timer_add_claim_page_joker_used': ('no', 'yes'),
    'add_van_add_claim_page_joker_used': ('no', 'yes'),
    'add_truck_camper_add_claim_page_joker_used': ('no', 'yes'),
    'add_car_add_claim_page_risk_fully_repaired': ('no', 'yes'),
    'add_old_timer_add_claim_page_risk_fully_repaired': ('no', 'yes'),
    'add_van_add_claim_page_risk_fully_repaired': ('no', 'yes'),
    'add_truck_camper_add_claim_page_risk_fully_repaired': ('no', 'yes'),
    'add_car_risk_background_page_certificates': ('no', 'yes'),
    'add_old_timer_risk_background_page_certificates': ('no', 'yes'),
    'add_van_risk_background_page_certificates': ('no', 'yes'),
    'add_truck_camper_risk_background_page_certificates': ('no', 'yes'),
    'add_car_add_driver_driver_license_page_license_category': ('b', 'be', 'c', 'ce', 'c1', 'c1e',
                                                                'd', 'de', 'd1', 'd1e'),
    'add_old_timer_add_driver_driver_license_page_license_category': ('b', 'be', 'c', 'ce', 'c1', 'c1e',
                                                                      'd', 'de', 'd1', 'd1e'),
    'add_van_add_driver_driver_license_page_license_category': ('b', 'be', 'c', 'ce', 'c1', 'c1e',
                                                                'd', 'de', 'd1', 'd1e'),
    'add_truck_camper_add_driver_driver_license_page_license_category': ('b', 'be', 'c', 'ce', 'c1', 'c1e',
                                                                         'd', 'de', 'd1', 'd1e'),
    'add_car_coverage_tariffs_page': ('civil liability', 'partial omnium', 'own damage basic', 'own damage comfort',
                                      'driver plus', 'legal assistance safe', 'tmc insured'),
    'add_truck_camper_coverage_tariffs_page': ('civil liability', 'partial omnium', 'own damage basic',
                                               'own damage comfort', 'driver plus', 'legal assistance safe'),
    'add_van_coverage_tariffs_page': ('civil liability', 'partial omnium', 'own damage basic', 'own damage comfort',
                                      'driver plus', 'legal assistance safe', 'tmc insured'),
    'add_old_timer_coverage_tariffs_page': ('civil liability', 'free assistance', 'legal assistance safe'),
    'billing_page_type': ('direct credit', 'direct debit'),
    'billing_page_frequency': ('monthly', 'quarterly', 'semi annual', 'annual'),
    'application_menu': ('', 'dxc graphtalk', 'omnichannel', 'file exchange', 'scheduler', 'batch chain reports',
                         'admin console', 'gt admin gateway', 'help', 'help sysops'),
    'language': ('english', 'dutch', 'french')
}

# ===================================================== Locators =====================================================

# GTAIA login page
login_username = 'input#username'
login_password = 'input#password'
login_button = '#kc-login'

# Application menu
iframe = '#iframe'
application_menu_options_tuple = '#overview>div.row>div:nth-of-type(@index@)'
language_options_tuple = '#oc-language-option-@index@'

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


search_owner_page_first_name_input = 'input#person-search-first-name-text'
search_owner_page_last_name_input = 'input#person-search-last-name-text'
search_owner_page_client_id_input = 'input#person-search-client-identifier-text'
search_owner_page_date_of_birth_input = 'input#person-search-client-date-date_input'
search_owner_page_search_button = 'button#btnfilter'
search_owner_page_reset_button = 'button#btnreset'

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

# Add Car
add_car_button = 'button#add-auto-risk-undefined-button-modal'
add_old_timer_button = 'button#add-old-timer-risk-undefined-button-modal'
add_van_button = 'button#add-van-risk-undefined-button-modal'
add_truck_camper_button = 'button#add-campingcar-risk-undefined-button-modal'

add_car_vehicle_details_page_referential_vehicle_search_button = '#quote-risk-undefined-anchor'

add_car_preferential_vehicle_search_page_make_input = 'input#make-referential-vehicle-make-autocomplete'
add_car_preferential_vehicle_search_page_model_input = 'input#model-referential-vehicle-model-autocomplete'
add_car_preferential_vehicle_search_page_search_button = 'button#search-undefined-button'

add_car_vehicle_details_page_vehicle_type_dropdown = '#quote-risk-automobile-type-select'
add_car_vehicle_details_page_vehicle_type_dropdown_tuple = (
    '#arg_minibus',
    '#arg_passenger_car',
    '#arg_station_wagon_all_terrain'
)

add_car_vehicle_details_page_first_use_date_input = 'input#quote-risk-automobile-first-use-date-date_input'
add_car_vehicle_details_page_number_of_seats_input = 'input#quote-risk-automobile-seats-positions-number'
add_car_vehicle_details_page_registration_number_input = 'input#quote-risk-automobile-registration-number-text'
add_car_vehicle_details_page_chassis_number_input = 'input#quote-risk-automobile-serial-number-text'

add_car_vehicle_details_page_registration_type_options_tuple = (
    'button[id="quote-risk-automobile-registration-type-toggle_Euro Plate_-button"]',
    'button[id="quote-risk-automobile-registration-type-toggle_Normal Plate_-button"]',
    'button[id="quote-risk-automobile-registration-type-toggle_BZ Plate_-button"]',
    'button[id="quote-risk-automobile-registration-type-toggle_Trader Plate_-button"]',
    'button[id="quote-risk-automobile-registration-type-toggle_Transit Plate_-button"]'
)

add_car_vehicle_details_page_fuel_type_options_tuple = (
    'button[id="quote-risk-automobile-fuel-type-toggle_Bio Ethanol_-button"]',
    'button[id="quote-risk-automobile-fuel-type-toggle_Diesel Oil_-button"]',
    'button[id="quote-risk-automobile-fuel-type-toggle_Electric_-button"]',
    'button[id="quote-risk-automobile-fuel-type-toggle_Hybrid / Micro Hybrid Diesel Oil_-button"]',
    'button[id="quote-risk-automobile-fuel-type-toggle_Hybrid / Micro Hybrid Petrol_-button"]',
    'button[id="quote-risk-automobile-fuel-type-toggle_LPG_-button"]',
    'button[id="quote-risk-automobile-fuel-type-toggle_Natural Gas for Vehicles_-button"]',
    'button[id="quote-risk-automobile-fuel-type-toggle_Petrol_-button"]',
    'button[id="quote-risk-automobile-fuel-type-toggle_Plug-in Hybrid Diesel Oil_-button"]',
    'button[id="quote-risk-automobile-fuel-type-toggle_Plug-in Hybrid Petrol_-button"]'
)

add_car_vehicle_details_page_usage_type_options_tuple = (
    'button#quote-risk-automobile-usage-type-toggle_Private_-button',
    'button#quote-risk-automobile-usage-type-toggle_Professional_-button'
)

add_car_vehicle_details_page_next_button = 'a#undefined-3-anchor'
add_car_add_driver_driver_details_page_next_button = 'a#undefined-2-anchor'

add_car_risk_evaluation_page_vehicle_value_input = 'input#quote-risk-automobile-sum-insured-number'
add_car_risk_evaluation_page_accessories_equipment_value_input = 'input#quote-risk-automobile-accessoires-sum-number'
add_car_risk_evaluation_page_next_button = '#undefined-4-anchor'
add_car_claim_history_page_add_claim_button = 'button#add-claim-undefined-button-modal'

add_car_add_claim_page_nature_dropdown = '#claim-history-property-recorded-claim-claim-type-select'
add_car_add_claim_page_nature_dropdown_tuple = ('#accident', '#corporal_responsible', '#damage_to_third', '#fire',
                                                '#glass_breakage', '#material_responsible', '#other', '#parking', '#theft')

add_car_add_claim_page_date_input = 'input#claim-history-property-recorded-claim-date-date_input'

add_car_add_claim_page_liability_dropdown = '#claim-history-property-recorded-claim-liability-select'
add_car_add_claim_page_liability_dropdown_tuple = '#claim-history-property-recorded-claim-liability-select_@index@'

add_car_add_claim_page_driver_type_dropdown = '#claim-history-property-recorded-claim-driver-type-select'
add_car_add_claim_page_driver_type_dropdown_tuple = '#claim-history-property-recorded-claim-driver-type-select_@index@'

add_car_add_claim_page_driver_date_of_birth_input = 'input#claim-history-property-recorded-claim-driver-birth-date-date_input'

add_car_add_claim_page_joker_used_options_tuple = (
    'button#claim-history-property-recorded-claim-joker-used-toggle__FALSE_-button',
    'button#claim-history-property-recorded-claim-joker-used-toggle__TRUE_-button'
)

add_car_add_claim_page_amount_input = 'input#claim-history-property-recorded-claim-amount-text'

add_car_add_claim_page_risk_fully_repaired_options_tuple = (
    'button#claim-history-property-recorded-claim-is-repaired-toggle__FALSE_-button',
    'button#claim-history-property-recorded-claim-is-repaired-toggle__TRUE_-button'
)

add_car_add_claim_page_ok_button = 'button:nth-of-type(1)#modal__ok'
add_car_claim_history_page_next_button = 'a#undefined-5-anchor'
add_car_drivers_page_add_driver_button = 'button#add-driver-undefined-button'
add_car_add_driver_add_driver_page_next_button = 'a#undefined-6-anchor'
add_car_add_driver_driver_license_page_license_date_input = 'input#driver-driving-category-info-license-date-date_input'

add_car_add_driver_driver_license_page_license_category_options_tuple = (
    'button#driver-driving-category-info-license-category-toggle_B_-button',
    'button#driver-driving-category-info-license-category-toggle_BE_-button',
    'button#driver-driving-category-info-license-category-toggle_C_-button',
    'button#driver-driving-category-info-license-category-toggle_CE_-button',
    'button#driver-driving-category-info-license-category-toggle_C1_-button',
    'button#driver-driving-category-info-license-category-toggle_C1E_-button',
    'button#driver-driving-category-info-license-category-toggle_D_-button',
    'button#driver-driving-category-info-license-category-toggle_DE_-button',
    'button#driver-driving-category-info-license-category-toggle_D1_-button',
    'button#driver-driving-category-info-license-category-toggle_D1E_-button'
)

add_car_add_driver_driver_license_page_next_button = '#cdk-accordion-child-13 a#undefined-3-anchor'
add_car_add_driver_address_page_next_button = '#cdk-accordion-child-14 a#undefined-4-anchor'
add_car_add_driver_contact_page_next_button = '#cdk-accordion-child-15 #undefined-5-anchor'
add_car_add_driver_page_ok_button = '#driver button#modal__ok'
add_car_drivers_page_next_button = 'a#undefined-6-anchor'

add_car_risk_background_page_certificates_options_tuple = (
    'button#eval-ques-ans-question-answer-answer-boolean-toggle__FALSE_00-button',
    'button#eval-ques-ans-question-answer-answer-boolean-toggle__TRUE_00-button'
)

add_car_coverage_tariffs_page_options_tuple = '#package-selected-checkbox0@index@'
add_car_add_driver_driver_license_page_license_id_input = 'input#driver-driving-category-info-license-id-text'
add_car_previous_insurer_page_next_button = 'a#undefined-7-anchor'
add_car_risk_background_page_next_button = 'a#undefined-8-anchor'
add_car_page_ok_button = '#mat-dialog-2 button#modal__ok'
coverage_tariffs_button = 'button#coverages-tariffs-undefined-button'
offer_congratulations_message = '.propositionMessage>a>h3'

# Old Timer
add_old_timer_vehicle_details_page_make_input = 'input#quote-risk-automobile-make-text'
add_old_timer_vehicle_details_page_model_input = 'input#quote-risk-automobile-model-text'
add_old_timer_vehicle_details_page_version_input = 'input#quote-risk-automobile-version-text'
add_old_timer_vehicle_details_page_vehicle_type_dropdown = '#quote-risk-automobile-type-select'
add_old_timer_vehicle_details_page_vehicle_type_dropdown_tuple = ('#arg_oldtimer_private_car',)
# add_old_timer_vehicle_details_page_power_input = 'input#quote-risk-automobile-power-text'
add_old_timer_vehicle_details_page_first_use_date_input = 'input#quote-risk-automobile-first-use-date-date_input'
add_old_timer_vehicle_details_page_number_of_seats_input = 'input#quote-risk-automobile-seats-positions-number'
add_old_timer_vehicle_details_page_registration_number_input = 'input#quote-risk-automobile-registration-number-text'
add_old_timer_vehicle_details_page_chassis_number_input = 'input#quote-risk-automobile-serial-number-text'

add_old_timer_vehicle_details_page_registration_type_options_tuple = add_car_vehicle_details_page_registration_type_options_tuple
add_old_timer_vehicle_details_page_fuel_type_options_tuple = add_car_vehicle_details_page_fuel_type_options_tuple
add_old_timer_vehicle_details_page_usage_type_options_tuple = add_car_vehicle_details_page_usage_type_options_tuple

add_old_timer_claim_history_page_add_claim_button = add_car_claim_history_page_add_claim_button
add_old_timer_add_claim_page_nature_dropdown = add_car_add_claim_page_nature_dropdown
add_old_timer_add_claim_page_nature_dropdown_tuple = add_car_add_claim_page_nature_dropdown_tuple
add_old_timer_add_claim_page_date_input = add_car_add_claim_page_date_input
add_old_timer_add_claim_page_liability_dropdown = add_car_add_claim_page_liability_dropdown
add_old_timer_add_claim_page_liability_dropdown_tuple = add_car_add_claim_page_liability_dropdown_tuple
add_old_timer_add_claim_page_driver_type_dropdown = add_car_add_claim_page_driver_type_dropdown
add_old_timer_add_claim_page_driver_type_dropdown_tuple = add_car_add_claim_page_driver_type_dropdown_tuple
add_old_timer_add_claim_page_driver_date_of_birth_input = add_car_add_claim_page_driver_date_of_birth_input
add_old_timer_add_claim_page_joker_used_options_tuple = add_car_add_claim_page_joker_used_options_tuple
add_old_timer_add_claim_page_amount_input = add_car_add_claim_page_amount_input
add_old_timer_add_claim_page_risk_fully_repaired_options_tuple = add_car_add_claim_page_risk_fully_repaired_options_tuple
add_old_timer_add_claim_page_ok_button = add_car_add_claim_page_ok_button

add_old_timer_claim_history_page_next_button = 'a#undefined-4-anchor'
add_old_timer_add_driver_next_button = 'a#undefined-2-anchor'
add_old_timer_add_driver_ok_button = '#mat-dialog-3 button#modal__ok'
add_old_timer_add_driver_driver_license_page_license_date_input = add_car_add_driver_driver_license_page_license_date_input
add_old_timer_vehicle_details_page_power_input = 'input#quote-risk-automobile-power-number'
add_old_timer_drivers_page_add_driver_button = 'button#add-driver-undefined-button'
add_old_timer_add_driver_driver_license_page_next_button = '#cdk-accordion-child-12 a#undefined-3-anchor'
add_old_timer_add_driver_address_page_next_button = '#cdk-accordion-child-13 #undefined-4-anchor'
add_old_timer_add_driver_contact_page_next_button = '#cdk-accordion-child-14 #undefined-5-anchor'
add_old_timer_add_driver_page_ok_button = add_car_add_driver_page_ok_button
add_old_timer_drivers_page_next_button = 'a#undefined-5-anchor'
add_old_timer_previous_insurer_page_next_button = 'a#undefined-6-anchor'
add_old_timer_risk_background_page_certificates_options_tuple = (
    'button#eval-ques-ans-question-answer-answer-boolean-toggle__FALSE_00-button',
    'button#eval-ques-ans-question-answer-answer-boolean-toggle__TRUE_00-button'
)
add_old_timer_risk_background_page_certificates_next_button = '#undefined-7-anchor'
add_old_timer_page_ok_button = '#mat-dialog-2 button#modal__ok'
add_old_timer_coverage_tariffs_page_options_tuple = add_car_coverage_tariffs_page_options_tuple

add_old_timer_vehicle_details_page_next_button = add_car_vehicle_details_page_next_button
add_old_timer_add_driver_add_driver_page_next_button = 'a#undefined-2-anchor'
add_old_timer_driver_license_page_license_id_input = add_car_add_driver_driver_license_page_license_id_input
add_old_timer_add_driver_driver_license_page_license_category_options_tuple = add_car_add_driver_driver_license_page_license_category_options_tuple
add_old_timer_risk_background_page_next_certificates_button = 'a#undefined-8-anchor'
billing_page_billing_renewal_day_input = 'input#billing-billing-main-due-day-text'
billing_page_billing_renewal_month_input = 'input#billing-billing-main-due-month-text'

# Add Van
add_van_vehicle_details_page_referential_vehicle_search_button = add_car_vehicle_details_page_referential_vehicle_search_button
add_van_preferential_vehicle_search_page_make_input = add_car_preferential_vehicle_search_page_make_input
add_van_preferential_vehicle_search_page_model_input = add_car_preferential_vehicle_search_page_model_input
add_van_preferential_vehicle_search_page_search_button = add_car_preferential_vehicle_search_page_search_button
add_van_vehicle_details_page_vehicle_type_dropdown = '#quote-risk-van-type-select'
add_van_vehicle_details_page_vehicle_type_dropdown_tuple = '#quote-risk-van-type-select_@index@'
add_van_vehicle_details_page_first_use_date_input = 'input#quote-risk-van-first-use-date-date_input'
add_van_vehicle_details_page_number_of_seats_input = 'input#quote-risk-van-seats-positions-number'
add_van_vehicle_details_page_registration_number_input = 'input#quote-risk-van-registration-number-text'
add_van_vehicle_details_page_chassis_number_input = 'input#quote-risk-van-serial-number-text'

add_van_vehicle_details_page_registration_type_options_tuple = (
    'button[id="quote-risk-van-registration-type-toggle_Euro Plate_-button"]',
    'button[id="quote-risk-van-registration-type-toggle_Normal Plate_-button"]',
    'button[id="quote-risk-van-registration-type-toggle_BZ Plate_-button"]',
    'button[id="quote-risk-van-registration-type-toggle_Trader Plate_-button"]',
    'button[id="quote-risk-van-registration-type-toggle_Transit Plate_-button"]'
)

add_van_vehicle_details_page_fuel_type_options_tuple = (
    'button[id="quote-risk-van-fuel-type-toggle_Diesel Oil_-button"]',
    'button[id="quote-risk-van-fuel-type-toggle_Electric_-button"]',
    'button[id="quote-risk-van-fuel-type-toggle_Hybrid (Diesel Oil / Electricity)_-button"]',
    'button[id="quote-risk-van-fuel-type-toggle_Hybrid (Petrol / Electricity)_-button"]',
    'button[id="quote-risk-van-fuel-type-toggle_Hydrogen_-button"]',
    'button[id="quote-risk-van-fuel-type-toggle_LPG_-button"]',
    'quote-risk-van-fuel-type-toggle_Natural Gas for Vehicles_-button',
    'button[id="quote-risk-van-fuel-type-toggle_Petrol_-button"]',
    'button[id="quote-risk-van-fuel-type-toggle_Unknown_-button"]'
)

add_van_vehicle_details_page_usage_type_options_tuple = (
    'button[id="quote-risk-van-usage-type-toggle_Business Rounds_-button"]',
    'button[id="quote-risk-van-usage-type-toggle_Craftsman_-button"]',
    'button[id="quote-risk-van-usage-type-toggle_Private_-button"]',
    'button[id="quote-risk-van-usage-type-toggle_Private - Business Journeys_-button"]',
    'button[id="quote-risk-van-usage-type-toggle_Taxi_-button"]',
    'button[id="quote-risk-van-usage-type-toggle_Transport of goods_-button"]',
    'button[id="quote-risk-van-usage-type-toggle_Professional_-button"]'
)

add_van_vehicle_details_page_next_button = 'a#undefined-3-anchor'
add_van_risk_evaluation_page_vehicle_value_input = 'input#quote-risk-van-sum-insured-number'
add_van_risk_evaluation_page_accessories_equipment_value_input = 'input#quote-risk-van-accessoires-sum-number'
add_van_risk_evaluation_page_next_button = 'a#undefined-4-anchor'
add_van_claim_history_page_add_claim_button = add_car_claim_history_page_add_claim_button
add_van_add_claim_page_nature_dropdown = add_car_add_claim_page_nature_dropdown
add_van_add_claim_page_nature_dropdown_tuple = add_car_add_claim_page_nature_dropdown_tuple
add_van_add_claim_page_date_input = add_car_add_claim_page_date_input
add_van_add_claim_page_liability_dropdown = add_car_add_claim_page_liability_dropdown
add_van_add_claim_page_liability_dropdown_tuple = add_car_add_claim_page_liability_dropdown_tuple
add_van_add_claim_page_driver_type_dropdown = add_car_add_claim_page_driver_type_dropdown
add_van_add_claim_page_driver_type_dropdown_tuple = add_car_add_claim_page_driver_type_dropdown_tuple
add_van_add_claim_page_driver_date_of_birth_input = add_car_add_claim_page_driver_date_of_birth_input
add_van_add_claim_page_joker_used_options_tuple = add_car_add_claim_page_joker_used_options_tuple
add_van_add_claim_page_amount_input = add_car_add_claim_page_amount_input
add_van_add_claim_page_risk_fully_repaired_options_tuple = add_car_add_claim_page_risk_fully_repaired_options_tuple
add_van_add_claim_page_ok_button = add_car_add_claim_page_ok_button
add_van_claim_history_page_next_button = add_car_claim_history_page_next_button
add_van_drivers_page_add_driver_button = add_car_drivers_page_add_driver_button
add_van_add_driver_page_next_button = 'a#undefined-2-anchor'
add_van_add_driver_driver_license_page_license_date_input = add_car_add_driver_driver_license_page_license_date_input
add_van_add_driver_driver_license_page_license_category_options_tuple = add_car_add_driver_driver_license_page_license_category_options_tuple
add_van_add_driver_driver_license_page_next_button = add_car_add_driver_driver_license_page_next_button
add_van_add_driver_address_page_next_button = add_car_add_driver_address_page_next_button
add_van_add_driver_page_ok_button = add_car_add_driver_page_ok_button
add_van_drivers_page_next_button = add_car_drivers_page_next_button
add_van_add_driver_contact_page_next_button = add_car_add_driver_contact_page_next_button
add_van_previous_insurer_page_next_button = add_car_previous_insurer_page_next_button
add_van_risk_background_page_certificates_options_tuple = add_car_risk_background_page_certificates_options_tuple
add_van_vehicle_details_page_referential_search_button = '#quote-risk-undefined-anchor'
add_van_vehicle_details_page_make_input = add_old_timer_vehicle_details_page_make_input
add_van_vehicle_details_page_model_input = add_old_timer_vehicle_details_page_model_input
add_van_vehicle_details_page_version_input = add_old_timer_vehicle_details_page_version_input
add_van_vehicle_details_page_power_input = add_old_timer_vehicle_details_page_power_input
add_van_driver_license_page_license_id_input = add_car_add_driver_driver_license_page_license_id_input
add_van_risk_background_page_certificates_next_button = 'a#undefined-8-anchor'
add_van_page_ok_button = 'button#modal__ok'
add_van_coverage_tariffs_page_options_tuple = add_car_coverage_tariffs_page_options_tuple

# Truck Camper
add_truck_camper_vehicle_details_page_vehicle_type_dropdown = '#quote-risk-truck-camper-type-select'
add_truck_camper_vehicle_details_page_vehicle_type_dropdown_tuple = ('#quote-risk-truck-camper-type-select_0',)

add_truck_camper_vehicle_details_page_make_input = 'input#quote-risk-truck-camper-make-text'
add_truck_camper_vehicle_details_page_model_input = 'input#quote-risk-truck-camper-model-text'
add_truck_camper_vehicle_details_page_power_input = 'input#quote-risk-truck-camper-power-number'
add_truck_camper_vehicle_details_page_first_use_date_input = 'input#quote-risk-truck-camper-first-use-date-date_input'
add_truck_camper_vehicle_details_page_number_of_seats_input = 'input#quote-risk-truck-camper-seats-positions-number'
add_truck_camper_vehicle_details_page_registration_number_input = 'input#quote-risk-truck-camper-registration-number-text'
add_truck_camper_vehicle_details_page_chassis_number_input = 'input#quote-risk-truck-camper-serial-number-text'
add_truck_camper_add_driver_address_page_next_button = add_car_add_driver_address_page_next_button
add_truck_camper_add_driver_page_ok_button = add_car_add_driver_page_ok_button
add_truck_camper_drivers_page_next_button = 'a#undefined-6-anchor'
add_truck_camper_risk_background_page_certificates_next_button = add_van_risk_background_page_certificates_next_button

add_truck_camper_vehicle_details_page_registration_type_options_tuple = (
    'button[id="quote-risk-truck-camper-registration-type-toggle_Euro Plate_-button"]',
    'button[id="quote-risk-truck-camper-registration-type-toggle_Normal Plate_-button"]',
    'button[id="quote-risk-truck-camper-registration-type-toggle_BZ Plate_-button"]',
    'button[id="quote-risk-truck-camper-registration-type-toggle_Trader Plate_-button"]',
    'button[id="quote-risk-truck-camper-registration-type-toggle_Transit Plate_-button"]'
)

add_truck_camper_vehicle_details_page_fuel_type_options_tuple = (
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Bio Ethanol_-button"]',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Diesel Oil_-button"]',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Electric_-button"]',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Hybrid / Micro Hybrid Diesel Oil_-button"]',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Hybrid / Micro Hybrid Petrol_-button"]',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_LPG_-button"]',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Natural Gas for Vehicles_-button"]',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Petrol_-button"]',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Plug-in Hybrid Diesel Oil_-button"]',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Plug-in Hybrid Petrol_-button"]'
)

add_truck_camper_vehicle_details_page_usage_type_options_tuple = (
    'button#quote-risk-camping-car-usage-type-toggle_Professional_-button',
    'button#quote-risk-camping-car-usage-type-toggle_Private_-button'
)

add_truck_camper_coverage_tariffs_page_options_tuple = '#package-selected-checkbox0@index@'

add_truck_camper_risk_background_page_certificates_options_tuple = add_car_risk_background_page_certificates_options_tuple

add_truck_camper_risk_evaluation_page_vehicle_value_input = 'input#quote-risk-truck-camper-sum-insured-number'
add_truck_camper_risk_evaluation_page_accessories_equipment_value_input = 'input#quote-risk-truck-camper-accessoires-sum-number'
add_truck_camper_risk_evaluation_page_next_button = 'a#undefined-4-anchor'
add_truck_camper_claim_history_page_next_button = 'a#undefined-5-anchor'
add_truck_camper_add_driver_driver_details_page_next_button = add_car_add_driver_driver_details_page_next_button
add_truck_camper_add_driver_driver_license_page_next_button = '#cdk-accordion-child-13 a#undefined-3-anchor'
add_truck_camper_vehicle_details_page_next_button = add_car_vehicle_details_page_next_button
add_truck_camper_claim_history_page_add_claim_button = add_car_claim_history_page_add_claim_button
add_truck_camper_add_claim_page_nature_dropdown = add_car_add_claim_page_nature_dropdown
add_truck_camper_add_claim_page_nature_dropdown_tuple = add_car_add_claim_page_nature_dropdown_tuple
add_truck_camper_add_claim_page_date_input = add_car_add_claim_page_date_input
add_truck_camper_add_claim_page_liability_dropdown = add_car_add_claim_page_liability_dropdown
add_truck_camper_add_claim_page_liability_dropdown_tuple = add_car_add_claim_page_liability_dropdown_tuple
add_truck_camper_add_claim_page_driver_type_dropdown = add_car_add_claim_page_driver_type_dropdown
add_truck_camper_add_claim_page_driver_type_dropdown_tuple = add_car_add_claim_page_driver_type_dropdown_tuple
add_truck_camper_add_claim_page_driver_date_of_birth_input = add_car_add_claim_page_driver_date_of_birth_input
add_truck_camper_add_claim_page_joker_used_options_tuple = add_car_add_claim_page_joker_used_options_tuple
add_truck_camper_add_claim_page_amount_input = add_car_add_claim_page_amount_input
add_truck_camper_add_claim_page_risk_fully_repaired_options_tuple = add_car_add_claim_page_risk_fully_repaired_options_tuple
add_truck_camper_add_claim_page_ok_button = add_car_add_claim_page_ok_button
add_truck_camper_drivers_page_add_driver_button = add_car_drivers_page_add_driver_button
add_truck_camper_add_driver_driver_license_page_license_id_input = add_car_add_driver_driver_license_page_license_id_input
add_truck_camper_add_driver_driver_license_page_license_date_input = add_car_add_driver_driver_license_page_license_date_input
add_truck_camper_add_driver_driver_license_page_license_category_options_tuple = add_car_add_driver_driver_license_page_license_category_options_tuple
add_truck_camper_add_driver_contact_page_next_button = add_car_add_driver_contact_page_next_button
add_truck_camper_previous_insurer_page_next_button = add_car_previous_insurer_page_next_button
add_truck_camper_page_ok_button = add_old_timer_page_ok_button
add_truck_camper_risk_background_page_next_button = add_car_risk_background_page_next_button


