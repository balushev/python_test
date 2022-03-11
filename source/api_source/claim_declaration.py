# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 11:09:21 2022

@author: bbalushev
"""


# ==================================== GET the Claim Declarations Collection (GET) =====================================
# ========================= Return the hypermedia of a Claim Declarations Collection (OPTIONS) =========================
# ==================================  POST the Claim Declarations Collection (POST) ====================================
claim_declaration_collection = {
    'url': 'Replace1/claim_declarations',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Claim Declarations Document (GET) ======================================
# ========================== Return the hypermedia of a Claim Declarations Document (OPTIONS) ==========================
# ================================== DELETE the Claim Declarations Document (DELETE) ===================================
# ==================================== PATCH the Claim Declarations Document (PATCH) ===================================
claim_declaration_document = {
    'url': 'Replace1/claim_declarations/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ===================================  GET the Information Receipts Collection (GET) ===================================
# =========================Return the hypermedia of a Information Receipts Collection (OPTIONS) ========================
# ================================== POST the Information Receipts Collection (POST) ===================================
information_receipt_collection_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Information Receipts Document (GET) ======================================
# ======================== Return the hypermedia of a Information Receipts Document (OPTIONS) ==========================
# ================================= PATCH the Information Receipts Document (PATCH) ====================================
information_receipt_document_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/information_receipts/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# =========================== Return the hypermedia of a Transfer Save Controller (OPTIONS) ============================
# ====================================== POST the Transfer Save Controller (POST) ======================================
transfer_information_receipt_save_controller_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/information_receipts/Replace3/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Multiple Transfer Save Controller (GET) ===================================
# ======================= Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) =======================
# ================================= POST the Multiple Transfer Save Controller (POST) ==================================
multiple_transfer_information_receipt_save_controller_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Information Types Collection (GET) ======================================
# ========================= Return the hypermedia of a Information Types Collection (OPTIONS) ==========================
information_type_collection_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/information_types',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ===================================== GET the Information Types Document (GET) =======================================
# ========================== Return the hypermedia of a Information Types Document (OPTIONS) ===========================
information_type_document_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/information_types/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================ Return the hypermedia of a Operations Collection (OPTIONS) ==============================
operation_collection_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Transfer Operation (GET) ==========================================
# ============================== Return the hypermedia of a Transfer Operation (OPTIONS) ===============================
# ========================================= POST the Transfer Operation (POST) =========================================
transfer_claim_declaration_operation_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/operations/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================== GET the Transfer Operation (GET) ==========================================
# ============================== Return the hypermedia of a Transfer Operation (OPTIONS) ===============================
# ======================================= DELETE the Transfer Operation (DELETE) =======================================
# ======================================= PATCH the Transfer Operation (PATCH) =========================================
transfer_claim_declaration_operation_of_the_claim_declaration_with_transfer_id = {
    'url': 'Replace1/claim_declarations/Replace2/operations/transfer/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ======================================= POST the Execute Save Controller (POST) ======================================
execute_transfer_claim_declaration_save_controller_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/operations/transfer/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Execute Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ======================================= POST the Execute Save Controller (POST) ======================================
execute_transfer_claim_declaration_save_controller_of_the_claim_declaration_with_transfer_id = {
    'url': 'Replace1/claim_declarations/Replace2/operations/transfer/Replace3/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ======================================= POST the Cancel Save Controller (POST) =======================================
cancel_transfer_claim_declaration_save_controller_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/operations/transfer/Replace3/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Available Documents Collection (GET) ====================================
# ======================== Return the hypermedia of a Available Documents Collection (OPTIONS) =========================
# =================================== POST the Available Documents Collection (POST) ===================================
available_document_collection_of_the_transfer_claim_declaration_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/operations/transfer/Replace3/available_documents',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Available Documents Document (GET) =====================================
# ========================= Return the hypermedia of a Available Documents Document (OPTIONS) ==========================
# =================================== PATCH the Available Documents Document (PATCH) ===================================
available_document_document_of_the_transfer_claim_declaration_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/operations/transfer/Replace3/available_documents/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ===================================== GET the Output Documents Collection (GET) ======================================
# ========================= Return the hypermedia of a Output Documents Collection (OPTIONS) ===========================
# ==================================== POST the Output Documents Collection (POST) =====================================
output_document_collection_of_the_transfer_claim_declaration_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/operations/transfer/Replace3/output_documents',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Output Documents Document (GET) =======================================
# ========================== Return the hypermedia of a Output Documents Document (OPTIONS) ============================
# ==================================== PATCH the Output Documents Document (PATCH) =====================================
output_document_document_of_the_transfer_claim_declaration_of_the_claim_declaration = {
    'url': 'Replace1/claim_declarations/Replace2/operations/transfer/Replace3/output_documents/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}
