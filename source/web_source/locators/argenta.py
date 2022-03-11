# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 09:05:01 2022

@author: bbalushev
"""


""" This file contains all locators related with 'Argenta' UI flow """

# ================================================ Mandatory elements ================================================
# Loading Div (mandatory)
loading_page_element = '.loadingDiv'

# Dictionary which contains all dropdowns values
dropdown_lists = {
    'add_car_vehicle_details_page_vehicle_type': ('minibus', 'passenger car', 'station wagon or all terrain vehicle'),
    'add_motorcycle_vehicle_details_page_vehicle_type': ('motorcycle', 'three wheel motorcycle', 'four wheel motorcycle'),
    'add_moped_vehicle_details_page_vehicle_type': ('class a', 'class b', 'three wheel moped', 'four wheel moped', 'speed pedelec'),
    'quote_insurance': ('home', 'car', 'family', 'motorcycle'),
    'offer_insurance': ('home', 'car', 'family', 'motorcycle'),
    'documents_insurance': ('home', 'car', 'family', 'motorcycle'),
    'add_car_add_claim_nature': ('accident', 'corporal claim', 'damage to third', 'fire', 'glass breakage',
                                 'material claim', 'other', 'parking', 'theft'),
    'add_car_add_claim_liability': ('0 percent', '50 percent', '100 percent'),
    'add_car_add_claim_driver_type': ('primary', 'secondary', 'occasional'),
    'add_old_timer_vehicle_details_page_vehicle_type': ('old timer private car',),
    'add_truck_camper_vehicle_type': ('camping car',),
    'add_home_home_details_page_building_year': ('before 1995', '1995 - 1999', '2000 - 2004', '2005 - 2009',
                                                 '2010 - 2014', '2015 - 2019', '2020 - 2020', '2021 - 2021',
                                                 '2022 - 2022'),
    'offer_add_home_home_details_page_building_year': ('before 1995', '1995 - 1999', '2000 - 2004', '2005 - 2009',
                                                       '2010 - 2014', '2015 - 2019', '2020 - 2020', '2021 - 2021',
                                                       '2022 - 2022')
}

# Dictionary which contains all options area values
options_area_lists = {
    'add_car_vehicle_details_page_registration_type': ('euro plate', 'normal plate', 'bz plate', 'trader plate', 'transit plate'),
    'add_motorcycle_vehicle_details_page_registration_type': ('euro plate', 'normal plate', 'bz plate', 'trader plate', 'transit plate'),
    'add_moped_vehicle_details_page_registration_type': ('euro plate', 'normal plate', 'bz plate', 'trader plate', 'transit plate'),
    'add_truck_camper_registration_type': ('euro plate', 'normal plate', 'bz plate', 'trader plate', 'transit plate'),
    'add_car_vehicle_details_page_fuel_type': ('bio ethanol', 'diesel oil', 'electric',
                                               'hybrid / micro hybrid diesel oil', 'hybrid / micro hybrid petrol',
                                               'lpg', 'natural gas for vehicles', 'petrol',
                                               'plug-in hybrid diesel oil', 'plug-in hybrid petrol'),
    'add_motorcycle_vehicle_details_page_fuel_type': ('diesel oil', 'electric', 'natural gas for vehicles', 'petrol'),
    'add_moped_vehicle_details_page_fuel_type': ('diesel oil', 'electric', 'natural gas for vehicles', 'petrol'),
    'add_truck_camper_fuel_type': ('diesel oil', 'electric', 'natural gas for vehicles', 'petrol'),
    'add_car_vehicle_details_page_usage_type': ('private', 'professional'),
    'add_motorcycle_vehicle_details_page_usage_type': ('private', 'professional'),
    'add_moped_vehicle_details_page_usage_type': ('private', 'professional'),
    'add_truck_camper_usage_type': ('professional', 'private'),
    'home_branch_owner': ('nc', 'fc'),
    'add_family_page_family_situation': ('family', '60 plus', 'single'),
    'add_car_add_claim_joker_used': ('no', 'yes'),
    'add_car_add_claim_risk_fully_repaired': ('no', 'yes'),
    'automobile_driver_quote_owner_as_driver': ('no', 'yes'),
    'add_car_risk_background_page_certificates': ('no', 'yes'),
    'add_home_home_details_page_classified_property': ('no', 'yes'),
    'offer_add_home_home_details_page_classified_property': ('no', 'yes'),
    'add_home_home_details_page_irregular_habitation': ('no', 'yes'),
    'offer_add_home_home_details_page_irregular_habitation': ('no', 'yes'),
    'add_home_home_details_page_flammable_construction': ('no', 'yes'),
    'offer_add_home_home_details_page_flammable_construction': ('no', 'yes'),
    'offer_add_car_risk_background_page_certificates': ('no', 'yes'),
    'offer_add_old_timer_risk_background_page_certificates': ('no', 'yes'),
    'offer_add_truck_camper_risk_background_page_certificates': ('no', 'yes'),
    'automobile_driver_driver_type': ('primary', 'secondary', 'occasional'),
    'add_car_add_driver_driver_license_page_license_category': ('b', 'be', 'c', 'ce', 'c1', 'c1e',
                                                                'd', 'de', 'd1', 'd1e'),
    'offer_add_car_add_driver_driver_license_page_license_category': ('b', 'be', 'c', 'ce', 'c1', 'c1e',
                                                                      'd', 'de', 'd1', 'd1e'),
    'add_motorcycle_add_driver_driver_license_page_license_category': ('a', 'a1', 'a2'),
    'offer_add_motorcycle_add_driver_driver_license_page_license_category': ('a', 'a1', 'a2'),
    'add_car_coverage_tariffs_page': ('partial omnium', 'own damage basic', 'own damage comfort', 'driver plus',
                                      'legal assistance safe', 'tmc insured'),
    'offer_add_car_coverage_tariffs_page': ('civil liability', 'partial omnium', 'own damage basic', 'own damage comfort', 'driver plus',
                                            'legal assistance safe', 'tmc insured'),
    'offer_add_truck_camper_coverage_tariffs_page': ('civil liability', 'partial omnium', 'own damage basic',
                                                     'own damage comfort', 'driver plus', 'legal assistance safe'),
    'add_old_timer_coverage_tariffs_page': ('civil liability', 'free assistance', 'legal assistance safe'),
    'offer_add_old_timer_coverage_tariffs_page': ('civil liability', 'free assistance', 'legal assistance safe'),
    'billing_page_type': ('direct credit', 'direct debit'),
    'billing_page_frequency': ('monthly', 'quarterly', 'semi annual', 'annual'),
    'add_home_home_details_page_type': ('apartment', 'block', 'bungalow or cottage', 'commercial premises', 'house', 'mobile home'),
    'add_home_home_details_page_usage': ('owner occupant', 'owner non occupant', 'owner with block policy',
                                         'tenant of a full building', 'tenant of a part of building'),
    'add_home_home_details_page_alarm_system': ('certified system', 'no', 'yes'),
    'offer_add_home_home_details_page_alarm_system': ('certified system', 'no', 'yes'),
    'add_home_home_details_page_abutment': ('closed', 'half open', 'open'),
    'offer_add_home_home_details_page_abutment': ('closed', 'half open', 'open'),
    'add_home_home_details_page_habitation_usage': ('habitation only', 'habitation and independent activity',
                                                    'independent and other commercial activity', 'garage',
                                                    'warehouse or stockroom'),
    'offer_add_home_home_details_page_habitation_usage': ('habitation only', 'habitation and independent activity',
                                                          'independent and other commercial activity', 'garage',
                                                          'warehouse or stockroom'),
    'add_motorcycle_coverage_tariffs_page_coverages': ('civil liability', 'free assistance',
                                                       'legal assistance basis', 'legal assistance safe'),
    'offer_add_motorcycle_coverage_tariffs_page_coverages': ('civil liability', 'free assistance',
                                                             'legal assistance basis', 'legal assistance safe'),
    'offer_add_home_risk_evaluation_page_evaluation_method': ('gim', 'by questions', 'manual'),
    'offer_add_family_add_home_risk_evaluation_page_evaluation_method': ('gim', 'by questions', 'manual')
}

# ===================================================== Locators =====================================================

# OmniChannel login page
login_username = 'input#authUsername'
login_password = 'input#authPassword'
login_button = 'button#loginBtn'

# Send to the back office page
submit_documents_button = 'button#create-documents-button'

# Argenta main page
quote_insurance_dropdown = 'div#navbarSupportedContent:nth-of-type(2)'
quote_insurance_dropdown_tuple = (
    '#cdk-overlay-0>div>div>button:nth-of-type(1):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(2):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(3):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(4):not(aria-disabled)'
)

offer_insurance_dropdown = 'div#navbarSupportedContent:nth-of-type(4)'
offer_insurance_dropdown_tuple = (
    '#cdk-overlay-0>div>div>button:nth-of-type(1):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(2):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(3):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(4):not(aria-disabled)'
)

search_person_link = 'a#person-search-undefined-anchor'
search_organization_link = 'a#organization-search-undefined-anchor'

# Distributor search page
general_info_description = '#toggle-0 mat-panel-description'
distributor_id_search_field = 'input#distributor-search-distributor-id-text'
distributor_button_reset = 'button#btnreset'
distributor_button_search = 'button#btnfilter'
distributor_id_tuple = '#_@index@__DISTRIBUTOR_ID'
distributor_total_count = '.paginator-totalcount'
distributor_button_ok = 'button#modal__ok'
distributor_button_cancel = 'button#modal__close'

# Quote contract information page
effective_date_input = 'input#quote-quote-contract-start-date-date_input'
frequency_dropdown = '#quote-quote-frequency-select'
frequency_dropdown_tuple = '#quote-quote-frequency-select_@index@'
language_dropdown = '#quote-quote-language-select'
language_dropdown_tuple = '#quote-quote-language-select_@index@'
person_radio_button = '#quote-owner-quote-owner-type-radio_Person_'
organization_radio_button = '#quote-owner-quote-owner-type-radio_Organization_'
civility_dropdown = '#quote-owner-quote-owner-person-title-select:not(aria-disabled)'
civility_dropdown_tuple = (
    '#mister:not(aria-disabled)',
    '#arg_other:not(aria-disabled)',
    '#mrs:not(aria-disabled)'
)
name_search_input = 'input#quote-owner-quote-owner-name-autocomplete'
search_owner_button = '#search-owner-undefined-anchor'
search_owner_page_first_name_input = 'input#person-search-first-name-text'
search_owner_page_last_name_input = 'input#person-search-last-name-text'
search_owner_page_client_id_input = 'input#person-search-client-identifier-text'
search_owner_page_date_of_birth_input = 'input#person-search-client-date-date_input'

search_owner_page_search_button = 'button#btnfilter'
search_owner_page_reset_button = 'button#btnreset'
quote_first_name_input = 'input#quote-owner-quote-owner-first-name-autocomplete'
date_of_birth_input = 'input#quote-owner-quote-owner-birth-date-date_input'
legal_form_dropdown = '#quote-owner-quote-owner-legal-form-select .mat-select-value'
legal_form_dropdown_tuple = '#quote-owner-quote-owner-legal-form-select_@index@'
owner_postal_code_input = 'input#quote-owner-postal-addresses-postal-address-postal-code-autocomplete'
postal_code_options_tuple = (
    '#mat-option-49',
    '#mat-option-50',
    '#mat-option-51',
    '#mat-option-52',
    '#mat-option-53'
)
city_input = 'input#quote-owner-postal-addresses-postal-address-city-name-autocomplete'
country_input = 'input#quote-owner-postal-addresses-postal-address-country-name-autocomplete'
street_name_input = 'input#quote-owner-postal-addresses-postal-address-street-name-autocomplete'
street_number_input = 'input#quote-owner-postal-addresses-postal-address-street-number-text'
box_number_input = 'input#quote-owner-postal-addresses-postal-address-box-number-text'
email_input = 'input#quote-owner-quote-owner-email-email'
phone_type_dropdown = '#quote-owner-quote-owner-phone-type-select'
phone_type_dropdown_tuple = '#quote-owner-quote-owner-phone-type-select_@index@'
phone_number_input = 'input#quote-owner-quote-owner-phone-text'
contract_info_tab_tuple = '#mat-expansion-panel-header-@index@'
risk_button = 'button#risk-management-undefined-button'
owner_prepopulate_icon = '#mat-expansion-panel-header-1>span>span'
address_prepopulate_icon = '#mat-expansion-panel-header-2>span>span'
contact_prepopulate_icon = '#mat-expansion-panel-header-3>span>span'

# Quote contract information page
add_car_button = 'button#add-auto-risk-undefined-button-modal'
add_old_timer_button = 'button#add-old-timer-risk-undefined-button-modal'
add_van_button = 'button#add-van-risk-undefined-button-modal'
add_truck_camper_button = 'button#add-campingcar-risk-undefined-button-modal'

branch_owner_tuple = (
    'button#reference-element-extension-element-value-toggle_0\,0\%_0-button',
    'button#reference-element-extension-element-value-toggle_0\,5\%_0-button',
    'button#reference-element-extension-element-value-toggle_1\,0\%_0-button',
    'button#reference-element-extension-element-value-toggle_1\,5\%_0-button',
    'button#reference-element-extension-element-value-toggle_2\,0\%_0-button',
    'button#reference-element-extension-element-value-toggle_2\,5\%_0-button',
    'button#reference-element-extension-element-value-toggle_3\,0\%_0-button',
    'button#reference-element-extension-element-value-toggle_3\,5\%_0-button',
    'button#reference-element-extension-element-value-toggle_4\,0\%_0-button',
    'button#reference-element-extension-element-value-toggle_4\,5\%_0-button',
    'button#reference-element-extension-element-value-toggle_5\,0\%_0-button',
    'button#reference-element-extension-element-value-toggle_5\,5\%_0-button',
    'button#reference-element-extension-element-value-toggle_6\,0\%_0-button',
    'button#reference-element-extension-element-value-toggle_6\,5\%_0-button',
    'button#reference-element-extension-element-value-toggle_7\,0\%_0-button',
    'button#reference-element-extension-element-value-toggle_7\,5\%_0-button',
    'button#reference-element-extension-element-value-toggle_8\,0\%_0-button',
    'button#reference-element-extension-element-value-toggle_8\,5\%_0-button',
    'button#reference-element-extension-element-value-toggle_9\,0\%_0-button',
    'button#reference-element-extension-element-value-toggle_9\,5\%_0-button',
    'button#reference-element-extension-element-value-toggle_10\,0\%_0-button'
)

contract_information_button = 'button#contract-info-undefined-button'
coverage_tariffs_button = 'button#coverages-tariffs-undefined-button'
referential_first_search_result = '#_0'
billing_button = 'button#billing-undefined-button'

# Billing page
billing_page_type_options_tuple = (
    'button#billing-billing-payment-type-toggle_Direct\ Credit_-button',
    'button#billing-billing-payment-type-toggle_Direct\ Debit_-button'
)
billing_page_frequency_options_tuple = (
    'button#billing-billing-frequency-toggle_Monthly_-button',
    'button#billing-billing-frequency-toggle_Quaterly_-button',
    'button#billing-billing-frequency-toggle_Semi-Annual_-button',
    'button#billing-billing-frequency-toggle_Annual_-button'
)
billing_renewal_day_input = 'input#billing-billing-main-due-day-text'
billing_renewal_month_input = 'input#billing-billing-main-due-month-text'
risk_acceptance_button = 'button#risk-acceptance-undefined-button'

# Add Car page
add_car_vehicle_details_page_referential_search_button = '#quote-risk-undefined-anchor'
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
    'button#quote-risk-automobile-registration-type-toggle_Euro\ Plate_-button',
    'button#quote-risk-automobile-registration-type-toggle_Normal\ Plate_-button',
    'button#quote-risk-automobile-registration-type-toggle_BZ\ Plate_-button',
    'button#quote-risk-automobile-registration-type-toggle_Trader\ Plate_-button',
    'button#quote-risk-automobile-registration-type-toggle_Transit\ Plate_-button'
)

add_car_vehicle_details_page_fuel_type_options_tuple = (
    'button#quote-risk-automobile-fuel-type-toggle_Bio\ Ethanol_-button',
    'button#quote-risk-automobile-fuel-type-toggle_Diesel\ Oil_-button',
    'button#quote-risk-automobile-fuel-type-toggle_Electric_-button',
    'button[id="quote-risk-automobile-fuel-type-toggle_Hybrid / Micro Hybrid Diesel Oil_-button"]',
    'button[id="quote-risk-automobile-fuel-type-toggle_Hybrid / Micro Hybrid Petrol_-button"]',
    'button#quote-risk-automobile-fuel-type-toggle_LPG_-button',
    'button[id="quote-risk-automobile-fuel-type-toggle_Natural Gas for Vehicles_-button"]',
    'button#quote-risk-automobile-fuel-type-toggle_Petrol_-button',
    'button[id="quote-risk-automobile-fuel-type-toggle_Plug-in Hybrid Diesel Oil_-button"]',
    'button[id="quote-risk-automobile-fuel-type-toggle_Plug-in Hybrid Petrol_-button"]'
)

add_car_vehicle_details_page_usage_type_options_tuple = (
    'button#quote-risk-automobile-usage-type-toggle_Private_-button',
    'button#quote-risk-automobile-usage-type-toggle_Professional_-button'
)

add_car_risk_evaluation_page_vehicle_value_input = 'input#quote-risk-automobile-sum-insured-number'
add_car_risk_evaluation_page_accessories_equipment_value_input = 'input#quote-risk-automobile-accessoires-sum-number'
add_car_risk_evaluation_page_next_button = '#undefined-4-anchor'
add_car_claim_history_page_add_claim_button = 'button#add-claim-undefined-button-modal'

add_car_add_claim_nature_dropdown = '#claim-history-property-recorded-claim-claim-type-select'
add_car_add_claim_nature_dropdown_tuple = ('#accident', '#corporal_responsible', '#damage_to_third', '#fire',
                                           '#glass_breakage', '#material_responsible', '#other', '#parking', '#theft')

add_car_add_claim_date_input = 'input#claim-history-property-recorded-claim-date-date_input'

add_car_add_claim_liability_dropdown = '#claim-history-property-recorded-claim-liability-select'
add_car_add_claim_liability_dropdown_tuple = '#claim-history-property-recorded-claim-liability-select_@index@'

add_car_add_claim_driver_type_dropdown = '#claim-history-property-recorded-claim-driver-type-select'
add_car_add_claim_driver_type_dropdown_tuple = '#claim-history-property-recorded-claim-driver-type-select_@index@'

add_car_add_claim_driver_date_of_birth_input = 'input#claim-history-property-recorded-claim-driver-birth-date-date_input'

add_car_add_claim_joker_used_options_tuple = (
    'button#claim-history-property-recorded-claim-joker-used-toggle__FALSE_-button',
    'button#claim-history-property-recorded-claim-joker-used-toggle__TRUE_-button'
)

add_car_add_claim_amount_input = 'input#claim-history-property-recorded-claim-amount-text'

add_car_add_claim_risk_fully_repaired_options_tuple = (
    'button#claim-history-property-recorded-claim-is-repaired-toggle__FALSE_-button',
    'button#claim-history-property-recorded-claim-is-repaired-toggle__TRUE_-button'
)

add_car_add_claim_ok_button = 'button:nth-of-type(1)#modal__ok'
add_car_claim_history_page_next_button = 'a#undefined-5-anchor'
add_car_drivers_page_add_driver_button = 'button#quote-drivers-undefined-button-modal'
add_car_add_driver_next_button = 'a#undefined-2-anchor'
add_car_add_driver_driver_license_page_license_date_input = 'input#driver-quote-driver-license-date-date_input'
add_car_add_driver_driver_license_page_license_category_options_tuple = (
    'button#driver-quote-driver-license-category-toggle_B_-button',
    'button#driver-quote-driver-license-category-toggle_BE_-button',
    'button#driver-quote-driver-license-category-toggle_C_-button',
    'button#driver-quote-driver-license-category-toggle_CE_-button',
    'button#driver-quote-driver-license-category-toggle_C1_-button',
    'button#driver-quote-driver-license-category-toggle_C1E_-button',
    'button#driver-quote-driver-license-category-toggle_D_-button',
    'button#driver-quote-driver-license-category-toggle_DE_-button',
    'button#driver-quote-driver-license-category-toggle_D1_-button',
    'button#driver-quote-driver-license-category-toggle_D1E_-button'
)
add_car_add_driver_driver_license_page_next_button = '#cdk-accordion-child-11 a#undefined-3-anchor'
add_car_add_driver_address_page_next_button = '#cdk-accordion-child-12 #undefined-4-anchor'
add_car_add_driver_page_ok_button = '#mat-dialog-3 button#modal__ok'
add_car_drivers_page_next_button = 'a#undefined-6-anchor'
add_car_risk_background_page_certificates_options_tuple = (
    'button#quote-eval-ques-ans-question-answer-answer-boolean-toggle__FALSE_00-button',
    'button#quote-eval-ques-ans-question-answer-answer-boolean-toggle__TRUE_00-button'
)
add_car_risk_background_page_certificates_next_button = 'a#undefined-7-anchor'
add_car_coverage_tariffs_page_options_tuple = (
    '#package-quote-product-component-selected-checkbox01',
    '#package-quote-product-component-selected-checkbox02',
    '#package-quote-product-component-selected-checkbox03',
    '#package-quote-product-component-selected-checkbox04',
    '#package-quote-product-component-selected-checkbox05',
    '#package-quote-product-component-selected-checkbox06'
)




automobile_driver_quote_owner_as_driver_options_tuple = (
    'button#driver-quote-driver-is-quote-owner-toggle__FALSE_-button',
    'button#driver-quote-driver-is-quote-owner-toggle__TRUE_-button'
)
automobile_driver_driver_type_options_tuple = (
    'button#driver-quote-driver-driver-type-toggle_Primary_-button',
    'button#driver-quote-driver-driver-type-toggle_Secondary_-button',
    'button#driver-quote-driver-driver-type-toggle_Occasional_-button'
)

# Add Old timer
add_old_timer_vehicle_details_page_make_input = 'input#quote-risk-automobile-make-text'
add_old_timer_vehicle_details_page_model_input = 'input#quote-risk-automobile-model-text'
add_old_timer_vehicle_details_page_version_input = 'input#quote-risk-automobile-version-text'
add_old_timer_vehicle_details_page_vehicle_type_dropdown = '#quote-risk-automobile-type-select'
add_old_timer_vehicle_details_page_vehicle_type_dropdown_tuple = ('#arg_oldtimer_private_car',)
add_old_timer_vehicle_details_page_power_input = 'input#quote-risk-automobile-power-text'
add_old_timer_vehicle_details_page_first_use_date_input = 'input#quote-risk-automobile-first-use-date-date_input'
add_old_timer_vehicle_details_page_number_of_seats_input = 'input#quote-risk-automobile-seats-positions-number'
add_old_timer_vehicle_details_page_registration_number_input = 'input#quote-risk-automobile-registration-number-text'
add_old_timer_vehicle_details_page_chassis_number_input = 'input#quote-risk-automobile-serial-number-text'
add_old_timer_claim_history_page_next_button = 'a#undefined-4-anchor'
add_old_timer_add_driver_next_button = 'a#undefined-2-anchor'
add_old_timer_add_driver_driver_license_page_next_button = '#cdk-accordion-child-10 a#undefined-3-anchor'
add_old_timer_add_driver_address_page_next_button = '#cdk-accordion-child-11 a#undefined-4-anchor'
add_old_timer_add_driver_ok_button = '#mat-dialog-3 button#modal__ok'
add_old_timer_drivers_page_next_button = 'a#undefined-5-anchor'
add_old_timer_risk_background_page_certificates_next_button = 'a#undefined-6-anchor'
add_old_timer_coverage_tariffs_page_options_tuple = '#package-quote-product-component-selected-checkbox0@index@'

# Add Van
van_vehicle_type_dropdown = '#quote-risk-van-type-select'
van_vehicle_type_dropdown_tuple = (
    '#arg_station_wagon_all_terrain',
    '#arg_truck'
)

first_use_date_input = 'same'
van_number_of_seats = 'input#quote-risk-van-seats-positions-number'
registration_number_input = 'issue'
chassis_number_input = 'issue'

# Add truck camper
add_truck_camper_vehicle_type_dropdown = '#quote-risk-truck-camper-type-select'
add_truck_camper_vehicle_type_dropdown_tuple = ('#quote-risk-truck-camper-type-select_0',)
add_truck_camper_make_input = 'input#quote-risk-truck-camper-make-text'
add_truck_camper_model_input = 'input#quote-risk-truck-camper-model-text'
add_truck_camper_power_input = 'input#quote-risk-truck-camper-power-number'
add_truck_camper_first_use_date_input = 'input#quote-risk-truck-camper-first-use-date-date_input'
add_truck_camper_number_of_seats_input = 'input#quote-risk-truck-camper-seats-positions-number'
add_truck_camper_registration_number_input = 'input#quote-risk-truck-camper-registration-number-text'
add_truck_camper_chassis_number_input = 'input#quote-risk-truck-camper-serial-number-text'
add_truck_camper_add_driver_address_page_next_button = '#cdk-accordion-child-12 #undefined-4-anchor'
add_truck_camper_add_driver_page_ok_button = '#mat-dialog-3 button#modal__ok'
add_truck_camper_drivers_page_next_button = 'a#undefined-6-anchor'
add_truck_camper_risk_background_page_certificates_next_button = 'a#undefined-7-anchor'

add_truck_camper_registration_type_options_tuple = (
    'button#quote-risk-truck-camper-registration-type-toggle_Euro\ Plate_-button',
    'button#quote-risk-truck-camper-registration-type-toggle_Normal\ Plate_-button',
    'button#quote-risk-truck-camper-registration-type-toggle_BZ\ Plate_-button',
    'button#quote-risk-truck-camper-registration-type-toggle_Trader\ Plate_-button',
    'button#quote-risk-truck-camper-registration-type-toggle_Transit\ Plate_-button'
)

add_truck_camper_fuel_type_options_tuple = (
    'button#quote-risk-truck-camper-fuel-type-toggle_Bio\ Ethanol_-button',
    'button#quote-risk-truck-camper-fuel-type-toggle_Diesel\ Oil_-button',
    'button#quote-risk-truck-camper-fuel-type-toggle_Electric_-button',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Hybrid / Micro Hybrid Diesel Oil_-button"]',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Hybrid / Micro Hybrid Petrol_-button"]',
    'button#quote-risk-truck-camper-fuel-type-toggle_LPG_-button',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Natural Gas for Vehicles_-button"]',
    'button#quote-risk-truck-camper-fuel-type-toggle_Petrol_-button',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Plug-in Hybrid Diesel Oil_-button"]',
    'button[id="quote-risk-truck-camper-fuel-type-toggle_Plug-in Hybrid Petrol_-button"]'
)

add_truck_camper_usage_type_options_tuple = (
    'button#quote-risk-camping-car-usage-type-toggle_Professional_-button',
    'button#quote-risk-camping-car-usage-type-toggle_Private_-button'
)

add_truck_camper_risk_evaluation_page_vehicle_value_input = 'input#quote-risk-truck-camper-sum-insured-number'
add_truck_camper_risk_evaluation_page_accessories_equipment_value_input = 'input#quote-risk-truck-camper-accessoires-sum-number'
add_truck_camper_risk_evaluation_page_next_button = 'a#undefined-4-anchor'
add_truck_camper_claim_history_page_next_button = 'a#undefined-5-anchor'
add_truck_camper_add_driver_driver_details_next_button = 'a#undefined-2-anchor'
add_truck_camper_add_driver_driver_license_page_next_button = '#cdk-accordion-child-11 a#undefined-3-anchor'

next_button = 'a#undefined-3-anchor'
reset_button = 'button#modal__custom'
ok_button = 'button#modal__ok'

# Home insurance
add_home_button = 'button#add-home-risk-undefined-button-modal'
add_family_button = 'button#add-family-risk-undefined-button-modal'
add_home_address_page_next_button = 'a#undefined-2-anchor'
add_home_home_details_page_type_options_tuple = (
    'button#quote-risk-dwelling-type-toggle_Appartment_-button',
    'button#quote-risk-dwelling-type-toggle_Block_-button',
    'button[id="quote-risk-dwelling-type-toggle_Bungalow / Cottage_-button"]',
    'button[id="quote-risk-dwelling-type-toggle_Commercial Premises_-button"]',
    'button#quote-risk-dwelling-type-toggle_House_-button',
    'button[id="quote-risk-dwelling-type-toggle_Mobile Home_-button"]'
)
add_home_home_details_page_usage_options_tuple = (
    'button[id="quote-risk-dwelling-usage-type-toggle_Owner Occupant_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Owner Non Occupant_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Owner with Block Policy_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Tenant of a Full Building_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Tenant of a part of Building_-button"]'
)
add_home_home_details_page_bedrooms_input = 'input#mat-input-32'
add_home_home_details_page_bathrooms_input = 'input#mat-input-33'
add_home_home_details_page_alarm_system_options_tuple = (
    'button[id="quote-risk-dwelling-alarm-system-toggle_Certified system_-button"]',
    'button[id="quote-risk-dwelling-alarm-system-toggle_No_-button"]',
    'button[id="quote-risk-dwelling-alarm-system-toggle_Yes_-button"]'
)
add_home_home_details_page_classified_property_options_tuple = (
    'button#quote-risk-dwelling-monument-toggle__FALSE_-button',
    'button#quote-risk-dwelling-monument-toggle__TRUE_-button'
)
add_home_home_details_page_abutment_options_tuple = (
    'button#quote-risk-dwelling-abutment-toggle_Closed_-button',
    'button#quote-risk-dwelling-abutment-toggle_Half\ Open_-button',
    'button#quote-risk-dwelling-abutment-toggle_Open_-button'
)
add_home_home_details_page_building_year_dropdown = '#quote-risk-dwelling-construction-year-select'
add_home_home_details_page_building_year_dropdown_tuple = '#quote-risk-dwelling-construction-year-select_@index@'
add_home_home_details_page_habitation_usage_options_tuple = (
    'button[id="risk-ref-element-extension-element-value-toggle_Habitation only_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Habitation and independant activity_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Independent and other commercial activity_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Garage_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Warehouse/Stockroom_0-button"]'
)
add_home_home_details_page_irregular_habitation_options_tuple = (
    'button#risk-ref-element-extension-element-value-toggle_No_1-button',
    'button#risk-ref-element-extension-element-value-toggle_Yes_1-button'
)
add_home_home_details_page_flammable_construction_options_tuple = (
    'button#risk-ref-element-extension-element-value-toggle_No_2-button',
    'button#risk-ref-element-extension-element-value-toggle_Yes_2-button'
)
add_home_home_details_page_next_button = 'a#undefined-3-anchor'


home_postal_code_input = 'input#quote-risk-preferred-address-postal-address-postal-code-autocomplete'
home_city_input = 'input#quote-risk-preferred-address-postal-address-city-name-autocomplete'
home_street_name_input = 'input#quote-risk-preferred-address-postal-address-street-name-autocomplete'
home_street_number_input = 'input#quote-risk-preferred-address-postal-address-street-number-text'
home_box_number_input = 'input#quote-risk-preferred-address-postal-address-box-number-text'

home_branch_owner_options_tuple = (
    'button#reference-element-extension-element-value-toggle_NC_0-button',
    'button#reference-element-extension-element-value-toggle_FC_0-button'
)

add_family_page_family_situation_options_tuple = (
    'button#quote-risk-family-family-situation-toggle_Family_-button',
    'button[id="quote-risk-family-family-situation-toggle_60+_-button"]',
    'button#quote-risk-family-family-situation-toggle_Single_-button'
)

# Coverage / Tariffs page
summary_button = 'button#summary-undefined-button'
submission_button = 'button#submission-undefined-button'
risk_acceptance_answer_button = 'button#ques-ans-item-question-answer-answer-boolean-toggle__FALSE_05-button'

# Summary page
proceed_to_offer_button = 'button#proceed-to-offer-undefined-button'
save_and_quit_button = 'button#save-quit-undefined-button'

# Motorcycle page
add_motorcycle_button = 'button#add-motorcycle-risk-undefined-button-modal'
add_moped_button = 'button#add-moped-risk-undefined-button-modal'

add_motorcycle_vehicle_details_page_make_input = 'input#quote-risk-motorcycle-make-text'
add_motorcycle_vehicle_details_page_model_input = 'input#quote-risk-motorcycle-model-text'

add_motorcycle_vehicle_details_page_vehicle_type_dropdown = '#quote-risk-motorcycle-type-select'
add_motorcycle_vehicle_details_page_vehicle_type_dropdown_tuple = '#quote-risk-motorcycle-type-select_@index@'

add_motorcycle_vehicle_details_page_cubic_capacity_input = 'input#quote-risk-motorcycle-cubic-capacity-number'
add_motorcycle_vehicle_details_page_registration_number_input = 'input#quote-risk-motorcycle-registration-number-text'
add_motorcycle_vehicle_details_page_chassis_number_input = 'input#quote-risk-motorcycle-serial-number-text'

add_motorcycle_vehicle_details_page_registration_type_options_tuple = (
    'button#quote-risk-motorcycle-registration-type-toggle_Euro\ Plate_-button',
    'button#quote-risk-motorcycle-registration-type-toggle_Normal\ Plate_-button',
    'button#quote-risk-motorcycle-registration-type-toggle_BZ\ Plate_-button',
    'button#quote-risk-motorcycle-registration-type-toggle_Trader\ Plate_-button',
    'button#quote-risk-motorcycle-registration-type-toggle_Transit\ Plate_-button'
)

add_motorcycle_vehicle_details_page_fuel_type_options_tuple = (
    'button#quote-risk-motorcycle-fuel-type-toggle_Diesel\ Oil_-button',
    'button#quote-risk-motorcycle-fuel-type-toggle_Electric_-button',
    'button[id="quote-risk-motorcycle-fuel-type-toggle_Natural Gas for Vehicles_-button"]',
    'button#quote-risk-motorcycle-fuel-type-toggle_Petrol_-button'
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

# Moped page
add_moped_vehicle_details_page_vehicle_type_dropdown = '#quote-risk-moped-type-select'
add_moped_vehicle_details_page_vehicle_type_dropdown_tuple = '#quote-risk-moped-type-select_@index@'

add_moped_vehicle_details_page_make_input = 'input#quote-risk-moped-make-text'
add_moped_vehicle_details_page_model_input = 'input#quote-risk-moped-model-text'
add_moped_vehicle_details_page_cubic_capacity_input = 'input#quote-risk-moped-cubic-capacity-number'
add_moped_vehicle_details_page_registration_number_input = 'input#quote-risk-moped-registration-number-text'
add_moped_vehicle_details_page_chassis_number_input = 'input#quote-risk-moped-serial-number-text'

add_moped_vehicle_details_page_registration_type_options_tuple = (
    'button#quote-risk-moped-registration-type-toggle_Euro\ Plate_-button',
    'button#quote-risk-moped-registration-type-toggle_Normal\ Plate_-button',
    'button#quote-risk-moped-registration-type-toggle_BZ\ Plate_-button',
    'button#quote-risk-moped-registration-type-toggle_Trader\ Plate_-button',
    'button#quote-risk-moped-registration-type-toggle_Transit\ Plate_-button'
)

add_moped_vehicle_details_page_fuel_type_options_tuple = (
    'button#quote-risk-moped-fuel-type-toggle_Diesel\ Oil_-button',
    'button#quote-risk-moped-fuel-type-toggle_Electric_-button',
    'button[id="quote-risk-moped-fuel-type-toggle_Natural Gas for Vehicles_-button"]',
    'button#quote-risk-moped-fuel-type-toggle_Petrol_-button'
)

add_moped_vehicle_details_page_usage_type_options_tuple = (
    'button#quote-risk-moped-usage-type-toggle_Private_-button',
)

add_moped_claim_history_page_next_button = 'a#undefined-4-anchor'

# Family
family_risk_acceptance_answer_no_button = 'button#ques-ans-item-question-answer-answer-boolean-toggle__FALSE_00-button'

# Offer
offer_add_car_drivers_page_add_driver_button = 'button#add-driver-undefined-button'
offer_add_car_driver_license_page_license_id_input = 'input#driver-driving-category-info-license-id-text'
offer_add_car_add_driver_driver_license_page_license_date_input = 'input#driver-driving-category-info-license-date-date_input'
offer_add_car_add_driver_driver_license_page_license_category_options_tuple = (
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
offer_add_car_add_driver_driver_license_page_next_button = '#cdk-accordion-child-13 a#undefined-3-anchor'
offer_add_car_add_driver_address_page_next_button = '#cdk-accordion-child-14 #undefined-4-anchor'
offer_add_car_add_driver_contact_page_next_button = '#cdk-accordion-child-15 #undefined-5-anchor'
offer_add_car_add_driver_page_ok_button = '#driver button#modal__ok'
offer_add_car_drivers_page_next_button = 'a#undefined-6-anchor'
offer_add_car_page_ok_button = '#mat-dialog-2 button#modal__ok'
offer_add_car_page_previous_insurer_next_button = 'a#undefined-7-anchor'
offer_add_car_risk_background_page_certificates_options_tuple = (
    'button#eval-ques-ans-question-answer-answer-boolean-toggle__FALSE_00-button',
    'button#eval-ques-ans-question-answer-answer-boolean-toggle__TRUE_00-button'
)
offer_add_car_risk_background_page_certificates_next_button = 'a#undefined-8-anchor'
offer_add_car_coverage_tariffs_page_options_tuple = '#package-selected-checkbox0@index@'
offer_congratulations_message = '.propositionMessage>a>h3'

offer_add_old_timer_vehicle_details_page_power_input = 'input#quote-risk-automobile-power-number'
offer_add_old_timer_drivers_page_add_driver_button = 'button#add-driver-undefined-button'
offer_add_old_timer_add_driver_driver_license_page_next_button = '#cdk-accordion-child-12 a#undefined-3-anchor'
offer_add_old_timer_add_driver_address_page_next_button = '#cdk-accordion-child-13 #undefined-4-anchor'
offer_add_old_timer_add_driver_contact_page_next_button = '#cdk-accordion-child-14 #undefined-5-anchor'
offer_add_old_timer_add_driver_page_ok_button = '#driver button#modal__ok'
offer_add_old_timer_drivers_page_next_button = 'a#undefined-5-anchor'
offer_add_old_timer_page_previous_insurer_next_button = 'a#undefined-6-anchor'
offer_add_old_timer_risk_background_page_certificates_options_tuple = (
    'button#eval-ques-ans-question-answer-answer-boolean-toggle__FALSE_00-button',
    'button#eval-ques-ans-question-answer-answer-boolean-toggle__TRUE_00-button'
)
offer_add_old_timer_risk_background_page_certificates_next_button = '#undefined-7-anchor'
offer_add_old_timer_page_ok_button = '#mat-dialog-2 button#modal__ok'
offer_add_old_timer_coverage_tariffs_page_options_tuple = '#package-selected-checkbox0@index@'

offer_add_truck_camper_drivers_page_add_driver_button = 'button#add-driver-undefined-button'
offer_add_truck_camper_add_driver_driver_license_page_next_button = '#cdk-accordion-child-13 #undefined-3-anchor'
offer_add_truck_camper_add_driver_address_page_next_button = '#cdk-accordion-child-14 #undefined-4-anchor'
offer_add_truck_camper_add_driver_contact_page_next_button = '#cdk-accordion-child-15 #undefined-5-anchor'
offer_add_truck_camper_add_driver_page_ok_button = '#driver button#modal__ok'
offer_add_truck_camper_drivers_page_next_button = 'a#undefined-6-anchor'
offer_add_truck_camper_previous_insurer_page_next_button = 'a#undefined-7-anchor'
offer_add_truck_camper_risk_background_page_certificates_options_tuple = (
    'button#eval-ques-ans-question-answer-answer-boolean-toggle__FALSE_00-button',
    'button#eval-ques-ans-question-answer-answer-boolean-toggle__TRUE_00-button'
)
offer_add_truck_camper_risk_background_page_certificates_next_button = '#undefined-8-anchor'
offer_add_truck_camper_page_ok_button = '#mat-dialog-2 button#modal__ok'
offer_add_truck_camper_coverage_tariffs_page_options_tuple = '#package-selected-checkbox0@index@'

offer_add_home_home_details_page_bedrooms_input = 'input#mat-input-18'
offer_add_home_home_details_page_bathrooms_input = 'input#mat-input-19'
offer_add_home_home_details_page_alarm_system_options_tuple = (
    'button[id="quote-risk-dwelling-alarm-system-toggle_Certified system_-button"]',
    'button[id="quote-risk-dwelling-alarm-system-toggle_No_-button"]',
    'button[id="quote-risk-dwelling-alarm-system-toggle_Yes_-button"]'
)
offer_add_home_home_details_page_classified_property_options_tuple = (
    'button#quote-risk-dwelling-monument-toggle__FALSE_-button',
    'button#quote-risk-dwelling-monument-toggle__TRUE_-button'
)
offer_add_home_home_details_page_abutment_options_tuple = (
    'button#quote-risk-dwelling-abutment-toggle_Closed_-button',
    'button#quote-risk-dwelling-abutment-toggle_Half\ Open_-button',
    'button#quote-risk-dwelling-abutment-toggle_Open_-button'
)
offer_add_home_home_details_page_building_year_dropdown = '#quote-risk-dwelling-construction-year-select'
offer_add_home_home_details_page_building_year_dropdown_tuple = '#quote-risk-dwelling-construction-year-select_@index@'
offer_add_home_home_details_page_habitation_usage_options_tuple = (
    'button[id="risk-ref-element-extension-element-value-toggle_Habitation only_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Habitation and independant activity_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Independent and other commercial activity_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Garage_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Warehouse/Stockroom_0-button"]'
)
offer_add_home_home_details_page_irregular_habitation_options_tuple = (
    'button#risk-ref-element-extension-element-value-toggle_No_1-button',
    'button#risk-ref-element-extension-element-value-toggle_Yes_1-button'
)
offer_add_home_home_details_page_flammable_construction_options_tuple = (
    'button#risk-ref-element-extension-element-value-toggle_No_2-button',
    'button#risk-ref-element-extension-element-value-toggle_Yes_2-button'
)
offer_add_home_home_details_page_next_button = 'a#undefined-3-anchor'
offer_add_home_equipment_page_add_equipment_button = 'button#add-equipment-undefined-button-modal'
offer_add_home_equipment_page_next_button = 'a#undefined-4-anchor'
offer_add_home_risk_evaluation_page_evaluation_method_options_tuple = (
    'button[id="quote-risk-insured-risk-estimation-method-toggle_GIM_-button"]',
    'button[id="quote-risk-insured-risk-estimation-method-toggle_By questions_-button"]',
    'button[id="quote-risk-insured-risk-estimation-method-toggle_Manual_-button"]'
)
offer_add_home_risk_evaluation_page_evaluate_button = 'button#evaluate-evaluate-risk-button'





offer_add_family_add_home_home_details_page_bedrooms_input = 'input#mat-input-22'
offer_add_family_add_home_home_details_page_bathrooms_input = 'input#mat-input-23'
offer_add_family_add_home_home_details_page_alarm_system_options_tuple = (
    'button[id="quote-risk-dwelling-alarm-system-toggle_Certified system_-button"]',
    'button[id="quote-risk-dwelling-alarm-system-toggle_No_-button"]',
    'button[id="quote-risk-dwelling-alarm-system-toggle_Yes_-button"]'
)
offer_add_family_add_home_home_details_page_classified_property_options_tuple = (
    'button#quote-risk-dwelling-monument-toggle__FALSE_-button',
    'button#quote-risk-dwelling-monument-toggle__TRUE_-button'
)
offer_add_family_add_home_home_details_page_abutment_options_tuple = (
    'button#quote-risk-dwelling-abutment-toggle_Closed_-button',
    'button#quote-risk-dwelling-abutment-toggle_Half\ Open_-button',
    'button#quote-risk-dwelling-abutment-toggle_Open_-button'
)
offer_add_family_add_home_home_details_page_building_year_dropdown = '#quote-risk-dwelling-construction-year-select'
offer_add_family_add_home_home_details_page_building_year_dropdown_tuple = '#quote-risk-dwelling-construction-year-select_@index@'
offer_add_family_add_home_home_details_page_habitation_usage_options_tuple = (
    'button[id="risk-ref-element-extension-element-value-toggle_Habitation only_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Habitation and independant activity_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Independent and other commercial activity_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Garage_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Warehouse/Stockroom_0-button"]'
)
offer_add_family_add_home_home_details_page_irregular_habitation_options_tuple = (
    'button#risk-ref-element-extension-element-value-toggle_No_1-button',
    'button#risk-ref-element-extension-element-value-toggle_Yes_1-button'
)
offer_add_family_add_home_home_details_page_flammable_construction_options_tuple = (
    'button#risk-ref-element-extension-element-value-toggle_No_2-button',
    'button#risk-ref-element-extension-element-value-toggle_Yes_2-button'
)
offer_add_family_add_home_home_details_page_next_button = 'a#undefined-3-anchor'
offer_add_family_add_home_equipment_page_add_equipment_button = 'button#add-equipment-undefined-button-modal'
offer_add_family_add_home_equipment_page_next_button = 'a#undefined-4-anchor'
offer_add_family_add_home_risk_evaluation_page_evaluation_method_options_tuple = (
    'button[id="quote-risk-insured-risk-estimation-method-toggle_GIM_-button"]',
    'button[id="quote-risk-insured-risk-estimation-method-toggle_By questions_-button"]',
    'button[id="quote-risk-insured-risk-estimation-method-toggle_Manual_-button"]'
)
offer_add_family_add_home_risk_evaluation_page_evaluate_button = 'button#evaluate-evaluate-risk-button'

offer_add_motorcycle_drivers_page_add_driver_button = 'button#add-driver-undefined-button'
offer_add_motorcycle_driver_license_page_license_id_input = 'input#driver-driving-category-info-license-id-text'
offer_add_motorcycle_add_driver_driver_license_page_license_date_input = 'input#driver-driving-category-info-license-date-date_input'
offer_add_motorcycle_add_driver_driver_license_page_license_category_options_tuple = (
    'button#driver-driving-category-info-license-category-toggle_A_-button',
    'button#driver-driving-category-info-license-category-toggle_A1_-button',
    'button#driver-driving-category-info-license-category-toggle_A2_-button'
)
offer_add_motorcycle_add_driver_driver_license_page_next_button = '#cdk-accordion-child-10 #undefined-3-anchor'
offer_add_motorcycle_add_driver_address_page_next_button = '#cdk-accordion-child-11 #undefined-4-anchor'
offer_add_motorcycle_add_driver_contact_page_next_button = '#cdk-accordion-child-12 #undefined-5-anchor'
offer_add_motorcycle_add_driver_page_ok_button = '#driver button#modal__ok'
offer_add_motorcycle_coverage_tariffs_page_coverages_options_tuple = '#package-selected-checkbox0@index@'

# Documents insurance
documents_insurance_dropdown = 'div#navbarSupportedContent:nth-of-type(6)'
documents_insurance_dropdown_tuple = (
    '#cdk-overlay-0>div>div>button:nth-of-type(1):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(2):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(3):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(4):not(aria-disabled)'
)
