# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 11:15:44 2022

@author: bbalushev
"""


# =================================== GET the Information Receipts Collection (GET) ====================================
# ========================= Return the hypermedia of a Information Receipts Collection (OPTIONS) =======================
# ================================== POST the Information Receipts Collection (POST) ===================================
information_receipt_collection = {
    'url': 'Replace1/references_wm/information_receipts',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Information Receipts Document (GET) =====================================
# ========================= Return the hypermedia of a Information Receipts Document (OPTIONS) =========================
# ================================== PATCH the Information Receipts Document (PATCH) ===================================
information_receipt_document = {
    'url': 'Replace1/references_wm/information_receipts/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ====================================== GET the Transfer Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_information_receipt_save_controller = {
    'url': 'Replace1/references_wm/information_receipts/Replace2/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================== GET the Multiple Transfer Save Controller (GET) ===================================
# ======================= Return the hypermedia of a Multiple Transfer Save Controller (OPTIONS) =======================
# ================================= POST the Multiple Transfer Save Controller (POST) ==================================
multiple_transfer_information_receipt_save_controller = {
    'url': 'Replace1/references_wm/information_receipts/multiple_transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}
