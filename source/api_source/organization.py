# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 10:59:29 2022

@author: bbalushev
"""


# ======================================= GET the Organizations Collection (GET) =======================================
# ============================ Return the hypermedia of a Organizations Collection (OPTIONS) ===========================
# ====================================== POST the Organizations Collection (POST) ======================================
organization_collection = {
    'url': 'Replace1/organizations',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Organizations Document (GET) ========================================
# ============================= Return the hypermedia of a Organizations Document (OPTIONS) ============================
# ====================================== PATCH the Organizations Document (PATCH) ======================================
organization_document = {
    'url': 'Replace1/organizations/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_organization_save_controller = {
    'url': 'Replace1/organizations/Replace2/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_organization_save_controller = {
    'url': 'Replace1/organizations/Replace2/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Activities Collection (GET) =========================================
# ============================= Return the hypermedia of a Activities Collection (OPTIONS) =============================
activity_collection_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/activities',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Activities Document (GET) ==========================================
# ============================== Return the hypermedia of a Activities Document (OPTIONS) ==============================
activity_document_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/activities/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_activity_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/activities/Replace3/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Process Operation (GET) ===========================================
# =============================== Return the hypermedia of a Process Operation (OPTIONS) ===============================
# ========================================= POST the Process Operation (POST) ==========================================
process_activity_operation_of_the_activity_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/activities/Replace3/operations/process',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================== GET the Process Operation (GET) ===========================================
# =============================== Return the hypermedia of a Process Operation (OPTIONS) ===============================
# ======================================= DELETE the Process Operation (DELETE) ========================================
# ======================================== PATCH the Process Operation (PATCH) =========================================
process_activity_operation_of_the_activity_of_the_organization_with_process_id = {
    'url': 'Replace1/organizations/Replace2/activities/Replace3/operations/process/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_process_activity_save_controller_of_the_activity_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/activities/Replace3/operations/process/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_process_activity_save_controller_of_the_activity_of_the_organization_with_process_id = {
    'url': 'Replace1/organizations/Replace2/activities/Replace3/operations/process/Replace4/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Resume In Aia Bridge resource (GET) ====================================
# ========================== Return the hypermedia of a Resume In Aia Bridge resource (OPTIONS) ========================
# =================================== POST the Resume In Aia Bridge resource (POST) ====================================
resume_in_aia_activity_bridge_resource_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/activities/Replace3/resume_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Activity Definitions Collection (GET) ====================================
# ======================== Return the hypermedia of a Activity Definitions Collection (OPTIONS) ========================
activity_definition_collection_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/activity_definitions',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Activity Definitions Document (GET) ===================================
# =========================== Return the hypermedia of a Activity Definitions Document (OPTIONS) =======================
activity_definition_document_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/activity_definitions/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Launch Activity In Aia Bridge resource (GET) =============================
# ======================== Return the hypermedia of a Launch Activity In Aia Bridge resource (OPTIONS) =================
# ================================= POST the Launch Activity In Aia Bridge resource (POST) =============================
launch_activity_in_aia_activity_definition_bridge_resource_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/activity_definitions/Replace3/launch_activity_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Bank Accounts Collection (GET) =======================================
# ============================ Return the hypermedia of a Bank Accounts Collection (OPTIONS) ===========================
# ===================================== POST the Bank Accounts Collection (POST) =======================================
bank_account_collection_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Bank Accounts Document (GET) ========================================
# ============================= Return the hypermedia of a Bank Accounts Document (OPTIONS) ============================
# ===================================== PATCH the Bank Accounts Document (PATCH) =======================================
bank_account_document_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Bank Mandates Collection (GET) =======================================
# ============================ Return the hypermedia of a Bank Mandates Collection (OPTIONS) ===========================
# ===================================== POST the Bank Mandates Collection (POST) =======================================
bank_mandate_collection_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Bank Mandates Document (GET) ========================================
# ============================= Return the hypermedia of a Bank Mandates Document (OPTIONS) ============================
# ===================================== PATCH the Bank Mandates Document (PATCH) =======================================
bank_mandate_document_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================= POST the Save Save Controller (POST) =========================================
save_bank_mandate_save_controller_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_bank_mandate_save_controller_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_bank_mandate_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Bank Mandate Add Contract Operation (GET) ===============================
# ========================= Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) ===================
# =================================== POST the Bank Mandate Add Contract Operation (POST) ==============================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_add_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Bank Mandate Add Contract Operation (GET) ===============================
# ========================= Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) ===================
# ================================ DELETE the Bank Mandate Add Contract Operation (DELETE) =============================
# ================================= PATCH the Bank Mandate Add Contract Operation (PATCH) ==============================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_add_contract/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_add_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_add_contract/Replace5/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_add_contract/Replace5/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# =============================== POST the Bank Mandate Remove Contract Operation (POST) ===============================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_remove_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# ============================ DELETE the Bank Mandate Remove Contract Operation (DELETE) ==============================
# ============================= PATCH the Bank Mandate Remove Contract Operation (PATCH) ===============================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_remove_contract/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_remove_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_remove_contract/Replace5/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_remove_contract/Replace5/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Bank Mandate Revoke Operation (GET) =====================================
# ========================= Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) =========================
# =================================== POST the Bank Mandate Revoke Operation (POST) ====================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_revoke',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =========================v========= GET the Bank Mandate Revoke Operation (GET) ======================================
# ========================== Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) ========================
# ================================= DELETE the Bank Mandate Revoke Operation (DELETE) ==================================
# ================================== PATCH the Bank Mandate Revoke Operation (PATCH) ===================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_organization_with_bank_mandate_revoke_id = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_revoke/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_revoke/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================= Return the hypermedia of a Execute Save Controller (OPTIONS) ===========================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization_with_bank_mandate_revoke_id = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_revoke/Replace5/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_revoke/Replace5/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the E Mail Addresses Collection (GET) ======================================
# ========================== Return the hypermedia of a E Mail Addresses Collection (OPTIONS) ==========================
# ==================================== POST the E Mail Addresses Collection (POST) =====================================
e_mail_address_collection_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/e_mail_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the E Mail Addresses Document (GET) =======================================
# =========================== Return the hypermedia of a E Mail Addresses Document (OPTIONS) ===========================
# ==================================== PATCH the E Mail Addresses Document (PATCH) =====================================
e_mail_address_document_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/e_mail_addresses/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Information Receipts Collection (GET) =================================
# =========================== Return the hypermedia of a Information Receipts Collection (OPTIONS) =====================
# ===================================== POST the Information Receipts Collection (POST) ================================
information_receipt_collection_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Information Receipts Document (GET) ====================================
# ========================== Return the hypermedia of a Information Receipts Document (OPTIONS) ========================
# ================================== PATCH the Information Receipts Document (PATCH) ===================================
information_receipt_document_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/information_receipts/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Transfer Save Controller (GET) =========================================
# ========================== Return the hypermedia of a Transfer Save Controller (OPTIONS) =============================
# =================================== POST the Transfer Save Controller (POST) =========================================
transfer_information_receipt_save_controller_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/information_receipts/Replace3/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Multiple Transfer Save Controller (GET) ================================
# ========================== Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) ====================
# ==================================== POST the Multiple Transfer Save Controller (POST) ===============================
multiple_transfer_information_receipt_save_controller_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Information Requests Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Requests Collection (OPTIONS) ========================
information_request_collection_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/information_requests',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Information Requests Document (GET) =====================================
# ========================= Return the hypermedia of a Information Requests Document (OPTIONS) =========================
information_request_document_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/information_requests/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Launch View Aia Bridge resource (GET) ====================================
# ======================== Return the hypermedia of a Launch View Aia Bridge resource (OPTIONS) ========================
# ================================== POST the Launch View Aia Bridge resource (POST) ===================================
launch_view_aia_organization_bridge_resource = {
    'url': 'Replace1/organizations/Replace2/launch_view_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Manual Tasks Collection (GET) ==========================================
# ========================== Return the hypermedia of a Manual Tasks Collection (OPTIONS) ==============================
# ==================================== POST the Manual Tasks Collection (POST) =========================================
manual_task_collection_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/manual_tasks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Manual Tasks Document (GET) ===========================================
# =========================== Return the hypermedia of a Manual Tasks Document (OPTIONS) ===============================
# =================================== PATCH the Manual Tasks Document (PATCH) ==========================================
manual_task_document_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/manual_tasks/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ==================================== GET the Transfer Save Controller (GET) ==========================================
# ========================= Return the hypermedia of a Transfer Save Controller (OPTIONS) ==============================
# =================================== POST the Transfer Save Controller (POST) =========================================
transfer_manual_task_save_controller_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/manual_tasks/Replace3/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================= GET the Organization Info Sheets Collection (GET) ==================================
# ====================== Return the hypermedia of a Organization Info Sheets Collection (OPTIONS) ======================
organization_info_sheet_collection_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/organization_info_sheets',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Organization Info Sheets Document (GET) ==================================
# ======================== Return the hypermedia of a Organization Info Sheets Document (OPTIONS) ======================
# ================================ PATCH the Organization Info Sheets Document (PATCH) =================================
organization_info_sheet_document_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/organization_info_sheets/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Pay Points Collection (GET) =========================================
# ============================= Return the hypermedia of a Pay Points Collection (OPTIONS) =============================
pay_point_collection_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/pay_points',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Pay Points Document (GET) ==========================================
# ============================== Return the hypermedia of a Pay Points Document (OPTIONS) ==============================
pay_point_document_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/pay_points/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Phone Addresses Collection (GET) ======================================
# =========================== Return the hypermedia of a Phone Addresses Collection (OPTIONS) ==========================
# ===================================== POST the Phone Addresses Collection (POST) =====================================
phone_address_collection_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/phone_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Phone Addresses Document (GET) =======================================
# ============================ Return the hypermedia of a Phone Addresses Document (OPTIONS) ===========================
# ==================================== PATCH the Phone Addresses Document (PATCH) ======================================
phone_address_document_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/phone_addresses/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Postal Addresses Collection (GET) ======================================
# ========================== Return the hypermedia of a Postal Addresses Collection (OPTIONS) ==========================
# ==================================== POST the Postal Addresses Collection (POST) =====================================
postal_address_collection_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/postal_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Postal Addresses Document (GET) ======================================
# ============================ Return the hypermedia of a Postal Addresses Document (OPTIONS) ==========================
# =================================== DELETE the Postal Addresses Document (DELETE) ====================================
# ==================================== PATCH the Postal Addresses Document (PATCH) =====================================
postal_address_document_of_the_organization = {
    'url': 'Replace1/organizations/Replace2/postal_addresses/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}
