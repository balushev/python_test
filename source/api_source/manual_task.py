# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 12:30:58 2022

@author: bbalushev
"""


# ======================================= GET the Manual Tasks Collection (GET) ========================================
# ============================ Return the hypermedia of a Manual Tasks Collection (OPTIONS) ============================
# ===================================== POST the Manual Tasks Collection (POST) ========================================
manual_task_collection = {
    'url': 'Replace1/references_wm/manual_tasks',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================= GET the Manual Tasks Document (GET) ========================================
# ============================== Return the hypermedia of a Manual Tasks Document (OPTIONS) ============================
# ======================================== PATCH the Manual Tasks Document (PATCH) =====================================
manual_task_document = {
    'url': 'Replace1/references_wm/manual_tasks/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================= GET the Transfer Save Controller (GET) =======================================
# ============================ Return the hypermedia of a Transfer Save Controller (OPTIONS) ===========================
# ===================================== POST the Transfer Save Controller (POST) =======================================
transfer_manual_task_save_controller = {
    'url': 'Replace1/references_wm/manual_tasks/Replace2/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}
