# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:12:09 2022

@author: bbalushev
"""


# =========================================== GET the Risks Collection (GET) ===========================================
# =============================== Return the hypermedia of a Risks Collection (OPTIONS) ================================
risk_collection = {
    'url': 'Replace1/risks',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Automobile Document (GET) ==========================================
# ============================= Return the hypermedia of a Automobile Document (OPTIONS) ===============================
risk_document = {
    'url': 'Replace1/risks/Replace2',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Clauses Collection (GET) ===========================================
# ============================== Return the hypermedia of a Clauses Collection (OPTIONS) ===============================
clause_collection_of_the_risk = {
    'url': 'Replace1/risks/Replace2/clauses',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =========================================== GET the Clauses Document (GET) ===========================================
# =============================== Return the hypermedia of a Clauses Document (OPTIONS) ================================
# ======================================== PATCH the Clauses Document (PATCH) ==========================================
clause_document_of_the_risk = {
    'url': 'Replace1/risks/Replace2/clauses/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Drivers Collection (GET) ===========================================
# ============================== Return the hypermedia of a Drivers Collection (OPTIONS) ===============================
contract_driver_collection_of_the_risk = {
    'url': 'Replace1/risks/Replace2/drivers',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =========================================== GET the Drivers Document (GET) ===========================================
# =============================== Return the hypermedia of a Drivers Document (OPTIONS) ================================
contract_driver_document_of_the_risk = {
    'url': 'Replace1/risks/Replace2/drivers/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ============================== GET the Exclude From Claim Dclrtn Save Controller (GET) ===============================
# ================== Return the hypermedia of a Exclude From Claim Dclrtn Save Controller (OPTIONS) ====================
# ============================= POST the Exclude From Claim Dclrtn Save Controller (POST) ==============================
exclude_from_claim_dclrtn_risk_save_controller = {
    'url': 'Replace1/risks/Replace2/exclude_from_claim_dclrtn',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Extension Elements Collection (GET) ======================================
# ======================== Return the hypermedia of a Extension Elements Collection (OPTIONS) ==========================
# =================================== POST the Extension Elements Collection (POST) ====================================
extension_element_collection_of_the_risk = {
    'url': 'Replace1/risks/Replace2/extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Extension Elements Document (GET) ======================================
# ========================= Return the hypermedia of a Extension Elements Document (OPTIONS) ===========================
# =================================== PATCH the Extension Elements Document (PATCH) ====================================
extension_element_document_of_the_risk = {
    'url': 'Replace1/risks/Replace2/extension_elements/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ============================= GET the Include In Claim Dclrtn Save Controller (GET) ==============================
# ================= Return the hypermedia of a Include In Claim Dclrtn Save Controller (OPTIONS) ===================
# ============================ POST the Include In Claim Dclrtn Save Controller (POST) =============================
include_in_claim_dclrtn_risk_save_controller = {
    'url': 'Replace1/risks/Replace2/include_in_claim_dclrtn',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Product Components Collection (GET) =====================================
# ======================== Return the hypermedia of a Product Components Collection (OPTIONS) ==========================
product_component_collection_of_the_risk = {
    'url': 'Replace1/risks/Replace2/product_components',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Product Components Document (GET) ======================================
# ========================= Return the hypermedia of a Product Components Document (OPTIONS) ===========================
product_component_document_of_the_risk = {
    'url': 'Replace1/risks/Replace2/product_components/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Clauses Collection (GET) ===========================================
# ============================== Return the hypermedia of a Clauses Collection (OPTIONS) ===============================
clause_collection_of_the_product_component_of_the_risk = {
    'url': 'Replace1/risks/Replace2/product_components/Replace3/clauses',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Clauses Document (GET) ============================================
# =============================== Return the hypermedia of a Clauses Document (OPTIONS) ================================
# ======================================== PATCH the Clauses Document (PATCH) ==========================================
clause_document_of_the_product_component_of_the_risk = {
    'url': 'Replace1/risks/Replace2/product_components/Replace3/clauses/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Financial Options Collection (GET) ======================================
# ========================= Return the hypermedia of a Financial Options Collection (OPTIONS) ==========================
financial_option_collection_of_the_product_component_of_the_risk = {
    'url': 'Replace1/risks/Replace2/product_components/Replace3/financial_options',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Financial Options Document (GET) =======================================
# ========================== Return the hypermedia of a Financial Options Document (OPTIONS) ===========================
financial_option_document_of_the_product_component_of_the_risk = {
    'url': 'Replace1/risks/Replace2/product_components/Replace3/financial_options/Replace4',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ============================ Return the hypermedia of a Financial Options Document (GET) =============================
# =============================== Return the hypermedia of a Funds Collection (OPTIONS) ================================
fund_collection_of_the_product_component_of_the_risk = {
    'url': 'Replace1/risks/Replace2/product_components/Replace3/funds',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =========================================== GET the Funds Document (GET) =============================================
# ================================ Return the hypermedia of a Funds Document (OPTIONS) =================================
fund_document_of_the_product_component_of_the_risk = {
    'url': 'Replace1/risks/Replace2/product_components/Replace3/funds/Replace4',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Savings Flows Collection (GET) ========================================
# =========================== Return the hypermedia of a Savings Flows Collection (OPTIONS) ============================
savings_flow_collection_of_the_fund_of_the_product_component_of_the_risk = {
    'url': 'Replace1/risks/Replace2/product_components/Replace3/funds/Replace4/savings_flows',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Savings Flows Document (GET) =========================================
# ============================ Return the hypermedia of a Savings Flows Document (OPTIONS) =============================
savings_flow_document_of_the_fund_of_the_product_component_of_the_risk = {
    'url': 'Replace1/risks/Replace2/product_components/Replace3/funds/Replace4/savings_flows/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Property Equipments Collection (GET) =====================================
# ======================== Return the hypermedia of a Property Equipments Collection (OPTIONS) =========================
risk_equipment_collection_of_the_risk = {
    'url': 'Replace1/risks/Replace2/property_equipments',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Property Equipments Document (GET) ======================================
# ========================= Return the hypermedia of a Property Equipments Document (OPTIONS) ==========================
risk_equipment_document_of_the_risk = {
    'url': 'Replace1/risks/Replace2/property_equipments/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================= GET the Property Recorded Claims Collection (GET) ==================================
# ===================== Return the hypermedia of a Property Recorded Claims Collection (OPTIONS) =======================
property_recorded_claim_collection_of_the_risk = {
    'url': 'Replace1/risks/Replace2/property_recorded_claims',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================== GET the Property Recorded Claims Document (GET) ===================================
# ====================== Return the hypermedia of a Property Recorded Claims Document (OPTIONS) ========================
property_recorded_claim_document_of_the_risk = {
    'url': 'Replace1/risks/Replace2/property_recorded_claims/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Property Zones Collection (GET) =======================================
# =========================== Return the hypermedia of a Property Zones Collection (OPTIONS) ===========================
property_zone_collection_of_the_risk = {
    'url': 'Replace1/risks/Replace2/property_zones',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Property Zones Document (GET) ========================================
# =========================== Return the hypermedia of a Property Zones Document (OPTIONS) =============================
property_zone_document_of_the_risk = {
    'url': 'Replace1/risks/Replace2/property_zones/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Questionnaires Collection (GET) =======================================
# ========================== Return the hypermedia of a Questionnaires Collection (OPTIONS) ============================
questionnaire_collection_of_the_risk = {
    'url': 'Replace1/risks/Replace2/questionnaires',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Questionnaires Document (GET) ========================================
# ============================ Return the hypermedia of a Questionnaires Document (OPTIONS) ============================
questionnaire_document_of_the_risk = {
    'url': 'Replace1/risks/Replace2/questionnaires/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Question Answers Collection (GET) ======================================
# ========================= Return the hypermedia of a Question Answers Collection (OPTIONS) ===========================
question_answer_collection_of_the_questionnaire_of_the_risk = {
    'url': 'Replace1/risks/Replace2/questionnaires/Replace3/question_answers',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Question Answers Document (GET) =======================================
# =========================== Return the hypermedia of a Question Answers Document (OPTIONS) ===========================
# ===================================== PATCH the Question Answers Document (PATCH) ====================================
question_answer_document_of_the_questionnaire_of_the_risk = {
    'url': 'Replace1/risks/Replace2/questionnaires/Replace3/question_answers/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}
