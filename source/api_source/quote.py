# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 20:37:31 2022

@author: bbalushev
"""


# ======================================== GET the Quotes Collection (GET) =============================================
# ============================= Return the hypermedia of a Quotes Collection (OPTIONS) =================================
# ====================================== POST the Quotes Collection (POST) =============================================
quote_collection = {
    'url': 'Replace1/quotes',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Quotes Document (GET) ==============================================
# ============================== Return the hypermedia of a Quotes Document (OPTIONS) ==================================
# ====================================== DELETE the Quotes Document (DELETE) ===========================================
# ======================================= PATCH the Quotes Document (PATCH) ============================================
quote_document = {
    'url': 'Replace1/quotes/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ==================================== GET the Available Documents Collection (GET) ====================================
# ========================= Return the hypermedia of a Available Documents Collection (OPTIONS) ========================
# ================================== POST the Available Documents Collection (POST) ====================================
available_document_collection_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/available_documents',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Available Documents Document (GET) ======================================
# ========================= Return the hypermedia of a Available Documents Document (OPTIONS) ==========================
# ================================== PATCH the Available Documents Document (PATCH) ====================================
available_document_document_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/available_documents/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Extension Elements Collection (GET) =====================================
# ========================= Return the hypermedia of a Extension Elements Collection (OPTIONS) =========================
# ================================== POST the Extension Elements Collection (POST) =====================================
extension_element_collection_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Extension Elements Document (GET) ======================================
# ========================== Return the hypermedia of a Extension Elements Document (OPTIONS) ==========================
# =================================== PATCH the Extension Elements Document (PATCH) ====================================
extension_element_document_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/extension_elements/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Transfer To Offer Operation (GET) ======================================
# ========================== Return the hypermedia of a Transfer To Offer Operation (OPTIONS) ==========================
# =================================== POST the Transfer To Offer Operation (POST) ======================================
transfer_to_offer_operation_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/operations/transfer_to_offer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Transfer To Offer Operation (GET) =======================================
# ========================= Return the hypermedia of a Transfer To Offer Operation (OPTIONS) ===========================
# ================================= DELETE the Transfer To Offer Operation (DELETE) ====================================
# ================================== PATCH the Transfer To Offer Operation (PATCH) =====================================
transfer_to_offer_operation_of_the_quote_with_transfer_to_offer_id = {
    'url': 'Replace1/quotes/Replace2/operations/transfer_to_offer/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ====================================== GET the Execute Save Controller (GET) =========================================
# =========================== Return the hypermedia of a Execute Save Controller (OPTIONS) =============================
# ==================================== POST the Execute Save Controller (POST) =========================================
execute_transfer_to_offer_save_controller_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/operations/transfer_to_offer/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_transfer_to_offer_save_controller_of_the_quote_with_transfer_to_offer_id = {
    'url': 'Replace1/quotes/Replace2/operations/transfer_to_offer/Replace3/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_transfer_to_offer_save_controller_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/operations/transfer_to_offer/Replace3/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Output Documents Collection (GET) ======================================
# ========================== Return the hypermedia of a Output Documents Collection (OPTIONS) ==========================
# =================================== POST the Output Documents Collection (POST) ======================================
output_document_collection_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/output_documents',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Output Documents Document (GET) =======================================
# =========================== Return the hypermedia of a Output Documents Document (OPTIONS) ===========================
# ==================================== PATCH the Output Documents Document (PATCH) =====================================
output_document_document_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/output_documents/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Owners Collection (GET) ============================================
# ============================== Return the hypermedia of a Owners Collection (OPTIONS) ================================
# ======================================= POST the Owners Collection (POST) ============================================
quote_owner_collection_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/owners',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Owners Document (GET) ===============================================
# ============================= Return the hypermedia of a Owners Document (OPTIONS) ===================================
# ===================================== DELETE the Owners Document (DELETE) ============================================
# ====================================== PATCH the Owners Document (PATCH) =============================================
quote_owner_document_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/owners/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ===================================== GET the Postal Addresses Collection (GET) ======================================
# ========================== Return the hypermedia of a Postal Addresses Collection (OPTIONS) ==========================
# =================================== POST the Postal Addresses Collection (POST) ======================================
postal_address_collection_of_the_quote_owner_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/owners/Replace3/postal_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Postal Addresses Document (GET) ========================================
# ========================== Return the hypermedia of a Postal Addresses Document (OPTIONS) ============================
# ================================== DELETE the Postal Addresses Document (DELETE) =====================================
# =================================== PATCH the Postal Addresses Document (PATCH) ======================================
postal_address_document_of_the_quote_owner_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/owners/Replace3/postal_addresses/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Save Save Controller (GET) ===========================================
# ============================ Return the hypermedia of a Save Save Controller (OPTIONS) ===============================
# ===================================== POST the Save Save Controller (POST) ===========================================
save_postal_address_save_controller_of_the_quote_owner_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/owners/Replace3/postal_addresses/Replace4/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_postal_address_save_controller_of_the_quote_owner_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/owners/Replace3/postal_addresses/Replace4/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Questionnaires Collection (GET) =======================================
# =========================== Return the hypermedia of a Questionnaires Collection (OPTIONS) ===========================
offer_questionnaire_collection_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/questionnaires',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Questionnaires Document (GET) ========================================
# ============================ Return the hypermedia of a Questionnaires Document (OPTIONS) ============================
offer_questionnaire_document_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/questionnaires/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Question Answers Collection (GET) ======================================
# ========================== Return the hypermedia of a Question Answers Collection (OPTIONS) ==========================
offer_question_answer_collection_of_the_offer_questionnaire_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/questionnaires/Replace3/question_answers',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Question Answers Document (GET) =======================================
# =========================== Return the hypermedia of a Question Answers Document (OPTIONS) ===========================
# ==================================== PATCH the Question Answers Document (PATCH) =====================================
offer_question_answer_document_of_the_offer_questionnaire_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/questionnaires/Replace3/question_answers/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Validate Save Controller (GET) =========================================
# =========================== Return the hypermedia of a Validate Save Controller (OPTIONS) ============================
# ==================================== POST the Validate Save Controller (POST) ========================================
validate_offer_questionnaire_save_controller_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/questionnaires/Replace3/validate',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Resume Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Resume Save Controller (OPTIONS) =============================
# ===================================== POST the Resume Save Controller (POST) =========================================
resume_quote_save_controller = {
    'url': 'Replace1/quotes/Replace2/resume',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Risks Collection (GET) =============================================
# ============================== Return the hypermedia of a Risks Collection (OPTIONS) =================================
# ======================================= POST the Risks Collection (POST) =============================================
quote_risk_collection_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Risks Document (GET) ===============================================
# ============================== Return the hypermedia of a Risks Document (OPTIONS) ===================================
# ====================================== DELETE the Risks Document (DELETE) ============================================
# ======================================= PATCH the Risks Document (PATCH) =============================================
quote_risk_document_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Drivers Collection (GET) ============================================
# ============================= Return the hypermedia of a Drivers Collection (OPTIONS) ================================
# ====================================== POST the Drivers Collection (POST) ============================================
quote_driver_collection_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/drivers',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Drivers Document (GET) =============================================
# ============================== Return the hypermedia of a Drivers Document (OPTIONS) =================================
# ====================================== DELETE the Drivers Document (DELETE) ==========================================
# ======================================= PATCH the Drivers Document (PATCH) ===========================================
quote_driver_document_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/drivers/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ===================================== GET the Postal Addresses Collection (GET) ======================================
# ========================== Return the hypermedia of a Postal Addresses Collection (OPTIONS) ==========================
# =================================== POST the Postal Addresses Collection (POST) ======================================
postal_address_collection_of_the_quote_driver_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/drivers/Replace4/postal_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Postal Addresses Document (GET) ========================================
# ========================== Return the hypermedia of a Postal Addresses Document (OPTIONS) ============================
# ================================== DELETE the Postal Addresses Document (DELETE) =====================================
# =================================== PATCH the Postal Addresses Document (PATCH) ======================================
postal_address_document_of_the_quote_driver_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/drivers/Replace4/postal_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Save Save Controller (GET) ==========================================
# ============================= Return the hypermedia of a Save Save Controller (OPTIONS) ==============================
# ====================================== POST the Save Save Controller (POST) ==========================================
save_postal_address_save_controller_of_the_quote_driver_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/drivers/Replace4/postal_addresses/Replace5/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_postal_address_save_controller_of_the_quote_driver_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/drivers/Replace4/postal_addresses/Replace5/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Reinitialize Driver Save Controller (GET) =================================
# ======================= Return the hypermedia of a Reinitialize Driver Save Controller (OPTIONS) =====================
# ================================ POST the Reinitialize Driver Save Controller (POST) =================================
reinitialize_driver_quote_driver_save_controller_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/drivers/Replace4/reinitialize_driver',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Evaluate Value Save Controller (GET) ====================================
# ========================= Return the hypermedia of a Evaluate Value Save Controller (OPTIONS) ========================
# ================================== POST the Evaluate Value Save Controller (POST) ====================================
evaluate_value_quote_risk_save_controller_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/evaluate_value',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Extension Elements Collection (GET) =====================================
# ========================== Return the hypermedia of a Extension Elements Collection (OPTIONS) ========================
# ================================== POST the Extension Elements Collection (POST) =====================================
extension_element_collection_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Extension Elements Document (GET) ======================================
# ========================== Return the hypermedia of a Extension Elements Document (OPTIONS) ==========================
# ==================================== PATCH the Extension Elements Document (PATCH) ===================================
extension_element_document_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/extension_elements/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Owners Collection (GET) ============================================
# ============================== Return the hypermedia of a Owners Collection (OPTIONS) ================================
# ======================================= POST the Owners Collection (POST) ============================================
quote_risk_owner_collection_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/owners',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================== GET the Owners Document (GET) =============================================
# =============================== Return the hypermedia of a Owners Document (OPTIONS) =================================
# ======================================== PATCH the Owners Document (PATCH) ===========================================
quote_risk_owner_document_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/owners/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Postal Addresses Collection (GET) ======================================
# ========================== Return the hypermedia of a Postal Addresses Collection (OPTIONS) ==========================
# =================================== POST the Postal Addresses Collection (POST) ======================================
postal_address_collection_of_the_quote_risk_owner_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/owners/Replace4/postal_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Postal Addresses Document (GET) ========================================
# ========================== Return the hypermedia of a Postal Addresses Document (OPTIONS) ============================
# ================================== DELETE the Postal Addresses Document (DELETE) =====================================
# =================================== PATCH the Postal Addresses Document (PATCH) ======================================
postal_address_document_of_the_quote_risk_owner_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/owners/Replace4/postal_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Save Save Controller (GET) ==========================================
# ============================= Return the hypermedia of a Save Save Controller (OPTIONS) ==============================
# ====================================== POST the Save Save Controller (POST) ==========================================
save_postal_address_save_controller_of_the_quote_risk_owner_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/owners/Replace4/postal_addresses/Replace5/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_postal_address_save_controller_of_the_quote_risk_owner_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/owners/Replace4/postal_addresses/Replace5/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Product Components Collection (GET) =====================================
# ========================= Return the hypermedia of a Product Components Collection (OPTIONS) =========================
quote_product_component_collection_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/product_components',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Product Components Document (GET) ======================================
# ========================== Return the hypermedia of a Product Components Document (OPTIONS) ==========================
# =================================== PATCH the Product Components Document (PATCH) ====================================
quote_product_component_document_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/product_components/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Property Equipments Collection (GET) ====================================
# ========================= Return the hypermedia of a Property Equipments Collection (OPTIONS) ========================
# ================================== POST the Property Equipments Collection (POST) ====================================
quote_risk_equipment_collection_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/property_equipments',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Property Equipments Document (GET) ======================================
# ========================= Return the hypermedia of a Property Equipments Document (OPTIONS) ==========================
# ================================= DELETE the Property Equipments Document (DELETE) ===================================
# ================================== PATCH the Property Equipments Document (PATCH) ====================================
quote_risk_equipment_document_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/property_equipments/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ================================== GET the Property Recorded Claims Collection (GET) =================================
# ======================= Return the hypermedia of a Property Recorded Claims Collection (OPTIONS) =====================
# ================================ POST the Property Recorded Claims Collection (POST) =================================
quote_property_recorded_claim_collection_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/property_recorded_claims',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Property Recorded Claims Document (GET) ==================================
# ======================== Return the hypermedia of a Property Recorded Claims Document (OPTIONS) ======================
# ================================ DELETE the Property Recorded Claims Document (DELETE) ===============================
# ================================= PATCH the Property Recorded Claims Document (PATCH) ================================
quote_property_recorded_claim_document_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/property_recorded_claims/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ====================================== GET the Questionnaires Collection (GET) =======================================
# =========================== Return the hypermedia of a Questionnaires Collection (OPTIONS) ===========================
offer_questionnaire_collection_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/questionnaires',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Questionnaires Document (GET) ========================================
# ============================ Return the hypermedia of a Questionnaires Document (OPTIONS) ============================
offer_questionnaire_document_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/questionnaires/Replace4',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Question Answers Collection (GET) ======================================
# ========================== Return the hypermedia of a Question Answers Collection (OPTIONS) ==========================
offer_question_answer_collection_of_the_offer_questionnaire_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/questionnaires/Replace4/question_answers',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Question Answers Document (GET) =======================================
# =========================== Return the hypermedia of a Question Answers Document (OPTIONS) ===========================
# ==================================== PATCH the Question Answers Document (PATCH) =====================================
offer_question_answer_document_of_the_offer_questionnaire_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/questionnaires/Replace4/question_answers/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Validate Save Controller (GET) ========================================
# =========================== Return the hypermedia of a Validate Save Controller (OPTIONS) ============================
# ==================================== POST the Validate Save Controller (POST) ========================================
validate_offer_questionnaire_save_controller_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/questionnaires/Replace4/validate',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Reinitialize Risk Save Controller (GET) ===================================
# ======================= Return the hypermedia of a Reinitialize Risk Save Controller (OPTIONS) =======================
# ================================ POST the Reinitialize Risk Save Controller (POST) ===================================
reinitialize_risk_quote_risk_save_controller_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/reinitialize_risk',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Tariff Adjustments Collection (GET) =====================================
# ========================= Return the hypermedia of a Tariff Adjustments Collection (OPTIONS) =========================
# ================================== POST the Tariff Adjustments Collection (POST) =====================================
quote_tariff_adjustment_collection_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/tariff_adjustments',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Tariff Adjustments Document (GET) ======================================
# ========================== Return the hypermedia of a Tariff Adjustments Document (OPTIONS) ==========================
# ================================== DELETE the Tariff Adjustments Document (DELETE) ===================================
# =================================== PATCH the Tariff Adjustments Document (PATCH) ====================================
quote_tariff_adjustment_document_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/tariff_adjustments/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ===================================== GET the Postal Addresses Collection (GET) ======================================
# ========================== Return the hypermedia of a Postal Addresses Collection (OPTIONS) ==========================
# =================================== POST the Postal Addresses Collection (POST) ======================================
postal_address_collection_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/postal_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Postal Addresses Document (GET) ========================================
# ========================== Return the hypermedia of a Postal Addresses Document (OPTIONS) ============================
# ================================== DELETE the Postal Addresses Document (DELETE) =====================================
# =================================== PATCH the Postal Addresses Document (PATCH) ======================================
postal_address_document_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/postal_addresses/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Save Save Controller (GET) ==========================================
# ============================= Return the hypermedia of a Save Save Controller (OPTIONS) ==============================
# ====================================== POST the Save Save Controller (POST) ==========================================
save_postal_address_save_controller_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/postal_addresses/Replace4/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_postal_address_save_controller_of_the_quote_risk_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/risks/Replace3/postal_addresses/Replace4/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Save Save Controller (GET) ==========================================
# ============================= Return the hypermedia of a Save Save Controller (OPTIONS) ==============================
# ====================================== POST the Save Save Controller (POST) ==========================================
save_quote_save_controller = {
    'url': 'Replace1/quotes/Replace2/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Tariff Adjustments Collection (GET) =====================================
# ========================= Return the hypermedia of a Tariff Adjustments Collection (OPTIONS) =========================
# ================================== POST the Tariff Adjustments Collection (POST) =====================================
quote_tariff_adjustment_collection_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/tariff_adjustments',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Tariff Adjustments Document (GET) ======================================
# ========================== Return the hypermedia of a Tariff Adjustments Document (OPTIONS) ==========================
# ================================ DELETE the Tariff Adjustments Document (DELETE) =====================================
# ================================== PATCH the Tariff Adjustments Document (PATCH) =====================================
quote_tariff_adjustment_document_of_the_quote = {
    'url': 'Replace1/quotes/Replace2/tariff_adjustments/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ================================== GET the Tariff Calculation Save Controller (GET) ==================================
# ======================= Return the hypermedia of a Tariff Calculation Save Controller (OPTIONS) ======================
# ================================ POST the Tariff Calculation Save Controller (POST) ==================================
tariff_calculation_quote_save_controller = {
    'url': 'Replace1/quotes/Replace2/tariff_calculation',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}
