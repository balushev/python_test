# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 13:35:47 2022

@author: bbalushev
"""


# ========================================= GET the Money Ins Collection (GET) =========================================
# ============================== Return the hypermedia of a Money Ins Collection (OPTIONS) =============================
# ======================================== POST the Money Ins Collection (POST) ========================================
money_in_collection = {
    'url': 'Replace1/financials/money_ins',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Money Ins Document (GET) ===========================================
# ============================== Return the hypermedia of a Money Ins Document (OPTIONS) ===============================
# ===================================== DELETE the Money Ins Document (DELETE) =========================================
# ====================================== PATCH the Money Ins Document (PATCH) ==========================================
money_in_document = {
    'url': 'Replace1/financials/money_ins/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_money_in_save_controller = {
    'url': 'Replace1/financials/money_ins/Replace2/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Cancel Save Controller (GET) ========================================
# ============================= Return the hypermedia of a Cancel Save Controller (OPTIONS) ============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_money_in_save_controller = {
    'url': 'Replace1/financials/money_ins/Replace2/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}
