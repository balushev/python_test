# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 17:01:14 2022

@author: bbalushev
"""


# ========================================== GET the Claims Collection (GET) ===========================================
# =============================== Return the hypermedia of a Claims Collection (OPTIONS) ===============================
# ========================================  POST the Claims Collection (POST) ==========================================
claim_collection = {
    'url': 'Replace1/claims',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Claim Life Document (GET) ==========================================
# ============================== Return the hypermedia of a Claim Life Document (OPTIONS) ==============================
# ======================================  PATCH the Claim Life Document (PATCH) ========================================
claim_document = {
    'url': 'Replace1/claims/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Activities Collection (GET) =========================================
# ============================= Return the hypermedia of a Activities Collection (OPTIONS) =============================
activity_collection_of_the_claim = {
    'url': 'Replace1/claims/Replace2/activities',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Activities Document (GET) ==========================================
# ============================== Return the hypermedia of a Activities Document (OPTIONS) ==============================
activity_document_of_the_claim = {
    'url': 'Replace1/claims/Replace2/activities/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}


# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_activity_of_the_claim = {
    'url': 'Replace1/claims/Replace2/activities/Replace3/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Process Operation (GET) ===========================================
# =============================== Return the hypermedia of a Process Operation (OPTIONS) ===============================
# ========================================  POST the Process Operation (POST) ==========================================
process_activity_operation_of_the_activity_of_the_claim = {
    'url': 'Replace1/claims/Replace2/activities/Replace3/operations/process',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================== GET the Process Operation (GET) ===========================================
# =============================== Return the hypermedia of a Process Operation (OPTIONS) ===============================
# =====================================  DELETE the Process Operation (DELETE) =========================================
# =======================================  PATCH the Process Operation (PATCH) =========================================
process_activity_operation_of_the_activity_of_the_claim_with_process_id = {
    'url': 'Replace1/claims/Replace2/activities/Replace3/operations/process/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# =====================================  POST the Execute Save Controller (POST) =======================================
execute_process_activity_save_controller_of_the_activity_of_the_claim = {
    'url': 'Replace1/claims/Replace2/activities/Replace3/operations/process/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_process_activity_save_controller_of_the_activity_of_the_claim_with_process_id = {
    'url': 'Replace1/claims/Replace2/activities/Replace3/operations/process/Replace4/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Resume In Aia Bridge resource (GET) =====================================
# ========================= Return the hypermedia of a Resume In Aia Bridge resource (OPTIONS) =========================
# ==================================  POST the Resume In Aia Bridge resource (POST) ====================================
resume_in_aia_activity_bridge_resource_of_the_claim = {
    'url': 'Replace1/claims/Replace2/activities/Replace3/resume_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Activity Definitions Collection (GET) ====================================
# ======================== Return the hypermedia of a Activity Definitions Collection (OPTIONS) ========================
activity_definition_collection_of_the_claim = {
    'url': 'Replace1/claims/Replace2/activity_definitions',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Activity Definitions Document (GET) =====================================
# ========================= Return the hypermedia of a Activity Definitions Document (OPTIONS) =========================
activity_definition_document_of_the_claim = {
    'url': 'Replace1/claims/Replace2/activity_definitions/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================ GET the Launch Activity In Aia Bridge resource (GET) ================================
# ===================== Return the hypermedia of a Launch Activity In Aia Bridge resource (OPTIONS) ====================
# ==============================  POST the Launch Activity In Aia Bridge resource (POST) ===============================
launch_activity_in_aia_activity_definition_bridge_resource_of_the_claim = {
    'url': 'Replace1/claims/Replace2/activity_definitions/Replace3/launch_activity_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Claim Life Folders Collection (GET) =====================================
# ========================= Return the hypermedia of a Claim Life Folders Collection (OPTIONS) =========================
claim_life_folder_collection_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Claim Life Folders Document (GET) ======================================
# ========================== Return the hypermedia of a Claim Life Folders Document (OPTIONS) ==========================
claim_life_folder_document_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ============================== GET the Cancel Extension Elements Save Controller (GET) ===============================
# =================== Return the hypermedia of a Cancel Extension Elements Save Controller (OPTIONS) ===================
# ============================  POST the Cancel Extension Elements Save Controller (POST) ==============================
cancel_extension_elements_claim_life_folder_save_controller_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/cancel_extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Extension Elements Collection (GET) =====================================
# ========================= Return the hypermedia of a Extension Elements Collection (OPTIONS) =========================
# ==================================  POST the Extension Elements Collection (POST) ====================================
extension_element_collection_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Extension Elements Document (GET) ======================================
# ========================== Return the hypermedia of a Extension Elements Document (OPTIONS) ==========================
# ==================================  PATCH the Extension Elements Document (PATCH) ====================================
extension_element_document_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/extension_elements/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# =================================== GET the Information Receipts Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Receipts Collection (OPTIONS) ========================
# ================================= POST the Information Receipts Collection (POST) ====================================
information_receipt_collection_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Information Receipts Document (GET) =====================================
# ========================= Return the hypermedia of a Information Receipts Document (OPTIONS) =========================
# ================================= PATCH the Information Receipts Document (PATCH) ====================================
information_receipt_document_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/information_receipts/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Transfer Save Controller (GET) ========================================
# =========================== Return the hypermedia of a Transfer Save Controller (OPTIONS) ============================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_information_receipt_save_controller_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/information_receipts/Replace4/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Multiple Transfer Save Controller (GET) ===================================
# ======================= Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) =======================
# ================================  POST the Multiple Transfer Save Controller (POST) ==================================
multiple_transfer_information_receipt_save_controller_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Information Requests Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Requests Collection (OPTIONS) ========================
information_request_collection_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/information_requests',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Information Requests Document (GET) =====================================
# ========================= Return the hypermedia of a Information Requests Document (OPTIONS) =========================
information_request_document_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/information_requests/Replace4',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Manual Tasks Collection (GET) ========================================
# ============================ Return the hypermedia of a Manual Tasks Collection (OPTIONS) ============================
# ===================================== POST the Manual Tasks Collection (POST) ========================================
manual_task_collection_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/manual_tasks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Manual Tasks Document (GET) =========================================
# ============================= Return the hypermedia of a Manual Tasks Document (OPTIONS) =============================
# ===================================== PATCH the Manual Tasks Document (PATCH) ========================================
manual_task_document_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/manual_tasks/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_manual_task_save_controller_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/manual_tasks/Replace4/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =============================== GET the Save Extension Elements Save Controller (GET) ================================
# ==================== Return the hypermedia of a Save Extension Elements Save Controller (OPTIONS) ====================
# ============================== POST the Save Extension Elements Save Controller (POST) ===============================
save_extension_elements_claim_life_folder_save_controller_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/save_extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Settlement Folders Collection (GET) =====================================
# ========================= Return the hypermedia of a Settlement Folders Collection (OPTIONS) =========================
settlement_folder_collection_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Settlement Folders Document (GET) ======================================
# ========================== Return the hypermedia of a Settlement Folders Document (OPTIONS) ==========================
settlement_folder_document_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Beneficiary Folders Collection (GET) =====================================
# ======================== Return the hypermedia of a Beneficiary Folders Collection (OPTIONS) =========================
beneficiary_folder_collection_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Beneficiary Folders Document (GET) ======================================
# ========================= Return the hypermedia of a Beneficiary Folders Document (OPTIONS) ==========================
beneficiary_folder_document_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ============================== GET the Cancel Extension Elements Save Controller (GET) ===============================
# =================== Return the hypermedia of a Cancel Extension Elements Save Controller (OPTIONS) ===================
# ============================= POST the Cancel Extension Elements Save Controller (POST) ==============================
cancel_extension_elements_beneficiary_folder_save_controlle_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders/Replace5/cancel_extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Extension Elements Collection (GET) =====================================
# ========================= Return the hypermedia of a Extension Elements Collection (OPTIONS) =========================
# =================================== POST the Extension Elements Collection (POST) ====================================
extension_element_collection_of_the_beneficiary_folder_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders/Replace5/extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Extension Elements Document (GET) ======================================
# ========================== Return the hypermedia of a Extension Elements Document (OPTIONS) ==========================
# ================================== PATCH the Extension Elements Document (PATCH) =====================================
extension_element_document_of_the_beneficiary_folder_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders/Replace5/extension_elements/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Life Settlements Collection (GET) ======================================
# ========================== Return the hypermedia of a Life Settlements Collection (OPTIONS) ==========================
life_settlement_collection_of_the_beneficiary_folder_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders/Replace5/life_settlements',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Life Settlements Document (GET) =======================================
# =========================== Return the hypermedia of a Life Settlements Document (OPTIONS) ===========================
life_settlement_document_of_the_beneficiary_folder_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders/Replace5/life_settlements/Replace6',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================== GET the Party Roles Collection (GET) ========================================
# ============================ Return the hypermedia of a Party Roles Collection (OPTIONS) =============================
# ====================================== POST the Party Roles Collection (POST) ========================================
claim_party_life_collection_of_the_beneficiary_folder_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders/Replace5/party_roles',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Party Roles Document (GET) =========================================
# ============================= Return the hypermedia of a Party Roles Document (OPTIONS) ==============================
# ===================================== DELETE the Party Roles Document (DELETE) =======================================
# ====================================== PATCH the Party Roles Document (PATCH) ========================================
claim_party_life_document_of_the_beneficiary_folder_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders/Replace5/party_roles/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ==================================== GET the Cancel Party Save Controller (GET) ======================================
# ========================== Return the hypermedia of a Cancel Party Save Controller (OPTIONS) =========================
# =================================== POST the Cancel Party Save Controller (POST) =====================================
cancel_party_claim_party_life_save_controller_of_the_beneficiary_folder_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders/Replace5/party_roles/Replace6/cancel_party',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Transfer Party Save Controller (GET) =====================================
# ========================= Return the hypermedia of a Transfer Party Save Controller (OPTIONS) ========================
# ================================== POST the Transfer Party Save Controller (POST) ====================================
transfer_party_claim_party_life_save_controller_of_the_beneficiary_folder_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders/Replace5/party_roles/Replace6/transfer_party',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =============================== GET the Save Extension Elements Save Controller (GET) ================================
# ==================== Return the hypermedia of a Save Extension Elements Save Controller (OPTIONS) ====================
# ============================== POST the Save Extension Elements Save Controller (POST) ===============================
save_extension_elements_beneficiary_folder_save_controller_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/beneficiary_folders/Replace5/save_extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ============================== GET the Cancel Extension Elements Save Controller (GET) ===============================
# =================== Return the hypermedia of a Cancel Extension Elements Save Controller (OPTIONS) ===================
# ============================= POST the Cancel Extension Elements Save Controller (POST) ==============================
cancel_extension_elements_settlement_folder_save_controller_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/cancel_extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Extension Elements Collection (GET) =====================================
# ========================= Return the hypermedia of a Extension Elements Collection (OPTIONS) =========================
# =================================== POST the Extension Elements Collection (POST) ====================================
extension_element_collection_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Extension Elements Document (GET) ======================================
# ========================== Return the hypermedia of a Extension Elements Document (OPTIONS) ==========================
# ================================== PATCH the Extension Elements Document (PATCH) =====================================
extension_element_document_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/extension_elements/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Party Roles Collection (GET) ========================================
# ============================= Return the hypermedia of a Party Roles Collection (OPTIONS) ============================
# ====================================== POST the Party Roles Collection (POST) ========================================
claim_party_life_collection_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/party_roles',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Party Roles Document (GET) ==========================================
# ============================= Return the hypermedia of a Party Roles Document (OPTIONS) ==============================
# ===================================== DELETE the Party Roles Document (DELETE) =======================================
# ====================================== PATCH the Party Roles Document (PATCH) ========================================
claim_party_life_document_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/party_roles/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ==================================== GET the Cancel Party Save Controller (GET) ======================================
# ========================== Return the hypermedia of a Cancel Party Save Controller (OPTIONS) =========================
# =================================== POST the Cancel Party Save Controller (POST) =====================================
cancel_party_claim_party_life_save_controller_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/party_roles/Replace5/cancel_party',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Transfer Party Save Controller (GET) =====================================
# ======================== Return the hypermedia of a Transfer Party Save Controller (OPTIONS) =========================
# ================================== POST the Transfer Party Save Controller (POST) ====================================
transfer_party_claim_party_life_save_controller_of_the_settlement_folder_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/party_roles/Replace5/transfer_party',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =============================== GET the Save Extension Elements Save Controller (GET) ================================
# ==================== Return the hypermedia of a Save Extension Elements Save Controller (OPTIONS) ====================
# ============================== POST the Save Extension Elements Save Controller (POST) ===============================
save_extension_elements_settlement_folder_save_controller_of_the_claim_life_folder_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_life_folders/Replace3/settlement_folders/Replace4/save_extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Claim Periods Collection (GET) =======================================
# =========================== Return the hypermedia of a Claim Periods Collection (OPTIONS) ============================
claim_period_collection_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_periods',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================== GET the Claim Periods Document (GET) ========================================
# ============================ Return the hypermedia of a Claim Periods Document (OPTIONS) =============================
claim_period_document_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_periods/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Extension Elements Collection (GET) =====================================
# ========================= Return the hypermedia of a Extension Elements Collection (OPTIONS) =========================
# ================================== POST the Extension Elements Collection (POST) =====================================
extension_element_collection_of_the_claim_period_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_periods/Replace3/extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Extension Elements Document (GET) ======================================
# ========================== Return the hypermedia of a Extension Elements Document (OPTIONS) ==========================
# ================================== PATCH the Extension Elements Document (PATCH) =====================================
extension_element_document_of_the_claim_period_of_the_claim = {
    'url': 'Replace1/claims/Replace2/claim_periods/Replace3/extension_elements/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# =================================== GET the Information Receipts Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Receipts Collection (OPTIONS) ========================
# ================================= POST the Information Receipts Collection (POST) ====================================
information_receipt_collection_of_the_claim = {
    'url': 'Replace1/claims/Replace2/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Information Receipts Document (GET) =====================================
# ========================= Return the hypermedia of a Information Receipts Document (OPTIONS) =========================
# ================================== PATCH the Information Receipts Document (PATCH) ===================================
information_receipt_document_of_the_claim = {
    'url': 'Replace1/claims/Replace2/information_receipts/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_information_receipt_save_controller_of_the_claim = {
    'url': 'Replace1/claims/Replace2/information_receipts/Replace3/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Multiple Transfer Save Controller (GET) ===================================
# ======================= Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) =======================
# ================================ POST the Multiple Transfer Save Controller (POST) ===================================
multiple_transfer_information_receipt_save_controller_of_the_claim = {
    'url': 'Replace1/claims/Replace2/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Information Requests Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Requests Collection (OPTIONS) ========================
information_request_collection_of_the_claim = {
    'url': 'Replace1/claims/Replace2/information_requests',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Information Requests Document (GET) =====================================
# ========================= Return the hypermedia of a Information Requests Document (OPTIONS) =========================
information_request_document_of_the_claim = {
    'url': 'Replace1/claims/Replace2/information_requests/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Launch View Aia Bridge resource (GET) ====================================
# ======================== Return the hypermedia of a Launch View Aia Bridge resource (OPTIONS) ========================
# ================================= POST the Launch View Aia Bridge resource (POST) ====================================
launch_view_aia_claim_bridge_resource = {
    'url': 'Replace1/claims/Replace2/launch_view_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Life Settlements Collection (GET) ======================================
# ========================== Return the hypermedia of a Life Settlements Collection (OPTIONS) ==========================
life_settlement_collection_of_the_claim = {
    'url': 'Replace1/claims/Replace2/life_settlements',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Life Settlements Document (GET) =======================================
# =========================== Return the hypermedia of a Life Settlements Document (OPTIONS) ===========================
life_settlement_document_of_the_claim = {
    'url': 'Replace1/claims/Replace2/life_settlements/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Manual Tasks Collection (GET) ========================================
# ============================ Return the hypermedia of a Manual Tasks Collection (OPTIONS) ============================
# ====================================== POST the Manual Tasks Collection (POST) =======================================
manual_task_collection_of_the_claim = {
    'url': 'Replace1/claims/Replace2/manual_tasks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Manual Tasks Document (GET) =========================================
# ============================= Return the hypermedia of a Manual Tasks Document (OPTIONS) =============================
# ====================================== PATCH the Manual Tasks Document (PATCH) =======================================
manual_task_document_of_the_claim = {
    'url': 'Replace1/claims/Replace2/manual_tasks/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_manual_task_save_controller_of_the_claim = {
    'url': 'Replace1/claims/Replace2/manual_tasks/Replace3/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_claim = {
    'url': 'Replace1/claims/Replace2/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================== GET the Party Roles Collection (GET) ========================================
# ============================= Return the hypermedia of a Party Roles Collection (OPTIONS) ============================
# ====================================== POST the Party Roles Collection (POST) ========================================
claim_party_life_collection_of_the_claim = {
    'url': 'Replace1/claims/Replace2/party_roles',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Party Roles Document (GET) ==========================================
# ============================= Return the hypermedia of a Party Roles Document (OPTIONS) ==============================
# ====================================== DELETE the Party Roles Document (DELETE) ======================================
# ====================================== PATCH the Party Roles Document (PATCH) ========================================
claim_party_life_document_of_the_claim = {
    'url': 'Replace1/claims/Replace2/party_roles/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ==================================== GET the Cancel Party Save Controller (GET) ======================================
# ========================= Return the hypermedia of a Cancel Party Save Controller (OPTIONS) ==========================
# =================================== POST the Cancel Party Save Controller (POST) =====================================
cancel_party_claim_party_life_save_controller_of_the_claim = {
    'url': 'Replace1/claims/Replace2/party_roles/Replace3/cancel_party',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Transfer Party Save Controller (GET) =====================================
# ======================== Return the hypermedia of a Transfer Party Save Controller (OPTIONS) =========================
# ================================== POST the Transfer Party Save Controller (POST) ====================================
transfer_party_claim_party_life_save_controller_of_the_claim = {
    'url': 'Replace1/claims/Replace2/party_roles/Replace3/transfer_party',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}
