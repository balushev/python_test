# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:27:27 2022

@author: bbalushev
"""


# ====================================== GET the Contracts Collection (GET) ============================================
# =========================== Return the hypermedia of a Contracts Collection (OPTIONS) ================================
contract_collection = {
    'url': 'Replace1/contracts',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Group Contract Document (GET) ==========================================
# ========================== Return the hypermedia of a Group Contract Document (OPTIONS) ==============================
contract_document = {
    'url': 'Replace1/contracts/Replace2',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =====================================  GET the Activities Collection (GET) ===========================================
# =========================== Return the hypermedia of a Activities Collection (OPTIONS) ===============================
activity_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/activities',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Activities Document (GET) ==============================================
# =========================== Return the hypermedia of a Activities Document (OPTIONS) =================================
activity_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/activities/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Operations Collection (GET) ==========================================
# ============================ Return the hypermedia of a Operations Collection (OPTIONS) ==============================
operation_collection_of_the_activity_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/activities/Replace3/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Process Operation (GET) ================================================
# ======================== Return the hypermedia of a Process Operation (OPTIONS) ======================================
# ================================== POST the Process Operation (POST) =================================================
process_activity_operation_of_the_activity_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/activities/Replace3/operations/process',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================== GET the Process Operation (GET) ===========================================
# =============================== Return the hypermedia of a Process Operation (OPTIONS) ===============================
# ======================================= DELETE the Process Operation (DELETE) ========================================
# ======================================== PATCH the Process Operation (PATCH) =========================================
process_activity_operation_of_the_activity_of_the_contract_with_process_id = {
    'url': 'Replace1/contracts/Replace2/activities/Replace3/operations/process/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== OST the Execute Save Controller (POST) ========================================
execute_process_activity_save_controller_of_the_activity_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/activities/Replace3/operations/process/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_process_activity_save_controller_of_the_activity_of_the_contract_with_process_id = {
    'url': 'Replace1/contracts/Replace2/activities/Replace3/operations/process/Replace4/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Resume In Aia Bridge resource (GET) ====================================
# ========================== Return the hypermedia of a Resume In Aia Bridge resource (OPTIONS) ========================
# =================================== POST the Resume In Aia Bridge resource (POST) ====================================
resume_in_aia_activity_bridge_resource_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/activities/Replace3/resume_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Activity Definitions Collection (GET) ====================================
# ======================== Return the hypermedia of a Activity Definitions Collection (OPTIONS) ========================
activity_definition_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/activity_definitions',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Activity Definitions Document (GET) =====================================
# ======================== Return the hypermedia of a Activity Definitions Document (OPTIONS) =========================
activity_definition_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/activity_definitions/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================ GET the Launch Activity In Aia Bridge resource (GET) ================================
# ===================== Return the hypermedia of a Launch Activity In Aia Bridge resource (OPTIONS) ====================
# ============================== POST the Launch Activity In Aia Bridge resource (POST) ================================
launch_activity_in_aia_activity_definition_bridge_resource_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/activity_definitions/Replace3/launch_activity_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Available Documents Collection (GET) ====================================
# ========================= Return the hypermedia of a Available Documents Collection (OPTIONS) ========================
# ================================== POST the Available Documents Collection (POST) ====================================
available_document_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/available_documents',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Available Documents Document (GET) =====================================
# ========================== Return the hypermedia of a Available Documents Document (OPTIONS) =========================
# =================================== PATCH the Available Documents Document (PATCH) ===================================
available_document_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/available_documents/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Billings Collection (GET) ==========================================
# ============================== Return the hypermedia of a Billings Collection (OPTIONS) ==============================
billing_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/billings',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Billings Document (GET) ============================================
# ============================== Return the hypermedia of a Billings Document (OPTIONS) ================================
# ======================================= PATCH the Billings Document (PATCH) ==========================================
billing_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/billings/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Extension Elements Collection (GET) ====================================
# ========================== Return the hypermedia of a Extension Elements Collection (OPTIONS) ========================
# =================================== POST the Extension Elements Collection (POST) ====================================
extension_element_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Extension Elements Document (GET) ======================================
# =========================== Return the hypermedia of a Extension Elements Document (OPTIONS) =========================
# ==================================== PATCH the Extension Elements Document (PATCH) ===================================
extension_element_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/extension_elements/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Information Receipts Collection (GET) ===================================
# ========================= Return the hypermedia of a Information Receipts Collection (OPTIONS) =======================
# =================================== POST the Information Receipts Collection (POST) ==================================
information_receipt_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Information Receipts Document (GET) ====================================
# ========================== Return the hypermedia of a Information Receipts Document (OPTIONS) ========================
# =================================== PATCH the Information Receipts Document (PATCH) ==================================
information_receipt_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/information_receipts/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ====================================== POST the Transfer Save Controller (POST) ======================================
transfer_information_receipt_save_controller_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/information_receipts/Replace3/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Multiple Transfer Save Controller (GET) ==================================
# ======================== Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) ======================
# ================================= POST the Multiple Transfer Save Controller (POST) ==================================
multiple_transfer_information_receipt_save_controller_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Information Requests Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Requests Collection (OPTIONS) ========================
information_request_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/information_requests',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Information Requests Document (GET) =====================================
# ========================= Return the hypermedia of a Information Requests Document (OPTIONS) =========================
information_request_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/information_requests/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Launch View Aia Bridge resource (GET) ====================================
# ======================== Return the hypermedia of a Launch View Aia Bridge resource (OPTIONS) ========================
# =================================  POST the Launch View Aia Bridge resource (POST) ===================================
launch_view_aia_contract_bridge_resource = {
    'url': 'Replace1/contracts/Replace2/launch_view_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Manual Tasks Collection (GET) ========================================
# ============================ Return the hypermedia of a Manual Tasks Collection (OPTIONS) ============================
# ====================================== POST the Manual Tasks Collection (POST) =======================================
manual_task_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/manual_tasks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Manual Tasks Document (GET) =========================================
# ============================= Return the hypermedia of a Manual Tasks Document (OPTIONS) =============================
# ====================================== PATCH the Manual Tasks Document (PATCH) =======================================
manual_task_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/manual_tasks/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_manual_task_save_controller_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/manual_tasks/Replace3/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Output Documents Collection (GET) ======================================
# ========================== Return the hypermedia of a Output Documents Collection (OPTIONS) ==========================
# ==================================== POST the Output Documents Collection (POST) =====================================
output_document_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/output_documents',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Output Documents Document (GET) =======================================
# =========================== Return the hypermedia of a Output Documents Document (OPTIONS) ===========================
# =================================== PATCH the Output Documents Document (PATCH) ======================================
output_document_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/output_documents/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Party Roles Collection (GET) =========================================
# ============================ Return the hypermedia of a Party Roles Collection (OPTIONS) =============================
party_role_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/party_roles',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Party Roles Document (GET) =========================================
# =============================== Return the hypermedia of a Party Roles Document (OPTIONS) ============================
party_role_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/party_roles/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Premiums Collection (GET) ==========================================
# ============================== Return the hypermedia of a Premiums Collection (OPTIONS) ==============================
premium_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/premiums',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Premiums Document (GET) ===========================================
# =============================== Return the hypermedia of a Premiums Document (OPTIONS) ===============================
premium_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/premiums/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Savings Flows Collection (GET) ========================================
# =========================== Return the hypermedia of a Savings Flows Collection (OPTIONS) ============================
savings_flow_collection_of_the_premium_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/premiums/Replace3/savings_flows',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Savings Flows Document (GET) =========================================
# ============================ Return the hypermedia of a Savings Flows Document (OPTIONS) =============================
savings_flow_document_of_the_premium_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/premiums/Replace3/savings_flows/Replace4',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================== GET the Risk Groups Collection (GET) ========================================
# ============================= Return the hypermedia of a Risk Groups Collection (OPTIONS) ============================
risk_group_collection_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Risk Groups Document (GET) =========================================
# ============================== Return the hypermedia of a Risk Groups Document (OPTIONS) =============================
risk_group_document_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Product Components Collection (GET) =====================================
# ========================= Return the hypermedia of a Product Components Collection (OPTIONS) =========================
product_component_collection_of_the_risk_group_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups/Replace3/product_components',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Product Components Document (GET) ======================================
# ========================== Return the hypermedia of a Product Components Document (OPTIONS) ==========================
product_component_document_of_the_risk_group_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups/Replace3/product_components/Replace4',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Clauses Collection (GET) ===========================================
# ============================== Return the hypermedia of a Clauses Collection (OPTIONS) ===============================
clause_collection_of_the_product_component_of_the_risk_group_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups/Replace3/product_components/Replace4/clauses',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Clauses Document (GET) ============================================
# =============================== Return the hypermedia of a Clauses Document (OPTIONS) ================================
# ======================================== PATCH the Clauses Document (PATCH) ==========================================
clause_document_of_the_product_component_of_the_risk_group_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups/Replace3/product_components/Replace4/clauses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================  GET the Financial Options Collection (GET) =====================================
# ========================= Return the hypermedia of a Financial Options Collection (OPTIONS) ==========================
financial_option_collection_of_the_product_component_of_the_risk_group_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups/Replace3/product_components/Replace4/financial_options',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Financial Options Document (GET) =======================================
# ========================== Return the hypermedia of a Financial Options Document (OPTIONS) ===========================
financial_option_document_of_the_product_component_of_the_risk_group_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups/Replace3/product_components/Replace4/financial_options/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Funds Collection (GET) ============================================
# =============================== Return the hypermedia of a Funds Collection (OPTIONS) ================================
fund_collection_of_the_product_component_of_the_risk_group_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups/Replace3/product_components/Replace4/funds',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Funds Document (GET) ==============================================
# =============================== Return the hypermedia of a Funds Document (OPTIONS) ==================================
fund_document_of_the_product_component_of_the_risk_group_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups/Replace3/product_components/Replace4/funds/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Savings Flows Collection (GET) ========================================
# =========================== Return the hypermedia of a Savings Flows Collection (OPTIONS) ============================
savings_flow_collection_of_the_fund_of_the_product_component_of_the_risk_group_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups/Replace3/product_components/Replace4/funds/Replace5/savings_flows',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Savings Flows Document (GET) =========================================
# ============================ Return the hypermedia of a Savings Flows Document (OPTIONS) =============================
savings_flow_document_of_the_fund_of_the_product_component_of_the_risk_group_of_the_contract = {
    'url': 'Replace1/contracts/Replace2/risk_groups/Replace3/product_components/Replace4/funds/Replace5/savings_flows/Replace6',
    'request_methods_list': ['GET', 'OPTIONS']
}
