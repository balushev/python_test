# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 18:18:15 2022

@author: bbalushev
"""


# ========================================== GET the Offers Collection (GET) ===========================================
# =============================== Return the hypermedia of a Offers Collection (OPTIONS) ===============================
# ======================================== POST the Offers Collection (POST) ===========================================
offer_collection = {
    'url': 'Replace1/offers',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================================== GET the Offers Document (GET) ============================================
# ================================ Return the hypermedia of a Offers Document (OPTIONS) ================================
# ======================================= DELETE the Offers Document (DELETE) ==========================================
# ========================================= PATCH the Offers Document (PATCH) ==========================================
offer_document = {
    'url': 'Replace1/offers/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Activities Collection (GET) =========================================
# ============================= Return the hypermedia of a Activities Collection (OPTIONS) =============================
activity_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/activities',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Activities Document (GET) ==========================================
# ============================== Return the hypermedia of a Activities Document (OPTIONS) ==============================
activity_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/activities/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_activity_of_the_offer = {
    'url': 'Replace1/offers/Replace2/activities/Replace3/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Process Operation (GET) ===========================================
# =============================== Return the hypermedia of a Process Operation (OPTIONS) ===============================
# ========================================= POST the Process Operation (POST) ==========================================
process_activity_operation_of_the_activity_of_the_offer = {
    'url': 'Replace1/offers/Replace2/activities/Replace3/operations/process',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================== GET the Process Operation (GET) ===========================================
# =============================== Return the hypermedia of a Process Operation (OPTIONS) ===============================
# ======================================= DELETE the Process Operation (DELETE) ========================================
# ======================================== PATCH the Process Operation (PATCH) =========================================
process_activity_operation_of_the_activity_of_the_offer_with_process_id = {
    'url': 'Replace1/offers/Replace2/activities/Replace3/operations/process/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_process_activity_save_controller_of_the_activity_of_the_offer = {
    'url': 'Replace1/offers/Replace2/activities/Replace3/operations/process/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_process_activity_save_controller_of_the_activity_of_the_offer_with_process_id = {
    'url': 'Replace1/offers/Replace2/activities/Replace3/operations/process/Replace4/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Resume In Aia Bridge resource (GET) ====================================
# ========================== Return the hypermedia of a Resume In Aia Bridge resource (OPTIONS) ========================
# =================================== POST the Resume In Aia Bridge resource (POST) ====================================
resume_in_aia_activity_bridge_resource_of_the_offer = {
    'url': 'Replace1/offers/Replace2/activities/Replace3/resume_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Billings Collection (GET) ==========================================
# ============================== Return the hypermedia of a Billings Collection (OPTIONS) ==============================
offer_billing_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/billings',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =========================================== GET the Billings Document (GET) ==========================================
# ================================ Return the hypermedia of a Billings Document (OPTIONS) ==============================
# ======================================== PATCH the Billings Document (PATCH) =========================================
offer_billing_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/billings/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Clauses Collection (GET) ===========================================
# ============================== Return the hypermedia of a Clauses Collection (OPTIONS) ===============================
offer_clause_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/clauses',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =========================================== GET the Clauses Document (GET) ===========================================
# ================================ Return the hypermedia of a Clauses Document (OPTIONS) ===============================
# ======================================== PATCH the Clauses Document (PATCH) ==========================================
offer_clause_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/clauses/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Extension Elements Collection (GET) ====================================
# ========================== Return the hypermedia of a Extension Elements Collection (OPTIONS) ========================
# =================================== POST the Extension Elements Collection (POST) ====================================
extension_element_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Extension Elements Document (GET) ======================================
# ========================== Return the hypermedia of a Extension Elements Document (OPTIONS) ==========================
# =================================== PATCH the Extension Elements Document (PATCH) ====================================
extension_element_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/extension_elements/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Information Receipts Collection (GET) ===================================
# ========================= Return the hypermedia of a Information Receipts Collection (OPTIONS) =======================
# ================================== POST the Information Receipts Collection (POST) ===================================
information_receipt_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Information Receipts Document (GET) ====================================
# ========================== Return the hypermedia of a Information Receipts Document (OPTIONS) ========================
# ================================== PATCH the Information Receipts Document (PATCH) ===================================
information_receipt_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/information_receipts/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_information_receipt_save_controller_of_the_offer = {
    'url': 'Replace1/offers/Replace2/information_receipts/Replace3/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Multiple Transfer Save Controller (GET) ==================================
# ======================== Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) ======================
# ================================= POST the Multiple Transfer Save Controller (POST) ==================================
multiple_transfer_information_receipt_save_controller_of_the_offer = {
    'url': 'Replace1/offers/Replace2/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Initial Payments Collection (GET) ======================================
# ========================== Return the hypermedia of a Initial Payments Collection (OPTIONS) ==========================
offer_initial_payment_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/initial_payments',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Initial Payments Document (GET) =======================================
# =========================== Return the hypermedia of a Initial Payments Document (OPTIONS) ===========================
# ==================================== PATCH the Initial Payments Document (PATCH) =====================================
offer_initial_payment_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/initial_payments/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ================================ GET the Offer Operation Info Sheets Collection (GET) ================================
# ===================== Return the hypermedia of a Offer Operation Info Sheets Collection (OPTIONS) ====================
offer_operation_info_sheet_collection_of_the_offer_initial_payment_of_the_offer = {
    'url': 'Replace1/offers/Replace2/initial_payments/Replace3/offer_operation_info_sheets',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================= GET the Offer Operation Info Sheets Document (GET) =================================
# ====================== Return the hypermedia of a Offer Operation Info Sheets Document (OPTIONS) =====================
# ============================== PATCH the Offer Operation Info Sheets Document (PATCH) ================================
offer_operation_info_sheet_document_of_the_offer_initial_payment_of_the_offer = {
    'url': 'Replace1/offers/Replace2/initial_payments/Replace3/offer_operation_info_sheets/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# =========================================== GET the Notes Collection (GET) ===========================================
# ================================ Return the hypermedia of a Notes Collection (OPTIONS) ===============================
# ========================================= POST the Notes Collection (POST) ===========================================
note_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/notes',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ============================================ GET the Notes Document (GET) ============================================
# ================================= Return the hypermedia of a Notes Document (OPTIONS) ================================
# ======================================== DELETE the Notes Document (DELETE) ==========================================
# ========================================== PATCH the Notes Document (PATCH) ==========================================
note_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/notes/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_note_save_controller_of_the_offer = {
    'url': 'Replace1/offers/Replace2/notes/Replace3/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Offer Operation Info Sheets Collection (GET) ================================
# ===================== Return the hypermedia of a Offer Operation Info Sheets Collection (OPTIONS) ====================
offer_operation_info_sheet_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/offer_operation_info_sheets',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================= GET the Offer Operation Info Sheets Document (GET) =================================
# ====================== Return the hypermedia of a Offer Operation Info Sheets Document (OPTIONS) =====================
# ============================== PATCH the Offer Operation Info Sheets Document (PATCH) ================================
offer_operation_info_sheet_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/offer_operation_info_sheets/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Generate Offer Doc Operation (GET) =====================================
# =========================== Return the hypermedia of Generate Offer Doc Operation (OPTIONS) ==========================
# =================================== POST the Generate Offer Doc Operation (POST) =====================================
generate_offer_doc_operation_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations/generate_offer_doc',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Generate Offer Doc Operation (GET) =====================================
# ========================== Return the hypermedia of a Generate Offer Doc Operation (OPTIONS) =========================
# ================================= DELETE the Generate Offer Doc Operation (DELETE) ===================================
# ================================== PATCH the Generate Offer Doc Operation (PATCH) ====================================
generate_offer_doc_operation_of_the_offer_with_generate_offer_doc_id = {
    'url': 'Replace1/offers/Replace2/operations/generate_offer_doc/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_generate_offer_doc_save_controller_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations/generate_offer_doc/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_generate_offer_doc_save_controller_of_the_offer_with_generate_offer_doc_id = {
    'url': 'Replace1/offers/Replace2/operations/generate_offer_doc/Replace3/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_generate_offer_doc_save_controller_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations/generate_offer_doc/Replace3/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Transfer Amendment Operation (GET) =====================================
# ========================== Return the hypermedia of a Transfer Amendment Operation (OPTIONS) =========================
# =================================== POST the Transfer Amendment Operation (POST) =====================================
transfer_amendment_operation_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations/transfer_amendment',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Transfer Amendment Operation (GET) =====================================
# ========================== Return the hypermedia of a Transfer Amendment Operation (OPTIONS) =========================
# ================================= DELETE the Transfer Amendment Operation (DELETE) ===================================
# =================================== PATCH the Transfer Amendment Operation (PATCH) ===================================
transfer_amendment_operation_of_the_offer_with_transfer_amendment_id = {
    'url': 'Replace1/offers/Replace2/operations/transfer_amendment/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_transfer_amendment_save_controller_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations/transfer_amendment/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_transfer_amendment_save_controller_of_the_offer_with_transfer_amendment_id = {
    'url': 'Replace1/offers/Replace2/operations/transfer_amendment/Replace3/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Available Documents Collection (GET) ====================================
# ========================= Return the hypermedia of a Available Documents Collection (OPTIONS) ========================
# =================================== POST the Available Documents Collection (POST) ===================================
available_document_collection_of_the_transfer_amendment_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations/transfer_amendment/Replace3/available_documents',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Available Documents Document (GET) =====================================
# ========================== Return the hypermedia of a Available Documents Document (OPTIONS) =========================
# =================================== PATCH the Available Documents Document (PATCH) ===================================
available_document_document_of_the_transfer_amendment_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations/transfer_amendment/Replace3/available_documents/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Output Documents Collection (GET) ======================================
# ========================== Return the hypermedia of a Output Documents Collection (OPTIONS) ==========================
# ==================================== POST the Output Documents Collection (POST) =====================================
output_document_collection_of_the_transfer_amendment_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations/transfer_amendment/Replace3/output_documents',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Output Documents Document (GET) ====================================
# ============================== Return the hypermedia of a Output Documents Document (OPTIONS) ========================
# ======================================= PATCH the Output Documents Document (PATCH) ==================================
output_document_document_of_the_transfer_amendment_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations/transfer_amendment/Replace3/output_documents/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Transfer To Contract Operation (GET) ==================================
# =========================== Return the hypermedia of a Transfer To Contract Operation (OPTIONS) ======================
# ==================================== POST the Transfer To Contract Operation (POST) ==================================
transfer_to_contract_operation_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations/transfer_to_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Transfer To Contract Operation (GET) ==================================
# =========================== Return the hypermedia of a Transfer To Contract Operation (OPTIONS) ======================
# =================================== DELETE the Transfer To Contract Operation (DELETE) ===============================
# ==================================== PATCH the Transfer To Contract Operation (PATCH) ================================
transfer_to_contract_operation_of_the_offer_with_transfer_to_contract_id = {
    'url': 'Replace1/offers/Replace2/operations/transfer_to_contract/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_transfer_to_contract_save_controller_of_the_offer = {
    'url': 'Replace1/offers/Replace2/operations/transfer_to_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_transfer_to_contract_save_controller_of_the_offer_with_transfer_to_contract_id = {
    'url': 'Replace1/offers/Replace2/operations/transfer_to_contract/Replace3/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Output Documents Collection (GET) =====================================
# =========================== Return the hypermedia of a Output Documents Collection (OPTIONS) =========================
# ==================================== POST the Output Documents Collection (POST) =====================================
output_document_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/output_documents',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Output Documents Document (GET) ======================================
# ============================ Return the hypermedia of a Output Documents Document (OPTIONS) ==========================
# ==================================== PATCH the Output Documents Document (PATCH) =====================================
output_document_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/output_documents/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Party Roles Collection (GET) ========================================
# ============================= Return the hypermedia of a Party Roles Collection (OPTIONS) ============================
# ======================================= POST the Party Roles Collection (POST) =======================================
offer_party_role_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Party Roles Document (GET) =========================================
# ============================== Return the hypermedia of a Party Roles Document (OPTIONS) =============================
# ===================================== DELETE the Party Roles Document (DELETE) =======================================
# ====================================== PATCH the Party Roles Document (PATCH) ========================================
offer_party_role_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Organizations Collection (GET) =======================================
# ============================ Return the hypermedia of a Organizations Collection (OPTIONS) ===========================
# ====================================== POST the Organizations Collection (POST) ======================================
organization_collection_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Organizations Document (GET) ========================================
# ============================= Return the hypermedia of a Organizations Document (OPTIONS) ============================
# ====================================== PATCH the Organizations Document (PATCH) ======================================
organization_document_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_organization_save_controller_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_organization_save_controller_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Activities Collection (GET) =========================================
# ============================= Return the hypermedia of a Activities Collection (OPTIONS) =============================
activity_collection_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/activities',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Activities Document (GET) ==========================================
# ============================== Return the hypermedia of a Activities Document (OPTIONS) ==============================
activity_document_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/activities/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_activity_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/activities/Replace5/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Process Operation (GET) ===========================================
# =============================== Return the hypermedia of a Process Operation (OPTIONS) ===============================
# ========================================= POST the Process Operation (POST) ==========================================
process_activity_operation_of_the_activity_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/activities/Replace5/operations/process',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================================== GET the Process Operation (GET) ==========================================
# ================================ Return the hypermedia of a Process Operation (OPTIONS) ==============================
# ======================================= DELETE the Process Operation (DELETE) ========================================
# ========================================= PATCH the Process Operation (PATCH) ========================================
process_activity_operation_of_the_activity_of_the_organization_of_the_offer_party_role_of_the_offer_with_process_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/activities/Replace5/operations/process/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_process_activity_save_controller_of_the_activity_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/activities/Replace5/operations/process/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_process_activity_save_controller_of_the_activity_of_the_organization_of_the_offer_party_role_of_the_offer_with_process_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/activities/Replace5/operations/process/Replace6/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Resume In Aia Bridge resource (GET) ====================================
# ========================== Return the hypermedia of a Resume In Aia Bridge resource (OPTIONS) ========================
# =================================== POST the Resume In Aia Bridge resource (POST) ====================================
resume_in_aia_activity_bridge_resource_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/activities/Replace5/resume_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Activity Definitions Collection (GET) ====================================
# ======================== Return the hypermedia of a Activity Definitions Collection (OPTIONS) ========================
activity_definition_collection_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/activity_definitions',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Activity Definitions Document (GET) =====================================
# ========================= Return the hypermedia of a Activity Definitions Document (OPTIONS) =========================
activity_definition_document_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/activity_definitions/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================ GET the Launch Activity In Aia Bridge resource (GET) ================================
# ===================== Return the hypermedia of a Launch Activity In Aia Bridge resource (OPTIONS) ====================
# =============================== POST the Launch Activity In Aia Bridge resource (POST) ===============================
launch_activity_in_aia_activity_definition_bridge_resource_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/activity_definitions/Replace5/launch_activity_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Bank Accounts Collection (GET) =======================================
# ============================ Return the hypermedia of a Bank Accounts Collection (OPTIONS) ===========================
# ====================================== POST the Bank Accounts Collection (POST) ======================================
bank_account_collection_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Bank Accounts Document (GET) ========================================
# ============================= Return the hypermedia of a Bank Accounts Document (OPTIONS) ============================
# ====================================== PATCH the Bank Accounts Document (PATCH) ======================================
bank_account_document_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Bank Mandates Collection (GET) =======================================
# ============================ Return the hypermedia of a Bank Mandates Collection (OPTIONS) ===========================
# ====================================== POST the Bank Mandates Collection (POST) ======================================
bank_mandate_collection_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Bank Mandates Document (GET) ========================================
# ============================= Return the hypermedia of a Bank Mandates Document (OPTIONS) ============================
# ====================================== PATCH the Bank Mandates Document (PATCH) ======================================
bank_mandate_document_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_bank_mandate_save_controller_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_bank_mandate_save_controller_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================= GET the Bank Mandate Add Contract Operation (GET) ==================================
# ====================== Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) ======================
# ================================ POST the Bank Mandate Add Contract Operation (POST) =================================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================= GET the Bank Mandate Add Contract Operation (GET) ==================================
# ====================== Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) ======================
# ============================= DELETE the Bank Mandate Add Contract Operation (DELETE) ================================
# =============================== PATCH the Bank Mandate Add Contract Operation (PATCH) ================================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# ============================== POST the Bank Mandate Remove Contract Operation (POST) ================================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# ============================ DELETE the Bank Mandate Remove Contract Operation (DELETE) ==============================
# ============================== PATCH the Bank Mandate Remove Contract Operation (PATCH) ==============================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Bank Mandate Revoke Operation (GET) ====================================
# ========================== Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) ========================
# =================================== POST the Bank Mandate Revoke Operation (POST) ====================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Bank Mandate Revoke Operation (GET) ====================================
# ========================== Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) ========================
# ================================ DELETE the Bank Mandate Revoke Operation (DELETE) ===================================
# ================================== PATCH the Bank Mandate Revoke Operation (PATCH) ===================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer_with_bank_mandate_revoke_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer_with_bank_mandate_revoke_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the E Mail Addresses Collection (GET) ======================================
# ========================== Return the hypermedia of a E Mail Addresses Collection (OPTIONS) ==========================
# ==================================== POST the E Mail Addresses Collection (POST) =====================================
e_mail_address_collection_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/e_mail_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the E Mail Addresses Document (GET) ======================================
# ============================ Return the hypermedia of a E Mail Addresses Document (OPTIONS) ==========================
# ==================================== PATCH the E Mail Addresses Document (PATCH) =====================================
e_mail_address_document_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/e_mail_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Information Receipts Collection (GET) ==================================
# ========================== Return the hypermedia of a Information Receipts Collection (OPTIONS) ======================
# =================================== POST the Information Receipts Collection (POST) ==================================
information_receipt_collection_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Information Receipts Document (GET) ====================================
# ========================== Return the hypermedia of a Information Receipts Document (OPTIONS) ========================
# =================================== PATCH the Information Receipts Document (PATCH) ==================================
information_receipt_document_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/information_receipts/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_information_receipt_save_controller_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/information_receipts/Replace5/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Multiple Transfer Save Controller (GET) ===================================
# ======================= Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) =======================
# ================================= POST the Multiple Transfer Save Controller (POST) ==================================
multiple_transfer_information_receipt_save_controller_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Information Requests Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Requests Collection (OPTIONS) ========================
information_request_collection_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/information_requests',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Information Requests Document (GET) =====================================
# ========================= Return the hypermedia of a Information Requests Document (OPTIONS) =========================
information_request_document_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/information_requests/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Launch View Aia Bridge resource (GET) ===================================
# ========================= Return the hypermedia of a Launch View Aia Bridge resource (OPTIONS) =======================
# ================================== POST the Launch View Aia Bridge resource (POST) ===================================
launch_view_aia_organization_bridge_resource_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/launch_view_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Manual Tasks Collection (GET) ========================================
# ============================ Return the hypermedia of a Manual Tasks Collection (OPTIONS) ============================
# ====================================== POST the Manual Tasks Collection (POST) =======================================
manual_task_collection_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/manual_tasks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Manual Tasks Document (GET) ===========================================
# =========================== Return the hypermedia of a Manual Tasks Document (OPTIONS) ===============================
# =================================== PATCH the Manual Tasks Document (PATCH) ==========================================
manual_task_document_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/manual_tasks/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Transfer Save Controller (GET) ==========================================
# ========================= Return the hypermedia of a Transfer Save Controller (OPTIONS) ==============================
# ================================== POST the Transfer Save Controller (POST) ==========================================
transfer_manual_task_save_controller_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/manual_tasks/Replace5/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================= GET the Organization Info Sheets Collection (GET) ==================================
# ====================== Return the hypermedia of a Organization Info Sheets Collection (OPTIONS) ======================
organization_info_sheet_collection_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/organization_info_sheets',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Organization Info Sheets Document (GET) ==================================
# ======================== Return the hypermedia of a Organization Info Sheets Document (OPTIONS) ======================
# ================================ PATCH the Organization Info Sheets Document (PATCH) =================================
organization_info_sheet_document_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/organization_info_sheets/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Pay Points Collection (GET) =========================================
# ============================= Return the hypermedia of a Pay Points Collection (OPTIONS) =============================
pay_point_collection_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/pay_points',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Pay Points Document (GET) ==========================================
# ============================== Return the hypermedia of a Pay Points Document (OPTIONS) ==============================
pay_point_document_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/pay_points/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Phone Addresses Collection (GET) ======================================
# =========================== Return the hypermedia of a Phone Addresses Collection (OPTIONS) ==========================
# ==================================== POST the Phone Addresses Collection (POST) ======================================
phone_address_collection_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/phone_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Phone Addresses Document (GET) =======================================
# ============================ Return the hypermedia of a Phone Addresses Document (OPTIONS) ===========================
# ===================================== PATCH the Phone Addresses Document (PATCH) =====================================
phone_address_document_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/phone_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Postal Addresses Collection (GET) ======================================
# ========================== Return the hypermedia of a Postal Addresses Collection (OPTIONS) ==========================
# ==================================== POST the Postal Addresses Collection (POST) =====================================
postal_address_collection_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/postal_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Postal Addresses Document (GET) ======================================
# ============================ Return the hypermedia of a Postal Addresses Document (OPTIONS) ==========================
# =================================== DELETE the Postal Addresses Document (DELETE) ====================================
# ==================================== PATCH the Postal Addresses Document (PATCH) =====================================
postal_address_document_of_the_organization_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/organizations/Replace4/postal_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ========================================== GET the Persons Collection (GET) ==========================================
# =============================== Return the hypermedia of a Persons Collection (OPTIONS) ==============================
# ======================================== POST the Persons Collection (POST) ==========================================
person_collection_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================================== GET the Persons Document (GET) ===========================================
# ================================ Return the hypermedia of a Persons Document (OPTIONS) ===============================
# ======================================== PATCH the Persons Document (PATCH) ==========================================
person_document_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_person_save_controller_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_person_save_controller_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Activities Collection (GET) =========================================
# ============================= Return the hypermedia of a Activities Collection (OPTIONS) =============================
activity_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/activities',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Activities Document (GET) ==========================================
# ============================== Return the hypermedia of a Activities Document (OPTIONS) ==============================
activity_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/activities/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_activity_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/activities/Replace5/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Process Operation (GET) ===========================================
# =============================== Return the hypermedia of a Process Operation (OPTIONS) ===============================
# ========================================= POST the Process Operation (POST) ==========================================
process_activity_operation_of_the_activity_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/activities/Replace5/operations/process',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================================== GET the Process Operation (GET) ==========================================
# ================================ Return the hypermedia of a Process Operation (OPTIONS) ==============================
# ======================================== DELETE the Process Operation (DELETE) =======================================
# ========================================= PATCH the Process Operation (PATCH) ========================================
process_activity_operation_of_the_activity_of_the_person_of_the_offer_party_role_of_the_offer_with_process_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/activities/Replace5/operations/process/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ======================================= POST the Execute Save Controller (POST) ======================================
execute_process_activity_save_controller_of_the_activity_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/activities/Replace5/operations/process/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_process_activity_save_controller_of_the_activity_of_the_person_of_the_offer_party_role_of_the_offer_with_process_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/activities/Replace5/operations/process/Replace6/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Resume In Aia Bridge resource (GET) ====================================
# ========================== Return the hypermedia of a Resume In Aia Bridge resource (OPTIONS) ========================
# =================================== POST the Resume In Aia Bridge resource (POST) ====================================
resume_in_aia_activity_bridge_resource_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/activities/Replace5/resume_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Activity Definitions Collection (GET) ====================================
# ======================== Return the hypermedia of a Activity Definitions Collection (OPTIONS) ========================
activity_definition_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/activity_definitions',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Activity Definitions Document (GET) =====================================
# ========================= Return the hypermedia of a Activity Definitions Document (OPTIONS) =========================
activity_definition_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/activity_definitions/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================ GET the Launch Activity In Aia Bridge resource (GET) ================================
# ===================== Return the hypermedia of a Launch Activity In Aia Bridge resource (OPTIONS) ====================
# ============================== POST the Launch Activity In Aia Bridge resource (POST) ================================
launch_activity_in_aia_activity_definition_bridge_resource_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/activity_definitions/Replace5/launch_activity_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Bank Accounts Collection (GET) =======================================
# ============================ Return the hypermedia of a Bank Accounts Collection (OPTIONS) ===========================
# ===================================== POST the Bank Accounts Collection (POST) =======================================
bank_account_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Bank Accounts Document (GET) ========================================
# ============================= Return the hypermedia of a Bank Accounts Document (OPTIONS) ============================
# ====================================== PATCH the Bank Accounts Document (PATCH) ======================================
bank_account_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Bank Mandates Collection (GET) =======================================
# ============================ Return the hypermedia of a Bank Mandates Collection (OPTIONS) ===========================
# ===================================== POST the Bank Mandates Collection (POST) =======================================
bank_mandate_collection_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Bank Mandates Document (GET) ========================================
# ============================= Return the hypermedia of a Bank Mandates Document (OPTIONS) ============================
# ===================================== PATCH the Bank Mandates Document (PATCH) =======================================
bank_mandate_document_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_bank_mandate_save_controller_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_bank_mandate_save_controller_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================== GET the Bank Mandate Add Contract Operation (GET) =================================
# ======================= Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) =====================
# ================================ POST the Bank Mandate Add Contract Operation (POST) =================================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Bank Mandate Add Contract Operation (GET) =================================
# ======================= Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) =====================
# ============================== DELETE the Bank Mandate Add Contract Operation (DELETE) ===============================
# =============================== PATCH the Bank Mandate Add Contract Operation (PATCH) ================================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ======================================= POST the Execute Save Controller (POST) ======================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# ============================== POST the Bank Mandate Remove Contract Operation (POST) ================================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# ============================ DELETE the Bank Mandate Remove Contract Operation (DELETE) ==============================
# ============================== PATCH the Bank Mandate Remove Contract Operation (PATCH) ==============================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Cancel Save Controller (GET) ===========================================
# ========================== Return the hypermedia of a Cancel Save Controller (OPTIONS) ===============================
# ==================================== POST the Cancel Save Controller (POST) ==========================================
cancel_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Bank Mandate Revoke Operation (GET) =======================================
# ======================= Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) ===========================
# ================================= POST the Bank Mandate Revoke Operation (POST) ======================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Bank Mandate Revoke Operation (GET) =======================================
# ======================= Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) ===========================
# =============================== DELETE the Bank Mandate Revoke Operation (DELETE) ====================================
# ================================ PATCH the Bank Mandate Revoke Operation (PATCH) =====================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer_with_bank_mandate_revoke_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer_with_bank_mandate_revoke_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the E Mail Addresses Collection (GET) =====================================
# =========================== Return the hypermedia of a E Mail Addresses Collection (OPTIONS) =========================
# ==================================== POST the E Mail Addresses Collection (POST) =====================================
e_mail_address_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/e_mail_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the E Mail Addresses Document (GET) =====================================
# ============================= Return the hypermedia of a E Mail Addresses Document (OPTIONS) =========================
# ===================================== PATCH the E Mail Addresses Document (PATCH) ====================================
e_mail_address_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/e_mail_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Family Members Collection (GET) ======================================
# ============================ Return the hypermedia of a Family Members Collection (OPTIONS) ==========================
# ===================================== POST the Family Members Collection (POST) ======================================
family_member_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/family_members',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Family Members Document (GET) =======================================
# ============================= Return the hypermedia of a Family Members Document (OPTIONS) ===========================
# ====================================== PATCH the Family Members Document (PATCH) ====================================
family_member_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/family_members/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Information Receipts Collection (GET) ===================================
# ========================= Return the hypermedia of a Information Receipts Collection (OPTIONS) =======================
# ================================== POST the Information Receipts Collection (POST) ===================================
information_receipt_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Information Receipts Document (GET) ====================================
# ========================== Return the hypermedia of a Information Receipts Document (OPTIONS) ========================
# ================================== PATCH the Information Receipts Document (PATCH) ===================================
information_receipt_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/information_receipts/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ====================================== POST the Transfer Save Controller (POST) ======================================
transfer_information_receipt_save_controller_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/information_receipts/Replace5/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Multiple Transfer Save Controller (GET) ==================================
# ======================== Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) ======================
# ================================= POST the Multiple Transfer Save Controller (POST) ==================================
multiple_transfer_information_receipt_save_controller_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Information Requests Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Requests Collection (OPTIONS) ========================
information_request_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/information_requests',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Information Requests Document (GET) =====================================
# ========================= Return the hypermedia of a Information Requests Document (OPTIONS) =========================
information_request_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/information_requests/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Launch View Aia Bridge resource (GET) ====================================
# ======================== Return the hypermedia of a Launch View Aia Bridge resource (OPTIONS) ========================
# ================================== POST the Launch View Aia Bridge resource (POST) ===================================
launch_view_aia_person_bridge_resource_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/launch_view_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================== GET the Manual Tasks Collection (GET) =====================================
# =============================== Return the hypermedia of a Manual Tasks Collection (OPTIONS) =========================
# ======================================== POST the Manual Tasks Collection (POST) =====================================
manual_task_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/manual_tasks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================================== GET the Manual Tasks Document (GET) ======================================
# ================================ Return the hypermedia of a Manual Tasks Document (OPTIONS) ==========================
# ======================================== PATCH the Manual Tasks Document (PATCH) =====================================
manual_task_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/manual_tasks/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================== GET the Transfer Save Controller (GET) ====================================
# =============================== Return the hypermedia of a Transfer Save Controller (OPTIONS) ========================
# ======================================== POST the Transfer Save Controller (POST) ====================================
transfer_manual_task_save_controller_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/manual_tasks/Replace5/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Occupations Collection (GET) ========================================
# ============================= Return the hypermedia of a Occupations Collection (OPTIONS) ============================
# ====================================== POST the Occupations Collection (POST) ========================================
occupation_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Occupations Document (GET) =========================================
# ============================== Return the hypermedia of a Occupations Document (OPTIONS) =============================
# ======================================= PATCH the Occupations Document (PATCH) =======================================
occupation_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_occupation_save_controller_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_occupation_save_controller_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Create Membership Operation (GET) ======================================
# ========================== Return the hypermedia of a Create Membership Operation (OPTIONS) ==========================
# ==================================== POST the Create Membership Operation (POST) =====================================
create_membership_operation_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/create_membership',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Create Membership Operation (GET) ======================================
# ========================== Return the hypermedia of a Create Membership Operation (OPTIONS) ==========================
# ================================== DELETE the Create Membership Operation (DELETE) ===================================
# =================================== PATCH the Create Membership Operation (PATCH) ====================================
create_membership_operation_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer_with_create_membership_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/create_membership/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_create_membership_save_controller_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/create_membership/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_create_membership_save_controller_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer_with_create_membership_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/create_membership/Replace6/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_create_membership_save_controller_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/create_membership/Replace6/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Generate Required Memberships Operation (GET) ===============================
# ===================== Return the hypermedia of a Generate Required Memberships Operation (OPTIONS) ===================
# ============================== POST the Generate Required Memberships Operation (POST) ===============================
generate_required_memberships_operation_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/generate_required_memberships',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =============================== GET the Generate Required Memberships Operation (GET) ================================
# ==================== Return the hypermedia of a Generate Required Memberships Operation (OPTIONS) ====================
# =========================== DELETE the Generate Required Memberships Operation (DELETE) ==============================
# ============================= PATCH the Generate Required Memberships Operation (PATCH) ==============================
generate_required_memberships_operation_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer_with_generate_required_memberships_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/generate_required_memberships/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_generate_required_memberships_save_controller_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/generate_required_memberships/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS==) =========================
# ======================================= POST the Execute Save Controller (POST) ======================================
execute_generate_required_memberships_save_controller_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer_with_generate_required_memberships_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/generate_required_memberships/Replace6/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_generate_required_memberships_save_controller_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/generate_required_memberships/Replace6/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Unblock T P Rights Operation (GET) =====================================
# ========================== Return the hypermedia of a Unblock T P Rights Operation (OPTIONS) =========================
# =================================== POST the Unblock T P Rights Operation (POST) =====================================
unblock_t_p_rights_operation_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/unblock_t_p_rights',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Unblock T P Rights Operation (GET) ===================================
# =========================== Return the hypermedia of a Unblock T P Rights Operation (OPTIONS) ========================
# ================================== DELETE the Unblock T P Rights Operation (DELETE) ==================================
# =================================== PATCH the Unblock T P Rights Operation (PATCH) ===================================
unblock_t_p_rights_operation_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer_with_unblock_tp_rights_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/unblock_t_p_rights/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_unblock_t_p_rights_save_controller_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/unblock_t_p_rights/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_unblock_t_p_rights_save_controller_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer_with_unblock_tp_rights_id = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/unblock_t_p_rights/Replace6/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_unblock_t_p_rights_save_controller_of_the_occupation_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/occupations/Replace5/operations/unblock_t_p_rights/Replace6/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Person Info Sheets Collection (GET) =====================================
# ========================= Return the hypermedia of a Person Info Sheets Collection (OPTIONS) =========================
person_info_sheet_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/person_info_sheets',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Person Info Sheets Document (GET) =====================================
# =========================== Return the hypermedia of a Person Info Sheets Document (OPTIONS) =========================
# ==================================== PATCH the Person Info Sheets Document (PATCH) ===================================
person_info_sheet_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/person_info_sheets/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Phone Addresses Collection (GET) ======================================
# =========================== Return the hypermedia of a Phone Addresses Collection (OPTIONS) ==========================
# ==================================== POST the Phone Addresses Collection (POST) ======================================
phone_address_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/phone_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Phone Addresses Document (GET) ========================================
# =========================== Return the hypermedia of a Phone Addresses Document (OPTIONS) ============================
# ==================================== PATCH the Phone Addresses Document (PATCH) ======================================
phone_address_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/phone_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Postal Addresses Collection (GET) =====================================
# =========================== Return the hypermedia of a Postal Addresses Collection (OPTIONS) =========================
# ==================================== POST the Postal Addresses Collection (POST) =====================================
postal_address_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/postal_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Postal Addresses Document (GET) =======================================
# =========================== Return the hypermedia of a Postal Addresses Document (OPTIONS) ===========================
# =================================== DELETE the Postal Addresses Document (DELETE) ====================================
# ===================================== PATCH the Postal Addresses Document (PATCH) ====================================
postal_address_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/postal_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# =================================== GET the Social Security I Ds Collection (GET) ====================================
# ======================== Return the hypermedia of a Social Security I Ds Collection (OPTIONS) ========================
social_security_i_d_collection_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/social_security_i_ds',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Social Security I Ds Document (GET) =====================================
# ========================= Return the hypermedia of a Social Security I Ds Document (OPTIONS) =========================
social_security_i_d_document_of_the_person_of_the_offer_party_role_of_the_offer = {
    'url': 'Replace1/offers/Replace2/party_roles/Replace3/persons/Replace4/social_security_i_ds/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Questionnaires Collection (GET) =======================================
# =========================== Return the hypermedia of a Questionnaires Collection (OPTIONS) ===========================
offer_questionnaire_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/questionnaires',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Questionnaires Document (GET) =========================================
# =========================== Return the hypermedia of a Questionnaires Document (OPTIONS) =============================
offer_questionnaire_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/questionnaires/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Question Answers Collection (GET) ======================================
# ========================== Return the hypermedia of a Question Answers Collection (OPTIONS) ==========================
offer_question_answer_collection_of_the_offer_questionnaire_of_the_offer = {
    'url': 'Replace1/offers/Replace2/questionnaires/Replace3/question_answers',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Question Answers Document (GET) ======================================
# ============================ Return the hypermedia of a Question Answers Document (OPTIONS) ==========================
# ==================================== PATCH the Question Answers Document (PATCH) =====================================
offer_question_answer_document_of_the_offer_questionnaire_of_the_offer = {
    'url': 'Replace1/offers/Replace2/questionnaires/Replace3/question_answers/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Validate Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Validate Save Controller (OPTIONS) ===========================
# ===================================== POST the Validate Save Controller (POST) =======================================
validate_offer_questionnaire_save_controller_of_the_offer = {
    'url': 'Replace1/offers/Replace2/questionnaires/Replace3/validate',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Resume Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Resume Save Controller (OPTIONS) ============================
# ====================================== POST the Resume Save Controller (POST) ========================================
resume_offer_save_controller = {
    'url': 'Replace1/offers/Replace2/resume',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================================== GET the Risks Collection (GET) ===========================================
# ================================ Return the hypermedia of a Risks Collection (OPTIONS) ===============================
# ========================================= POST the Risks Collection (POST) ===========================================
offer_risk_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ============================================ GET the Risks Document (GET) ============================================
# ================================= Return the hypermedia of a Risks Document (OPTIONS) ================================
# ======================================== DELETE the Risks Document (DELETE) ==========================================
# ========================================== PATCH the Risks Document (PATCH) ==========================================
offer_risk_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ========================================== GET the Drivers Collection (GET) ==========================================
# =============================== Return the hypermedia of a Drivers Collection (OPTIONS) ==============================
# ======================================== POST the Drivers Collection (POST) ==========================================
offer_driver_collection_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/drivers',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================================== GET the Drivers Document (GET) ===========================================
# ================================ Return the hypermedia of a Drivers Document (OPTIONS) ===============================
# ======================================== DELETE the Drivers Document (DELETE) ========================================
# ========================================= PATCH the Drivers Document (PATCH) =========================================
offer_driver_document_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/drivers/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ==================================== GET the Evaluate Value Save Controller (GET) ====================================
# ========================= Return the hypermedia of a Evaluate Value Save Controller (OPTIONS) ========================
# =================================== POST the Evaluate Value Save Controller (POST) ===================================
evaluate_value_offer_risk_save_controller_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/evaluate_value',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Extension Elements Collection (GET) ====================================
# ========================== Return the hypermedia of a Extension Elements Collection (OPTIONS) ========================
# ==================================== POST the Extension Elements Collection (POST) ===================================
extension_element_collection_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/extension_elements',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Extension Elements Document (GET) ====================================
# ============================ Return the hypermedia of a Extension Elements Document (OPTIONS) ========================
# ==================================== PATCH the Extension Elements Document (PATCH) ===================================
extension_element_document_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/extension_elements/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Organizations Collection (GET) =======================================
# ============================ Return the hypermedia of a Organizations Collection (OPTIONS) ===========================
# ====================================== POST the Organizations Collection (POST) ======================================
organization_collection_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Organizations Document (GET) ========================================
# ============================= Return the hypermedia of a Organizations Document (OPTIONS) ============================
# ====================================== PATCH the Organizations Document (PATCH) ======================================
organization_document_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_organization_save_controller_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_organization_save_controller_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Activities Collection (GET) =========================================
# ============================= Return the hypermedia of a Activities Collection (OPTIONS) =============================
activity_collection_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/activities',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Activities Document (GET) ==========================================
# ============================== Return the hypermedia of a Activities Document (OPTIONS) ==============================
activity_document_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/activities/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_activity_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/activities/Replace5/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Process Operation (GET) ============================================
# ============================== Return the hypermedia of a Process Operation (OPTIONS) ================================
# ======================================= POST the Process Operation (POST) ============================================
process_activity_operation_of_the_activity_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/activities/Replace5/operations/process',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================== GET the Process Operation (GET) ===========================================
# =============================== Return the hypermedia of a Process Operation (OPTIONS) ===============================
# ======================================= DELETE the Process Operation (DELETE) ========================================
# ======================================== PATCH the Process Operation (PATCH) =========================================
process_activity_operation_of_the_activity_of_the_organization_of_the_offer_risk_of_the_offer_with_process_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/activities/Replace5/operations/process/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_process_activity_save_controller_of_the_activity_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/activities/Replace5/operations/process/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_process_activity_save_controller_of_the_activity_of_the_organization_of_the_offer_risk_of_the_offer_with_process_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/activities/Replace5/operations/process/Replace6/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Resume In Aia Bridge resource (GET) =====================================
# ========================= Return the hypermedia of a Resume In Aia Bridge resource (OPTIONS) =========================
# =================================== POST the Resume In Aia Bridge resource (POST) ====================================
resume_in_aia_activity_bridge_resource_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/activities/Replace5/resume_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Activity Definitions Collection (GET) ====================================
# ======================== Return the hypermedia of a Activity Definitions Collection (OPTIONS) ========================
activity_definition_collection_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/activity_definitions',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Activity Definitions Document (GET) =====================================
# ========================= Return the hypermedia of a Activity Definitions Document (OPTIONS) =========================
activity_definition_document_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1offers/Replace2/risks/Replace3/organizations/Replace4/activity_definitions/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================ GET the Launch Activity In Aia Bridge resource (GET) ================================
# ===================== Return the hypermedia of a Launch Activity In Aia Bridge resource (OPTIONS) ====================
# =============================== POST the Launch Activity In Aia Bridge resource (POST) ===============================
launch_activity_in_aia_activity_definition_bridge_resource_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/activity_definitions/Replace5/launch_activity_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Bank Accounts Collection (GET) =======================================
# ============================ Return the hypermedia of a Bank Accounts Collection (OPTIONS) ===========================
# ===================================== POST the Bank Accounts Collection (POST) =======================================
bank_account_collection_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Bank Accounts Document (GET) ========================================
# ============================= Return the hypermedia of a Bank Accounts Document (OPTIONS) ============================
# ====================================== PATCH the Bank Accounts Document (PATCH) ======================================
bank_account_document_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Bank Mandates Collection (GET) =======================================
# ============================ Return the hypermedia of a Bank Mandates Collection (OPTIONS) ===========================
# ====================================== POST the Bank Mandates Collection (POST) ======================================
bank_mandate_collection_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Bank Mandates Document (GET) ========================================
# ============================= Return the hypermedia of a Bank Mandates Document (OPTIONS) ============================
# ===================================== PATCH the Bank Mandates Document (PATCH) =======================================
bank_mandate_document_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_bank_mandate_save_controller_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_bank_mandate_save_controller_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================== GET the Bank Mandate Add Contract Operation (GET) =================================
# ======================= Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) =====================
# ================================ POST the Bank Mandate Add Contract Operation (POST) =================================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Bank Mandate Add Contract Operation (GET) =================================
# ======================= Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) =====================
# ============================= DELETE the Bank Mandate Add Contract Operation (DELETE) ================================
# =============================== PATCH the Bank Mandate Add Contract Operation (PATCH) ================================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# =========================================== GET the Execute Save Controller (GET) ====================================
# ================================ Return the hypermedia of a Execute Save Controller (OPTIONS) ========================
# ========================================= POST the Execute Save Controller (POST) ====================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================================== GET the Execute Save Controller (GET) ====================================
# ================================ Return the hypermedia of a Execute Save Controller (OPTIONS) ========================
# ========================================== POST the Execute Save Controller (POST) ===================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================================== GET the Cancel Save Controller (GET) =====================================
# ================================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =========================
# ========================================= POST the Cancel Save Controller (POST) =====================================
cancel_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# ============================== POST the Bank Mandate Remove Contract Operation (POST) ================================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# ============================ DELETE the Bank Mandate Remove Contract Operation (DELETE) ==============================
# ============================== PATCH the Bank Mandate Remove Contract Operation (PATCH) ==============================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Bank Mandate Revoke Operation (GET) =================================
# ============================= Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) =====================
# ====================================== POST the Bank Mandate Revoke Operation (POST) =================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Bank Mandate Revoke Operation (GET) ====================================
# ========================== Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) ========================
# ================================ DELETE the Bank Mandate Revoke Operation (DELETE) ===================================
# ================================== PATCH the Bank Mandate Revoke Operation (PATCH) ===================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer_with_bank_mandate_revoke_id = {
    'url': 'Replace1offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer_with_bank_mandate_revoke_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the E Mail Addresses Collection (GET) =====================================
# =========================== Return the hypermedia of a E Mail Addresses Collection (OPTIONS) =========================
# ==================================== POST the E Mail Addresses Collection (POST) =====================================
e_mail_address_collection_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/e_mail_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the E Mail Addresses Document (GET) =====================================
# ============================= Return the hypermedia of a E Mail Addresses Document (OPTIONS) =========================
# ===================================== PATCH the E Mail Addresses Document (PATCH) ====================================
e_mail_address_document_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/e_mail_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Information Receipts Collection (GET) ===================================
# ========================= Return the hypermedia of a Information Receipts Collection (OPTIONS) =======================
# ================================== POST the Information Receipts Collection (POST) ===================================
information_receipt_collection_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Information Receipts Document (GET) =====================================
# ========================= Return the hypermedia of a Information Receipts Document (OPTIONS) =========================
# ================================== PATCH the Information Receipts Document (PATCH) ===================================
information_receipt_document_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/information_receipts/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_information_receipt_save_controller_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/information_receipts/Replace5/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Multiple Transfer Save Controller (GET) ==================================
# ======================== Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) ======================
# ================================== POST the Multiple Transfer Save Controller (POST) =================================
multiple_transfer_information_receipt_save_controller_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Information Requests Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Requests Collection (OPTIONS) ========================
information_request_collection_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/information_requests',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Information Requests Document (GET) =====================================
# ========================= Return the hypermedia of a Information Requests Document (OPTIONS) =========================
information_request_document_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/information_requests/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Launch View Aia Bridge resource (GET) ===================================
# ========================= Return the hypermedia of a Launch View Aia Bridge resource (OPTIONS) =======================
# ================================== POST the Launch View Aia Bridge resource (POST) ===================================
launch_view_aia_organization_bridge_resource_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/launch_view_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Manual Tasks Collection (GET) ==========================================
# =========================== Return the hypermedia of a Manual Tasks Collection (OPTIONS) =============================
# ==================================== POST the Manual Tasks Collection (POST) =========================================
manual_task_collection_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/manual_tasks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Manual Tasks Document (GET) =========================================
# ============================= Return the hypermedia of a Manual Tasks Document (OPTIONS) =============================
# ====================================== PATCH the Manual Tasks Document (PATCH) =======================================
manual_task_document_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/manual_tasks/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_manual_task_save_controller_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/manual_tasks/Replace5/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================= GET the Organization Info Sheets Collection (GET) ==================================
# ====================== Return the hypermedia of a Organization Info Sheets Collection (OPTIONS) ======================
organization_info_sheet_collection_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/organization_info_sheets',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Organization Info Sheets Document (GET) ==================================
# ======================== Return the hypermedia of a Organization Info Sheets Document (OPTIONS) ======================
# ================================ PATCH the Organization Info Sheets Document (PATCH) =================================
organization_info_sheet_document_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/organization_info_sheets/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Pay Points Collection (GET) =========================================
# ============================= Return the hypermedia of a Pay Points Collection (OPTIONS) =============================
pay_point_collection_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/pay_points',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Pay Points Document (GET) ==========================================
# ============================== Return the hypermedia of a Pay Points Document (OPTIONS) ==============================
pay_point_document_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/pay_points/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Phone Addresses Collection (GET) ======================================
# =========================== Return the hypermedia of a Phone Addresses Collection (OPTIONS) ==========================
# ===================================== POST the Phone Addresses Collection (POST) =====================================
phone_address_collection_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/phone_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Phone Addresses Document (GET) =======================================
# ============================ Return the hypermedia of a Phone Addresses Document (OPTIONS) ===========================
# ==================================== PATCH the Phone Addresses Document (PATCH) ======================================
phone_address_document_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/phone_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Postal Addresses Collection (GET) ======================================
# ========================== Return the hypermedia of a Postal Addresses Collection (OPTIONS) ==========================
# =================================== POST the Postal Addresses Collection (POST) ======================================
postal_address_collection_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/organizations/Replace4/postal_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Postal Addresses Document (GET) =======================================
# =========================== Return the hypermedia of a Postal Addresses Document (OPTIONS) ===========================
# ================================== DELETE the Postal Addresses Document (DELETE) =====================================
# =================================== PATCH the Postal Addresses Document (PATCH) ======================================
postal_address_document_of_the_organization_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1offers/Replace2/risks/Replace3/organizations/Replace4/postal_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ========================================== GET the Persons Collection (GET) ==========================================
# =============================== Return the hypermedia of a Persons Collection (OPTIONS) ==============================
# ======================================== POST the Persons Collection (POST) ==========================================
person_collection_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================================== GET the Persons Document (GET) ===========================================
# ================================ Return the hypermedia of a Persons Document (OPTIONS) ===============================
# ========================================= PATCH the Persons Document (PATCH) =========================================
person_document_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_person_save_controller_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_person_save_controller_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Activities Collection (GET) =========================================
# ============================= Return the hypermedia of a Activities Collection (OPTIONS) =============================
activity_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/activities',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Activities Document (GET) ==========================================
# ============================== Return the hypermedia of a Activities Document (OPTIONS) ==============================
activity_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/activities/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Operations Collection (GET) ========================================
# ============================== Return the hypermedia of a Operations Collection (OPTIONS) ============================
operation_collection_of_the_activity_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/activities/Replace5/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================ GET the Process Operation (GET) =======================================
# ===================== Return the hypermedia of a Process Operation (OPTIONS) ===========================
# ============================== POST the Process Operation (POST) ======================================
process_activity_operation_of_the_activity_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/activities/Replace5/operations/process',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================== GET the Process Operation (GET) ===========================================
# ============================ ===Return the hypermedia of a Process Operation (OPTIONS) ===============================
# ===================================== DELETE the Process Operation (DELETE) ==========================================
# ======================================= PATCH the Process Operation (PATCH) ==========================================
process_activity_operation_of_the_activity_of_the_person_of_the_offer_risk_of_the_offer_with_process_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/activities/Replace5/operations/process/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_process_activity_save_controller_of_the_activity_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/activities/Replace5/operations/process/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_process_activity_save_controller_of_the_activity_of_the_person_of_the_offer_risk_of_the_offer_with_process_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/activities/Replace5/operations/process/Replace6/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Resume In Aia Bridge resource (GET) ====================================
# ========================== Return the hypermedia of a Resume In Aia Bridge resource (OPTIONS) ========================
# =================================== POST the Resume In Aia Bridge resource (POST) ====================================
resume_in_aia_activity_bridge_resource_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/activities/Replace5/resume_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Activity Definitions Collection (GET) ====================================
# ======================== Return the hypermedia of a Activity Definitions Collection (OPTIONS) ========================
activity_definition_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/activity_definitions',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Activity Definitions Document (GET) =====================================
# ========================= Return the hypermedia of a Activity Definitions Document (OPTIONS) =========================
activity_definition_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/activity_definitions/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================ GET the Launch Activity In Aia Bridge resource (GET) ================================
# ===================== Return the hypermedia of a Launch Activity In Aia Bridge resource (OPTIONS) ====================
# ============================== POST the Launch Activity In Aia Bridge resource (POST) ================================
launch_activity_in_aia_activity_definition_bridge_resource_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/activity_definitions/Replace5/launch_activity_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Bank Accounts Collection (GET) ========================================
# =========================== Return the hypermedia of a Bank Accounts Collection (OPTIONS) ============================
# ==================================== POST the Bank Accounts Collection (POST) ========================================
bank_account_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Bank Accounts Document (GET) ========================================
# ============================= Return the hypermedia of a Bank Accounts Document (OPTIONS) ============================
# ===================================== PATCH the Bank Accounts Document (PATCH) =======================================
bank_account_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Bank Mandates Collection (GET) =======================================
# ============================ Return the hypermedia of a Bank Mandates Collection (OPTIONS) ===========================
# ===================================== POST the Bank Mandates Collection (POST) =======================================
bank_mandate_collection_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Bank Mandates Document (GET) ========================================
# ============================= Return the hypermedia of a Bank Mandates Document (OPTIONS) ============================
# ====================================== PATCH the Bank Mandates Document (PATCH) ======================================
bank_mandate_document_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================= POST the Save Save Controller (POST) =========================================
save_bank_mandate_save_controller_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_bank_mandate_save_controller_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================== GET the Operations Collection (GET) =======================================
# =============================== Return the hypermedia of a Operations Collection (OPTIONS) ===========================
operation_collection_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================== GET the Bank Mandate Add Contract Operation (GET) =================================
# ======================= Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) =====================
# ================================ POST the Bank Mandate Add Contract Operation (POST) =================================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Bank Mandate Add Contract Operation (GET) =================================
# ======================= Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) =====================
# ============================= DELETE the Bank Mandate Add Contract Operation (DELETE) ================================
# =============================== PATCH the Bank Mandate Add Contract Operation (PATCH) ================================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_add_contract/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# ============================== POST the Bank Mandate Remove Contract Operation (POST) ================================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# ============================ DELETE the Bank Mandate Remove Contract Operation (DELETE) ==============================
# ============================== PATCH the Bank Mandate Remove Contract Operation (PATCH) ==============================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_remove_contract/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Bank Mandate Revoke Operation (GET) ====================================
# ========================== Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) ========================
# =================================== POST the Bank Mandate Revoke Operation (POST) ====================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Bank Mandate Revoke Operation (GET) ====================================
# ========================== Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) ========================
# ================================== DELETE the Bank Mandate Revoke Operation (DELETE) =================================
# =================================== PATCH the Bank Mandate Revoke Operation (PATCH) ==================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer_with_bank_mandate_revoke_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer_with_bank_mandate_revoke_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/bank_accounts/Replace5/bank_mandates/Replace6/operations/bank_mandate_revoke/Replace7/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the E Mail Addresses Collection (GET) =====================================
# =========================== Return the hypermedia of a E Mail Addresses Collection (OPTIONS) =========================
# ===================================== POST the E Mail Addresses Collection (POST) ====================================
e_mail_address_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/e_mail_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the E Mail Addresses Document (GET) =======================================
# =========================== Return the hypermedia of a E Mail Addresses Document (OPTIONS) ===========================
# ==================================== PATCH the E Mail Addresses Document (PATCH) =====================================
e_mail_address_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/e_mail_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Family Members Collection (GET) ======================================
# ============================ Return the hypermedia of a Family Members Collection (OPTIONS) ==========================
# ====================================== POST the Family Members Collection (POST) =====================================
family_member_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/family_members',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Family Members Document (GET) ========================================
# ============================ Return the hypermedia of a Family Members Document (OPTIONS) ============================
# ==================================== PATCH the Family Members Document (PATCH) =======================================
family_member_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/family_members/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Information Receipts Collection (GET) ===================================
# ========================= Return the hypermedia of a Information Receipts Collection (OPTIONS) =======================
# =================================== POST the Information Receipts Collection (POST) ==================================
information_receipt_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Information Receipts Document (GET) =====================================
# ========================= Return the hypermedia of a Information Receipts Document (OPTIONS) =========================
# ================================== PATCH the Information Receipts Document (PATCH) ===================================
information_receipt_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/information_receipts/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Transfer Save Controller (GET) ======================================
# ============================= Return the hypermedia of a Transfer Save Controller (OPTIONS) ==========================
# ======================================= POST the Transfer Save Controller (POST) =====================================
transfer_information_receipt_save_controller_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/information_receipts/Replace5/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Multiple Transfer Save Controller (GET) ===================================
# ======================= Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) =======================
# ================================ POST the Multiple Transfer Save Controller (POST) ===================================
multiple_transfer_information_receipt_save_controller_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Information Requests Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Requests Collection (OPTIONS) ========================
information_request_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/information_requests',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Information Requests Document (GET) =====================================
# ========================= Return the hypermedia of a Information Requests Document (OPTIONS) =========================
information_request_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/information_requests/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Launch View Aia Bridge resource (GET) ====================================
# ======================== Return the hypermedia of a Launch View Aia Bridge resource (OPTIONS) ========================
# ================================= POST the Launch View Aia Bridge resource (POST) ====================================
launch_view_aia_person_bridge_resource_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/launch_view_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Manual Tasks Collection (GET) ========================================
# ============================ Return the hypermedia of a Manual Tasks Collection (OPTIONS) ============================
# ====================================== POST the Manual Tasks Collection (POST) =======================================
manual_task_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/manual_tasks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Manual Tasks Document (GET) =========================================
# ============================= Return the hypermedia of a Manual Tasks Document (OPTIONS) =============================
# ====================================== PATCH the Manual Tasks Document (PATCH) =======================================
manual_task_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/manual_tasks/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_manual_task_save_controller_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/manual_tasks/Replace5/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Occupations Collection (GET) ========================================
# ============================= Return the hypermedia of a Occupations Collection (OPTIONS) ============================
# ======================================= POST the Occupations Collection (POST) =======================================
occupation_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Occupations Document (GET) =========================================
# ============================== Return the hypermedia of a Occupations Document (OPTIONS) =============================
# ======================================= PATCH the Occupations Document (PATCH) =======================================
occupation_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_occupation_save_controller_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_occupation_save_controller_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Create Membership Operation (GET) =====================================
# =========================== Return the hypermedia of a Create Membership Operation (OPTIONS) =========================
# ===================================== POST the Create Membership Operation (POST) ====================================
create_membership_operation_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/create_membership',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Create Membership Operation (GET) ======================================
# ========================== Return the hypermedia of a Create Membership Operation (OPTIONS) ==========================
# ================================== DELETE the Create Membership Operation (DELETE) ===================================
# =================================== PATCH the Create Membership Operation (PATCH) ====================================
create_membership_operation_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer_with_create_membership_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/create_membership/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ========================================= GET the Execute Save Controller (GET) ======================================
# ============================== Return the hypermedia of a Execute Save Controller (OPTIONS) ==========================
# ======================================== POST the Execute Save Controller (POST) =====================================
execute_create_membership_save_controller_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/create_membership/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_create_membership_save_controller_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer_with_create_membership_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/create_membership/Replace6/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_create_membership_save_controller_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/create_membership/Replace6/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =============================== GET the Generate Required Memberships Operation (GET) ================================
# ==================== Return the hypermedia of a Generate Required Memberships Operation (OPTIONS) ====================
# ============================== POST the Generate Required Memberships Operation (POST) ===============================
generate_required_memberships_operation_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/generate_required_memberships',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =============================== GET the Generate Required Memberships Operation (GET) ================================
# ==================== Return the hypermedia of a Generate Required Memberships Operation (OPTIONS) ====================
# ============================ DELETE the Generate Required Memberships Operation (DELETE) =============================
# ============================= PATCH the Generate Required Memberships Operation (PATCH) ==============================
generate_required_memberships_operation_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer_with_generate_required_memberships_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/generate_required_memberships/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_generate_required_memberships_save_controller_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/generate_required_memberships/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_generate_required_memberships_save_controller_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer_with_generate_required_memberships_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/generate_required_memberships/Replace6/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

#====================================== GET the Cancel Save Controller (GET) ===========================================
# ========================== Return the hypermedia of a Cancel Save Controller (OPTIONS) ===============================
# ==================================== POST the Cancel Save Controller (POST) ==========================================
cancel_generate_required_memberships_save_controller_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/generate_required_memberships/Replace6/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Unblock T P Rights Operation (GET) =======================================
# ======================== Return the hypermedia of a Unblock T P Rights Operation (OPTIONS) ===========================
# ================================== POST the Unblock T P Rights Operation (POST) ======================================
unblock_t_p_rights_operation_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/unblock_t_p_rights',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Unblock T P Rights Operation (GET) ========================================
# ======================= Return the hypermedia of a Unblock T P Rights Operation (OPTIONS) ============================
# =============================== DELETE the Unblock T P Rights Operation (DELETE) =====================================
# ================================ PATCH the Unblock T P Rights Operation (PATCH) ======================================
unblock_t_p_rights_operation_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer_with_unblock_tp_rights_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/unblock_t_p_rights/Replace6',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ===================================== GET the Execute Save Controller (GET) ==========================================
# ========================== Return the hypermedia of a Execute Save Controller (OPTIONS) ==============================
# ==================================== POST the Execute Save Controller (POST) =========================================
execute_unblock_t_p_rights_save_controller_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/unblock_t_p_rights/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Execute Save Controller (GET) ===========================================
# ========================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===============================
# ================================== POST the Execute Save Controller (POST) ===========================================
execute_unblock_t_p_rights_save_controller_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer_with_unblock_tp_rights_id = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/unblock_t_p_rights/Replace6/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_unblock_t_p_rights_save_controller_of_the_occupation_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/occupations/Replace5/operations/unblock_t_p_rights/Replace6/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Person Info Sheets Collection (GET) =====================================
# ========================= Return the hypermedia of a Person Info Sheets Collection (OPTIONS) =========================
person_info_sheet_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/person_info_sheets',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Person Info Sheets Document (GET) ========================================
# ======================== Return the hypermedia of a Person Info Sheets Document (OPTIONS) ============================
# ================================ PATCH the Person Info Sheets Document (PATCH) =======================================
person_info_sheet_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/person_info_sheets/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Phone Addresses Collection (GET) ========================================
# ========================= Return the hypermedia of a Phone Addresses Collection (OPTIONS) ============================
# ================================== POST the Phone Addresses Collection (POST) ========================================
phone_address_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/phone_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Phone Addresses Document (GET) ========================================
# =========================== Return the hypermedia of a Phone Addresses Document (OPTIONS) ============================
# =================================== PATCH the Phone Addresses Document (PATCH) =======================================
phone_address_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/phone_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# =================================== GET the Postal Addresses Collection (GET) ========================================
# ======================== Return the hypermedia of a Postal Addresses Collection (OPTIONS) ============================
# ================================= POST the Postal Addresses Collection (POST) ========================================
postal_address_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/postal_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Postal Addresses Document (GET) =========================================
# ========================= Return the hypermedia of a Postal Addresses Document (OPTIONS) =============================
# =============================== DELETE the Postal Addresses Document (DELETE) ========================================
# ================================= PATCH the Postal Addresses Document (PATCH) ========================================
postal_address_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/postal_addresses/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# =================================== GET the Social Security I Ds Collection (GET) ====================================
# ======================== Return the hypermedia of a Social Security I Ds Collection (OPTIONS) ========================
social_security_i_d_collection_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/social_security_i_ds',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Social Security I Ds Document (GET) =====================================
# ========================= Return the hypermedia of a Social Security I Ds Document (OPTIONS) =========================
social_security_i_d_document_of_the_person_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/persons/Replace4/social_security_i_ds/Replace5',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Product Components Collection (GET) =====================================
# ========================= Return the hypermedia of a Product Components Collection (OPTIONS) =========================
offer_product_component_collection_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/product_components',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Product Components Document (GET) ========================================
# ======================== Return the hypermedia of a Product Components Document (OPTIONS) ============================
# ================================= PATCH the Product Components Document (PATCH) ======================================
offer_product_component_document_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/product_components/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ================================== GET the Financial Options Collection (GET) ========================================
# ======================= Return the hypermedia of a Financial Options Collection (OPTIONS) ============================
# ================================= POST the Financial Options Collection (POST) =======================================
offer_financial_option_collection_of_the_offer_product_component_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/product_components/Replace4/financial_options',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Financial Options Document (GET) ========================================
# ========================= Return the hypermedia of a Financial Options Document (OPTIONS) ============================
# =============================== DELETE the Financial Options Document (DELETE) =======================================
# ================================= PATCH the Financial Options Document (PATCH) =======================================
offer_financial_option_document_of_the_offer_product_component_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/product_components/Replace4/financial_options/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# =========================================== GET the Funds Collection (GET) ===========================================
# ================================ Return the hypermedia of a Funds Collection (OPTIONS) ===============================
# ========================================= POST the Funds Collection (POST) ===========================================
offer_fund_collection_of_the_offer_product_component_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/product_components/Replace4/funds',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================================== GET the Funds Document (GET) =============================================
# ================================ Return the hypermedia of a Funds Document (OPTIONS) =================================
# ========================================= PATCH the Funds Document (PATCH) ===========================================
offer_fund_document_of_the_offer_product_component_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/product_components/Replace4/funds/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Property Equipments Collection (GET) ====================================
# ========================= Return the hypermedia of a Property Equipments Collection (OPTIONS) ========================
# ================================== POST the Property Equipments Collection (POST) ====================================
offer_risk_equipment_collection_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/property_equipments',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Property Equipments Document (GET) =====================================
# ========================== Return the hypermedia of a Property Equipments Document (OPTIONS) =========================
# ================================= DELETE the Property Equipments Document (DELETE) ===================================
# =================================== PATCH the Property Equipments Document (PATCH) ===================================
offer_risk_equipment_document_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/property_equipments/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ================================= GET the Property Recorded Claims Collection (GET) ==================================
# ====================== Return the hypermedia of a Property Recorded Claims Collection (OPTIONS) ======================
# ================================ POST the Property Recorded Claims Collection (POST) =================================
offer_property_recorded_claims_collection_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/property_recorded_claims',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Property Recorded Claims Document (GET) ==================================
# ======================== Return the hypermedia of a Property Recorded Claims Document (OPTIONS) ======================
# =============================== DELETE the Property Recorded Claims Document (DELETE) ================================
# ================================ PATCH the Property Recorded Claims Document (PATCH) =================================
offer_property_recorded_claims_document_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/property_recorded_claims/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ====================================== GET the Questionnaires Collection (GET) =======================================
# =========================== Return the hypermedia of a Questionnaires Collection (OPTIONS) ===========================
offer_questionnaire_collection_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/questionnaires',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Questionnaires Document (GET) ========================================
# ============================ Return the hypermedia of a Questionnaires Document (OPTIONS) ============================
offer_questionnaire_document_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/questionnaires/Replace4',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Question Answers Collection (GET) ======================================
# ========================== Return the hypermedia of a Question Answers Collection (OPTIONS) ==========================
offer_question_answer_collection_of_the_offer_questionnaire_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/questionnaires/Replace4/question_answers',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Question Answers Document (GET) =======================================
# =========================== Return the hypermedia of a Question Answers Document (OPTIONS) ===========================
# ==================================== PATCH the Question Answers Document (PATCH) =====================================
offer_question_answer_document_of_the_offer_questionnaire_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/questionnaires/Replace4/question_answers/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Validate Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Validate Save Controller (OPTIONS) ===========================
# ===================================== POST the Validate Save Controller (POST) =======================================
validate_offer_questionnaire_save_controller_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/questionnaires/Replace4/validate',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Tariff Adjustments Collection (GET) ====================================
# ========================== Return the hypermedia of a Tariff Adjustments Collection (OPTIONS) ========================
# ==================================== POST the Tariff Adjustments Collection (POST) ===================================
offer_premium_adjustment_collection_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/tariff_adjustments',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Tariff Adjustments Document (GET) ======================================
# ========================== Return the hypermedia of a Tariff Adjustments Document (OPTIONS) ==========================
# =================================== PATCH the Tariff Adjustments Document (PATCH) ====================================
offer_premium_adjustment_document_of_the_offer_risk_of_the_offer = {
    'url': 'Replace1/offers/Replace2/risks/Replace3/tariff_adjustments/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Save Save Controller (GET) ==========================================
# ============================= Return the hypermedia of a Save Save Controller (OPTIONS) ==============================
# ====================================== POST the Save Save Controller (POST) ==========================================
save_offer_save_controller = {
    'url': 'Replace1/offers/Replace2/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Scheduled Payments Collection (GET) ====================================
# ========================== Return the hypermedia of a Scheduled Payments Collection (OPTIONS) ========================
# =================================== POST the Scheduled Payments Collection (POST) ====================================
offer_scheduled_payment_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/scheduled_payments',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Scheduled Payments Document (GET) =====================================
# =========================== Return the hypermedia of a Scheduled Payments Document (OPTIONS) =========================
# =================================== PATCH the Scheduled Payments Document (PATCH) ====================================
offer_scheduled_payment_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/scheduled_payments/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# =============================== GET the Offer Operation Info Sheets Collection (GET) =================================
# ===================== Return the hypermedia of a Offer Operation Info Sheets Collection (OPTIONS) ====================
offer_operation_info_sheet_collection_of_the_offer_scheduled_payment_of_the_offer = {
    'url': 'Replace1/offers/Replace2/scheduled_payments/Replace3/offer_operation_info_sheets',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================= GET the Offer Operation Info Sheets Document (GET) =================================
# ====================== Return the hypermedia of a Offer Operation Info Sheets Document (OPTIONS) =====================
# ============================== PATCH the Offer Operation Info Sheets Document (PATCH) ================================
offer_operation_info_sheet_document_of_the_offer_scheduled_payment_of_the_offer = {
    'url': 'Replace1/offers/Replace2/scheduled_payments/Replace3/offer_operation_info_sheets/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# =================================== GET the Scheduled Surrenders Collection (GET) ====================================
# ======================== Return the hypermedia of a Scheduled Surrenders Collection (OPTIONS) ========================
# ================================== POST the Scheduled Surrenders Collection (POST) ===================================
offer_scheduled_surrender_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/scheduled_surrenders',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Scheduled Surrenders Document (GET) =====================================
# ========================= Return the hypermedia of a Scheduled Surrenders Document (OPTIONS) =========================
# ================================== PATCH the Scheduled Surrenders Document (PATCH) ===================================
offer_scheduled_surrender_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/scheduled_surrenders/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# =============================== GET the Offer Operation Info Sheets Collection (GET) =================================
# ==================== Return the hypermedia of a Offer Operation Info Sheets Collection (OPTIONS) =====================
offer_operation_info_sheet_collection_of_the_offer_scheduled_surrender_of_the_offer = {
    'url': 'Replace1/offers/Replace2/scheduled_surrenders/Replace3/offer_operation_info_sheets',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================= GET the Offer Operation Info Sheets Document (GET) =================================
# ====================== Return the hypermedia of a Offer Operation Info Sheets Document (OPTIONS) =====================
# ============================== PATCH the Offer Operation Info Sheets Document (PATCH) ================================
offer_operation_info_sheet_document_of_the_offer_scheduled_surrender_of_the_offer = {
    'url': 'Replace1/offers/Replace2/scheduled_surrenders/Replace3/offer_operation_info_sheets/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Tariff Adjustments Collection (GET) =====================================
# ========================= Return the hypermedia of a Tariff Adjustments Collection (OPTIONS) =========================
# =================================== POST the Tariff Adjustments Collection (POST) ====================================
offer_premium_adjustment_collection_of_the_offer = {
    'url': 'Replace1/offers/Replace2/tariff_adjustments',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Tariff Adjustments Document (GET) ======================================
# ========================== Return the hypermedia of a Tariff Adjustments Document (OPTIONS) ==========================
# =================================== PATCH the Tariff Adjustments Document (PATCH) ====================================
offer_premium_adjustment_document_of_the_offer = {
    'url': 'Replace1/offers/Replace2/tariff_adjustments/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ================================== GET the Tariff Calculation Save Controller (GET) ==================================
# ======================= Return the hypermedia of a Tariff Calculation Save Controller (OPTIONS) ======================
# ================================= POST the Tariff Calculation Save Controller (POST) =================================
tariff_calculation_offer_save_controller = {
    'url': 'Replace1/offers/Replace2/tariff_calculation',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Validate Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Validate Save Controller (OPTIONS) ===========================
# ===================================== POST the Validate Save Controller (POST) =======================================
validate_offer_save_controller = {
    'url': 'Replace1/offers/Replace2/validate',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}
