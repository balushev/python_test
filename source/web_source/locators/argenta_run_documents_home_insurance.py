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
    'documents': ('home insurance', 'car insurance', 'family insurance', 'motorcycle insurance'),
    'add_home_home_details_page_building_year': ('before 1995', '1995 - 1999', '2000 - 2004', '2005 - 2009',
                                                 '2010 - 2014', '2015 - 2019', '2020 - 2020', '2021 - 2021',
                                                 '2022 - 2022'),
    'add_family_add_home_home_details_page_building_year': ('before 1995', '1995 - 1999', '2000 - 2004', '2005 - 2009',
                                                            '2010 - 2014', '2015 - 2019', '2020 - 2020', '2021 - 2021',
                                                            '2022 - 2022')
}

# Dictionary which contains all options area values
options_area_lists = {
    'home_branch_owner': ('nc', 'fc'),
    'add_home_home_details_page_classified_property': ('no', 'yes'),
    'add_family_add_home_home_details_page_classified_property': ('no', 'yes'),
    'add_home_home_details_page_irregular_habitation': ('no', 'yes'),
    'add_family_add_home_home_details_page_irregular_habitation': ('no', 'yes'),
    'add_home_home_details_page_flammable_construction': ('no', 'yes'),
    'add_family_add_home_home_details_page_flammable_construction': ('no', 'yes'),
    'billing_page_frequency': ('monthly', 'quarterly', 'semi annual', 'annual'),
    'add_home_home_details_page_type': ('apartment', 'block', 'bungalow or cottage', 'commercial premises', 'house',
                                        'mobile home'),
    'add_family_add_home_home_details_page_type': ('apartment', 'block', 'bungalow or cottage', 'commercial premises',
                                                   'house', 'mobile home'),
    'add_home_home_details_page_usage': ('owner occupant', 'owner non occupant', 'owner with block policy',
                                         'tenant of a full building', 'tenant of a part of building'),
    'add_family_add_home_home_details_page_usage': ('owner occupant', 'owner non occupant', 'owner with block policy',
                                                    'tenant of a full building', 'tenant of a part of building'),
    'add_home_home_details_page_alarm_system': ('certified system', 'no', 'yes'),
    'add_family_add_home_home_details_page_alarm_system': ('certified system', 'no', 'yes'),
    'add_home_home_details_page_abutment': ('closed', 'half open', 'open'),
    'add_family_add_home_home_details_page_abutment': ('closed', 'half open', 'open'),
    'add_home_home_details_page_habitation_usage': ('habitation only', 'habitation and independent activity',
                                                    'independent and other commercial activity', 'garage',
                                                    'warehouse or stockroom'),
    'add_family_add_home_home_details_page_habitation_usage': ('habitation only', 'habitation and independent activity',
                                                               'independent and other commercial activity', 'garage',
                                                               'warehouse or stockroom'),
    'add_home_risk_evaluation_page_evaluation_method': ('gim', 'by questions', 'manual'),
    'add_family_add_home_risk_evaluation_page_evaluation_method': ('gim', 'by questions', 'manual'),
    'add_family_page_family_situation': ('family', '60 plus', 'single'),
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
documents_dropdown = 'div#navbarSupportedContent:nth-of-type(6)'
documents_dropdown_tuple = (
    '#cdk-overlay-0>div>div>button:nth-of-type(1):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(2):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(3):not(aria-disabled)',
    '#cdk-overlay-0>div>div>button:nth-of-type(4):not(aria-disabled)'
)

# Search Owner page
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

# Home
add_home_button = 'button#add-home-risk-undefined-button-modal'
add_home_address_page_next_button = 'a#undefined-2-anchor'

add_home_home_details_page_type_options_tuple = (
    'button[id="quote-risk-dwelling-type-toggle_Appartment_-button"]',
    'button[id="quote-risk-dwelling-type-toggle_Block_-button"]',
    'button[id="quote-risk-dwelling-type-toggle_Bungalow / Cottage_-button"]',
    'button[id="quote-risk-dwelling-type-toggle_Commercial Premises_-button"]',
    'button[id="quote-risk-dwelling-type-toggle_House_-button"]',
    'button[id="quote-risk-dwelling-type-toggle_Mobile Home_-button"]'
)

add_home_home_details_page_usage_options_tuple = (
    'button[id="quote-risk-dwelling-usage-type-toggle_Owner Occupant_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Owner Non Occupant_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Owner with Block Policy_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Tenant of a Full Building_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Tenant of a part of Building_-button"]'
)

add_home_home_details_page_bedrooms_input = 'input#mat-input-18'
add_home_home_details_page_bathrooms_input = 'input#mat-input-19'

add_home_home_details_page_alarm_system_options_tuple = (
    'button[id="quote-risk-dwelling-alarm-system-toggle_Certified system_-button"]',
    'button[id="quote-risk-dwelling-alarm-system-toggle_No_-button"]',
    'button[id="quote-risk-dwelling-alarm-system-toggle_Yes_-button"]'
)

add_home_home_details_page_classified_property_options_tuple = (
    'button[id="quote-risk-dwelling-monument-toggle__FALSE_-button"]',
    'button[id="quote-risk-dwelling-monument-toggle__TRUE_-button"]'
)

add_home_home_details_page_abutment_options_tuple = (
    'button[id="quote-risk-dwelling-abutment-toggle_Closed_-button"]',
    'button[id="quote-risk-dwelling-abutment-toggle_Half Open_-button"]',
    'button[id="quote-risk-dwelling-abutment-toggle_Open_-button"]'
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
    'button[id="risk-ref-element-extension-element-value-toggle_No_1-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Yes_1-button"]'
)

add_home_home_details_page_flammable_construction_options_tuple = (
    'button[id="risk-ref-element-extension-element-value-toggle_No_2-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Yes_2-button"]'
)

add_home_risk_evaluation_page_evaluation_method_options_tuple = (
    'button[id="quote-risk-insured-risk-estimation-method-toggle_GIM_-button"]',
    'button[id="quote-risk-insured-risk-estimation-method-toggle_By questions_-button"]',
    'button[id="quote-risk-insured-risk-estimation-method-toggle_Manual_-button"]'
)

add_home_home_details_page_next_button = 'a#undefined-3-anchor'
add_home_equipment_page_add_equipment_button = 'button#add-equipment-undefined-button-modal'
add_home_equipment_page_next_button = 'a#undefined-4-anchor'
add_home_risk_evaluation_page_evaluate_button = 'button#evaluate-evaluate-risk-button'


home_postal_code_input = 'input#quote-risk-preferred-address-postal-address-postal-code-autocomplete'
home_city_input = 'input#quote-risk-preferred-address-postal-address-city-name-autocomplete'
home_street_name_input = 'input#quote-risk-preferred-address-postal-address-street-name-autocomplete'
home_street_number_input = 'input#quote-risk-preferred-address-postal-address-street-number-text'
home_box_number_input = 'input#quote-risk-preferred-address-postal-address-box-number-text'

home_branch_owner_options_tuple = (
    'button[id="reference-element-extension-element-value-toggle_NC_0-button"]',
    'button[id="reference-element-extension-element-value-toggle_FC_0-button"]'
)

# Add Family
add_family_button = 'button#add-family-risk-undefined-button-modal'

add_family_page_family_situation_options_tuple = (
    'button[id="quote-risk-family-family-situation-toggle_Family_-button"]',
    'button[id="quote-risk-family-family-situation-toggle_60+_-button"]',
    'button[id="quote-risk-family-family-situation-toggle_Single_-button"]'
)

add_family_page_ok_button = 'button#modal__ok'

add_family_page_add_home_button = 'button#add-home-risk-undefined-button-modal'
add_family_add_home_address_page_next_button = 'a#undefined-2-anchor'

add_family_add_home_home_details_page_type_options_tuple = (
    'button[id="quote-risk-dwelling-type-toggle_Appartment_-button"]',
    'button[id="quote-risk-dwelling-type-toggle_Block_-button"]',
    'button[id="quote-risk-dwelling-type-toggle_Bungalow / Cottage_-button"]',
    'button[id="quote-risk-dwelling-type-toggle_Commercial Premises_-button"]',
    'button[id="quote-risk-dwelling-type-toggle_House_-button"]',
    'button[id="quote-risk-dwelling-type-toggle_Mobile Home_-button"]'
)

add_family_add_home_home_details_page_usage_options_tuple = (
    'button[id="quote-risk-dwelling-usage-type-toggle_Owner Occupant_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Owner Non Occupant_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Owner with Block Policy_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Tenant of a Full Building_-button"]',
    'button[id="quote-risk-dwelling-usage-type-toggle_Tenant of a part of Building_-button"]'
)

add_family_add_home_home_details_page_bedrooms_input = 'input#mat-input-22'
add_family_add_home_home_details_page_bathrooms_input = 'input#mat-input-23'

add_family_add_home_home_details_page_alarm_system_options_tuple = (
    'button[id="quote-risk-dwelling-alarm-system-toggle_Certified system_-button"]',
    'button[id="quote-risk-dwelling-alarm-system-toggle_No_-button"]',
    'button[id="quote-risk-dwelling-alarm-system-toggle_Yes_-button"]'
)

add_family_add_home_home_details_page_classified_property_options_tuple = (
    'button[id="quote-risk-dwelling-monument-toggle__FALSE_-button"]',
    'button[id="quote-risk-dwelling-monument-toggle__TRUE_-button"]'
)

add_family_add_home_home_details_page_abutment_options_tuple = (
    'button[id="quote-risk-dwelling-abutment-toggle_Closed_-button"]',
    'button[id="quote-risk-dwelling-abutment-toggle_Half Open_-button"]',
    'button[id="quote-risk-dwelling-abutment-toggle_Open_-button"]'
)

add_family_add_home_home_details_page_building_year_dropdown = '#quote-risk-dwelling-construction-year-select'
add_family_add_home_home_details_page_building_year_dropdown_tuple = '#quote-risk-dwelling-construction-year-select_@index@'

add_family_add_home_home_details_page_habitation_usage_options_tuple = (
    'button[id="risk-ref-element-extension-element-value-toggle_Habitation only_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Habitation and independant activity_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Independent and other commercial activity_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Garage_0-button"]',
    'button[id="risk-ref-element-extension-element-value-toggle_Warehouse/Stockroom_0-button"]'
)

add_family_add_home_home_details_page_irregular_habitation_options_tuple = (
    'button#risk-ref-element-extension-element-value-toggle_No_1-button',
    'button#risk-ref-element-extension-element-value-toggle_Yes_1-button'
)

add_family_add_home_home_details_page_flammable_construction_options_tuple = (
    'button#risk-ref-element-extension-element-value-toggle_No_2-button',
    'button#risk-ref-element-extension-element-value-toggle_Yes_2-button'
)

add_family_add_home_home_details_page_next_button = 'a#undefined-3-anchor'
add_family_add_home_equipment_page_next_button = 'a#undefined-4-anchor'

add_family_add_home_risk_evaluation_page_evaluation_method_options_tuple = (
    'button[id="quote-risk-insured-risk-estimation-method-toggle_GIM_-button"]',
    'button[id="quote-risk-insured-risk-estimation-method-toggle_By questions_-button"]',
    'button[id="quote-risk-insured-risk-estimation-method-toggle_Manual_-button"]'
)
