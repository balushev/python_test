# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:34:58 2022

@author: bbalushev
"""


# ========================================= GET the Persons Collection (GET) ===========================================
# ============================== Return the hypermedia of a Persons Collection (OPTIONS) ===============================
# ======================================= POST the Persons Collection (POST) ===========================================
person_collection = {
    'url': 'Replace1/persons',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Persons Document (GET) =============================================
# ============================== Return the hypermedia of a Persons Document (OPTIONS) =================================
# ======================================= PATCH the Persons Document (PATCH) ===========================================
person_document = {
    'url': 'Replace1/persons/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Save Save Controller (GET) ==========================================
# ============================= Return the hypermedia of a Save Save Controller (OPTIONS) ==============================
# ====================================== POST the Save Save Controller (POST) ==========================================
save_person_save_controller = {
    'url': 'Replace1/persons/Replace2/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_person_save_controller = {
    'url': 'Replace1/persons/Replace2/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Activities Collection (GET) =========================================
# ============================= Return the hypermedia of a Activities Collection (OPTIONS) =============================
activity_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/activities',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Activities Document (GET) ==============================================
# ========================== Return the hypermedia of a Activities Document (OPTIONS) ==================================
activity_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/activities/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Operations Collection (GET) ==========================================
# ============================ Return the hypermedia of a Operations Collection (OPTIONS) ==============================
operation_collection_of_the_activity_of_the_person = {
    'url': 'Replace1/persons/Replace2/activities/Replace3/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================= GET the Process Operation (GET) ============================================
# ============================== Return the hypermedia of a Process Operation (OPTIONS) ================================
# ======================================= POST the Process Operation (POST) ============================================
process_activity_operation_of_the_activity_of_the_person = {
    'url': 'Replace1/persons/Replace2/activities/Replace3/operations/process',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Process Operation (GET) ============================================
# ============================== Return the hypermedia of a Process Operation (OPTIONS) ================================
# ====================================== DELETE the Process Operation (DELETE) =========================================
# ======================================= PATCH the Process Operation (PATCH) ==========================================
process_activity_operation_of_the_activity_of_the_person_with_process_id = {
    'url': 'Replace1/persons/Replace2/activities/Replace3/operations/process/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_process_activity_save_controller_of_the_activity_of_the_person = {
    'url': 'Replace1/persons/Replace2/activities/Replace3/operations/process/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_process_activity_save_controller_of_the_activity_of_the_person_with_process_id = {
    'url': 'Replace1/persons/Replace2/activities/Replace3/operations/process/Replace4/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Resume In Aia Bridge resource (GET) =====================================
# ========================= Return the hypermedia of a Resume In Aia Bridge resource (OPTIONS) =========================
# ================================== POST the Resume In Aia Bridge resource (POST) =====================================
resume_in_aia_activity_bridge_resource_of_the_person = {
    'url': 'Replace1/persons/Replace2/activities/Replace3/resume_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Activity Definitions Collection (GET) ====================================
# ======================== Return the hypermedia of a Activity Definitions Collection (OPTIONS) ========================
activity_definition_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/activity_definitions',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Activity Definitions Document (GET) =====================================
# ========================= Return the hypermedia of a Activity Definitions Document (OPTIONS) =========================
activity_definition_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/activity_definitions/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================ GET the Launch Activity In Aia Bridge resource (GET) ================================
# ===================== Return the hypermedia of a Launch Activity In Aia Bridge resource (OPTIONS) ====================
# ============================== POST the Launch Activity In Aia Bridge resource (POST) ================================
launch_activity_in_aia_activity_definition_bridge_resource_of_the_person = {
    'url': 'Replace1/persons/Replace2/activity_definitions/Replace3/launch_activity_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Bank Accounts Collection (GET) ========================================
# =========================== Return the hypermedia of a Bank Accounts Collection (OPTIONS) ============================
# ==================================== POST the Bank Accounts Collection (POST) ========================================
bank_account_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Bank Accounts Document (GET) =========================================
# ============================ Return the hypermedia of a Bank Accounts Document (OPTIONS) =============================
# ===================================== PATCH the Bank Accounts Document (PATCH) =======================================
bank_account_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Bank Mandates Collection (GET) ========================================
# =========================== Return the hypermedia of a Bank Mandates Collection (OPTIONS) ============================
# ==================================== POST the Bank Mandates Collection (POST) ========================================
bank_mandate_collection_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Bank Mandates Document (GET) =========================================
# ============================ Return the hypermedia of a Bank Mandates Document (OPTIONS) =============================
# ===================================== PATCH the Bank Mandates Document (PATCH) =======================================
bank_mandate_document_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Save Save Controller (GET) ==========================================
# ============================= Return the hypermedia of a Save Save Controller (OPTIONS) ==============================
# ====================================== POST the Save Save Controller (POST) ==========================================
save_bank_mandate_save_controller_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_bank_mandate_save_controller_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Operations Collection (GET) ==========================================
# ============================ Return the hypermedia of a Operations Collection (OPTIONS) ==============================
operation_collection_of_the_bank_mandate_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================== GET the Bank Mandate Add Contract Operation (GET) =================================
# ======================= Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) =====================
# ================================ POST the Bank Mandate Add Contract Operation (POST) =================================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_add_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================= GET the Bank Mandate Add Contract Operation (GET) ==================================
# ====================== Return the hypermedia of a Bank Mandate Add Contract Operation (OPTIONS) ======================
# ============================== DELETE the Bank Mandate Add Contract Operation (DELETE) ===============================
# =============================== PATCH the Bank Mandate Add Contract Operation (PATCH) ================================
bank_mandate_add_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_add_contract/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_add_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_with_bank_mandate_add_contract_id = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_add_contract/Replace5/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_bank_mandate_add_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_add_contract/Replace5/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# ============================== POST the Bank Mandate Remove Contract Operation (POST) ================================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_remove_contract',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Bank Mandate Remove Contract Operation (GET) ================================
# ===================== Return the hypermedia of a Bank Mandate Remove Contract Operation (OPTIONS) ====================
# ============================ DELETE the Bank Mandate Remove Contract Operation (DELETE) ==============================
# ============================== PATCH the Bank Mandate Remove Contract Operation (PATCH) ==============================
bank_mandate_remove_contract_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_remove_contract/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_remove_contract/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_with_bank_mandate_remove_contract_id = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_remove_contract/Replace5/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_bank_mandate_remove_contract_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_remove_contract/Replace5/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Bank Mandate Revoke Operation (GET) =====================================
# ========================= Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) =========================
# ================================== POST the Bank Mandate Revoke Operation (POST) =====================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_revoke',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Bank Mandate Revoke Operation (GET) =====================================
# ========================= Return the hypermedia of a Bank Mandate Revoke Operation (OPTIONS) =========================
# ================================= DELETE the Bank Mandate Revoke Operation (DELETE) ==================================
# ================================== PATCH the Bank Mandate Revoke Operation (PATCH) ===================================
bank_mandate_revoke_operation_of_the_bank_mandate_of_the_bank_account_of_the_person_with_bank_mandate_revoke_id = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_revoke/Replace5',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_revoke/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Execute Save Controller (GET) =========================================
# =========================== Return the hypermedia of a Execute Save Controller (OPTIONS) =============================
# ==================================== POST the Execute Save Controller (POST) =========================================
execute_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person_with_bank_mandate_revoke_id = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_revoke/Replace5/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_bank_mandate_revoke_save_controller_of_the_bank_mandate_of_the_bank_account_of_the_person = {
    'url': 'Replace1/persons/Replace2/bank_accounts/Replace3/bank_mandates/Replace4/operations/bank_mandate_revoke/Replace5/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the E Mail Addresses Collection (GET) =====================================
# =========================== Return the hypermedia of a E Mail Addresses Collection (OPTIONS) =========================
# ==================================== POST the E Mail Addresses Collection (POST) =====================================
e_mail_address_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/e_mail_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the E Mail Addresses Document (GET) =======================================
# =========================== Return the hypermedia of a E Mail Addresses Document (OPTIONS) ===========================
# ==================================== PATCH the E Mail Addresses Document (PATCH) =====================================
e_mail_address_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/e_mail_addresses/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Family Members Collection (GET) =======================================
# =========================== Return the hypermedia of a Family Members Collection (OPTIONS) ===========================
# ==================================== POST the Family Members Collection (POST) =======================================
family_member_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/family_members',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Family Members Document(GET) =========================================
# ============================ Return the hypermedia of a Family Members Document (OPTIONS) ============================
# ===================================== PATCH the Family Members Document (PATCH) ======================================
family_member_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/family_members/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# =================================== GET the Information Receipts Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Receipts Collection (OPTIONS) ========================
# ================================= POST the Information Receipts Collection (POST) ====================================
information_receipt_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}


# ==================================== GET the Information Receipts Document (GET) =====================================
# ========================= Return the hypermedia of a Information Receipts Document (OPTIONS) =========================
# ================================== PATCH the Information Receipts Document (PATCH) ===================================
information_receipt_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/information_receipts/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_information_receipt_save_controller_of_the_person = {
    'url': 'Replace1/persons/Replace2/information_receipts/Replace3/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Multiple Transfer Save Controller (GET) ==================================
# ======================== Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) ======================
# ================================= POST the Multiple Transfer Save Controller (POST) ==================================
multiple_transfer_information_receipt_save_controller_of_the_person = {
    'url': 'Replace1/persons/Replace2/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Information Requests Collection (GET) ====================================
# ======================== Return the hypermedia of a Information Requests Collection (OPTIONS) ========================
information_request_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/information_requests',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Information Requests Document (GET) =====================================
# ========================= Return the hypermedia of a Information Requests Document (OPTIONS) =========================
information_request_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/information_requests/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =================================== GET the Launch View Aia Bridge resource (GET) ====================================
# ======================== Return the hypermedia of a Launch View Aia Bridge resource (OPTIONS) ========================
# ================================= POST the Launch View Aia Bridge resource (POST) ====================================
launch_view_aia_person_bridge_resource = {
    'url': 'Replace1/persons/Replace2/launch_view_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Manual Tasks Collection (GET) =========================================
# =========================== Return the hypermedia of a Manual Tasks Collection (OPTIONS) =============================
# ==================================== POST the Manual Tasks Collection (POST) =========================================
manual_task_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/manual_tasks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Manual Tasks Document (GET) ==========================================
# ============================ Return the hypermedia of a Manual Tasks Document (OPTIONS) ==============================
# ===================================== PATCH the Manual Tasks Document (PATCH) ========================================
manual_task_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/manual_tasks/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Transfer Save Controller (GET) ========================================
# =========================== Return the hypermedia of a Transfer Save Controller (OPTIONS) ============================
# ==================================== POST the Transfer Save Controller (POST) ========================================
transfer_manual_task_save_controller_of_the_person = {
    'url': 'Replace1/persons/Replace2/manual_tasks/Replace3/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Occupations Collection (GET) =========================================
# ============================ Return the hypermedia of a Occupations Collection (OPTIONS) =============================
# ===================================== POST the Occupations Collection (POST) =========================================
occupation_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Occupations Document (GET) ===========================================
# ============================ Return the hypermedia of a Occupations Document (OPTIONS) ===============================
# ===================================== PATCH the Occupations Document (PATCH) =========================================
occupation_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Save Save Controller (GET) ==========================================
# ============================= Return the hypermedia of a Save Save Controller (OPTIONS) ==============================
# ====================================== POST the Save Save Controller (POST) ==========================================
save_occupation_save_controller_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_occupation_save_controller_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Operations Collection (GET) ==========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operation_collection_of_the_occupation_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Create Membership Operation (GET) ======================================
# ========================== Return the hypermedia of a Create Membership Operation (OPTIONS) ==========================
# =================================== POST the Create Membership Operation (POST) ======================================
create_membership_operation_of_the_occupation_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/create_membership',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Create Membership Operation (GET) ======================================
# ========================== Return the hypermedia of a Create Membership Operation (OPTIONS) ==========================
# ================================= DELETE the Create Membership Operation (DELETE) ====================================
# =================================== PATCH the Create Membership Operation (PATCH) ====================================
create_membership_operation_of_the_occupation_of_the_person_with_create_membership_id = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/create_membership/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ====================================== GET the Execute Save Controller (GET) =========================================
# =========================== Return the hypermedia of a Execute Save Controller (OPTIONS) =============================
# ==================================== POST the Execute Save Controller (POST) =========================================
execute_create_membership_save_controller_of_the_occupation_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/create_membership/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_create_membership_save_controller_of_the_occupation_of_the_person_with_create_membership_id = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/create_membership/Replace4/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_create_membership_save_controller_of_the_occupation_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/create_membership/Replace4/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Generate Required Memberships Operation (GET) ===============================
# ===================== Return the hypermedia of a Generate Required Memberships Operation (OPTIONS) ===================
# ============================== POST the Generate Required Memberships Operation (POST) ===============================
generate_required_memberships_operation_of_the_occupation_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/generate_required_memberships',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================ GET the Generate Required Memberships Operation (GET) ===============================
# ===================== Return the hypermedia of a Generate Required Memberships Operation (OPTIONS) ===================
# =========================== DELETE the Generate Required Memberships Operation (DELETE) ==============================
# ============================= PATCH the Generate Required Memberships Operation (PATCH) ==============================
generate_required_memberships_operation_of_the_occupation_of_the_person_with_generate_required_memberships_id = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/generate_required_memberships/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_generate_required_memberships_save_controller_of_the_occupation_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/generate_required_memberships/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Execute Save Controller (GET) =========================================
# =========================== Return the hypermedia of a Execute Save Controller (OPTIONS) =============================
# ==================================== POST the Execute Save Controller (POST) =========================================
execute_generate_required_memberships_save_controller_of_the_occupation_of_the_person_with_generate_required_memberships_id = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/generate_required_memberships/Replace4/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ===================================== POST the Cancel Save Controller (POST) =========================================
cancel_generate_required_memberships_save_controller_of_the_occupation_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/generate_required_memberships/Replace4/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Unblock T P Rights Operation (GET) =====================================
# ========================== Return the hypermedia of a Unblock T P Rights Operation (OPTIONS) =========================
# =================================== POST the Unblock T P Rights Operation (POST) =====================================
unblock_t_p_rights_operation_of_the_occupation_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/unblock_t_p_rights',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Unblock T P Rights Operation (GET) ======================================
# ========================= Return the hypermedia of a Unblock T P Rights Operation (OPTIONS) ==========================
# ================================ DELETE the Unblock T P Rights Operation (DELETE) ====================================
# ================================= PATCH the Unblock T P Rights Operation (PATCH) =====================================
unblock_t_p_rights_operation_of_the_occupation_of_the_person_with_unblock_tp_rights_id = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/unblock_t_p_rights/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ===================================== POST the Execute Save Controller (POST) ========================================
execute_unblock_t_p_rights_save_controller_of_the_occupation_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/unblock_t_p_rights/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Execute Save Controller (GET) =========================================
# =========================== Return the hypermedia of a Execute Save Controller (OPTIONS) =============================
# ==================================== POST the Execute Save Controller (POST) =========================================
execute_unblock_t_p_rights_save_controller_of_the_occupation_of_the_person_with_unblock_tp_rights_id = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/unblock_t_p_rights/Replace4/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_unblock_t_p_rights_save_controller_of_the_occupation_of_the_person = {
    'url': 'Replace1/persons/Replace2/occupations/Replace3/operations/unblock_t_p_rights/Replace4/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Person Info Sheets Collection (GET) =====================================
# ========================= Return the hypermedia of a Person Info Sheets Collection (OPTIONS) =========================
person_info_sheet_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/person_info_sheets',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Person Info Sheets Document (GET) ======================================
# ========================== Return the hypermedia of a Person Info Sheets Document (OPTIONS) ==========================
# =================================== PATCH the Person Info Sheets Document (PATCH) ====================================
person_info_sheet_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/person_info_sheets/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Phone Addresses Collection (GET) ======================================
# =========================== Return the hypermedia of a Phone Addresses Collection (OPTIONS) ==========================
# ==================================== POST the Phone Addresses Collection (POST) ======================================
phone_address_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/phone_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Phone Addresses Document (GET) ========================================
# =========================== Return the hypermedia of a Phone Addresses Document (OPTIONS) ============================
# ==================================== PATCH the Phone Addresses Document (PATCH) ======================================
phone_address_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/phone_addresses/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Postal Addresses Collection (GET) ======================================
# =========================== Return the hypermedia of a Postal Addresses Collection (OPTIONS) =========================
# ==================================== POST the Postal Addresses Collection (POST) =====================================
postal_address_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/postal_addresses',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Postal Addresses Document (GET) =======================================
# =========================== Return the hypermedia of a Postal Addresses Document (OPTIONS) ===========================
# =================================== DELETE the Postal Addresses Document (DELETE) ====================================
# ==================================== PATCH the Postal Addresses Document (PATCH) =====================================
postal_address_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/postal_addresses/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# =================================== GET the Social Security I Ds Collection (GET) ====================================
# ======================== Return the hypermedia of a Social Security I Ds Collection (OPTIONS) ========================
social_security_i_d_collection_of_the_person = {
    'url': 'Replace1/persons/Replace2/social_security_i_ds',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Social Security I Ds Document (GET) =====================================
# ========================= Return the hypermedia of a Social Security I Ds Document (OPTIONS) =========================
social_security_i_d_document_of_the_person = {
    'url': 'Replace1/persons/Replace2/social_security_i_ds/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}
