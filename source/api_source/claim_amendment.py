# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:18:21 2022

@author: bbalushev
"""


# =================================== GET the Claim Amendments Collection (GET) ====================================
# ======================== Return the hypermedia of a Claim Amendments Collection (OPTIONS) ========================
# ================================== POST the Claim Amendments Collection (POST) ===================================
claim_amendment_collection = {
    'url': 'Replace1/claim_amendments',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Claim Amendments Document (GET) =====================================
# ========================= Return the hypermedia of a Claim Amendments Document (OPTIONS) =========================
# ================================= DELETE the Claim Amendments Document (DELETE) ==================================
# =================================== PATCH the Claim Amendments Document (PATCH) ==================================
claim_amendment_document = {
    'url': 'Replace1/claim_amendments/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ====================================== GET the Operations Collection (GET) =======================================
# =========================== Return the hypermedia of a Operations Collection (OPTIONS) ===========================
operation_collection_of_the_claim_amendment = {
    'url': 'Replace1/claim_amendments/Replace2/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Transfer Operation (GET) =========================================
# ============================ Return the hypermedia of a Transfer Operation (OPTIONS) =============================
# ====================================== POST the Transfer Operation (POST) ========================================
transfer_claim_amendment_operation_of_the_claim_amendment = {
    'url': 'Replace1/claim_amendments/Replace2/operations/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Transfer Operation (GET) ========================================
# ============================ Return the hypermedia of a Transfer Operation (OPTIONS) =============================
# ===================================== DELETE the Transfer Operation (DELETE) =====================================
# ====================================== PATCH the Transfer Operation (PATCH) ======================================
transfer_claim_amendment_operation_of_the_claim_amendment_with_transfer_id = {
    'url': 'Replace1/claim_amendments/Replace2/operations/transfer/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ===================================== GET the Execute Save Controller (GET) ======================================
# ========================== Return the hypermedia of a Execute Save Controller (OPTIONS) ==========================
# ==================================== POST the Execute Save Controller (POST) =====================================
execute_transfer_claim_amendment_save_controller_of_the_claim_amendment = {
    'url': 'Replace1/claim_amendments/Replace2/operations/transfer/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ===================================== GET the Execute Save Controller (GET) ======================================
# ========================== Return the hypermedia of a Execute Save Controller (OPTIONS) ==========================
# ==================================== POST the Execute Save Controller (POST) =====================================
execute_transfer_claim_amendment_save_controller_of_the_claim_amendment_with_transfer_id = {
    'url': 'Replace1/claim_amendments/Replace2/operations/transfer/Replace3/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ====================================== GET the Cancel Save Controller (GET) ======================================
# ========================== Return the hypermedia of a Cancel Save Controller (OPTIONS) ===========================
# ===================================== POST the Cancel Save Controller (POST) =====================================
cancel_transfer_claim_amendment_save_controller_of_the_claim_amendment = {
    'url': 'Replace1/claim_amendments/Replace2/operations/transfer/Replace3/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}
