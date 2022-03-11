# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:19:32 2022

@author: bbalushev
"""


# ========================================== GET the Notes Collection (GET) ============================================
# =============================== Return the hypermedia of a Notes Collection (OPTIONS) ================================
# ========================================= POST the Notes Collection (POST) ===========================================
note_collection = {
    'url': 'Replace1/references_wm/notes',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ========================================== GET the Notes Document (GET) ==============================================
# =============================== Return the hypermedia of a Notes Document (OPTIONS) ==================================
# ====================================== DELETE the Notes Document (DELETE) ============================================
# ======================================= PATCH the Notes Document (PATCH) =============================================
note_document = {
    'url': 'Replace1/references_wm/notes/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ====================================== GET the Transfer Save Controller (GET) ========================================
# =========================== Return the hypermedia of a Transfer Save Controller (OPTIONS) ============================
# ==================================== POST the Transfer Save Controller (POST) ========================================
transfer_note_save_controller = {
    'url': 'Replace1/references_wm/notes/Replace2/transfer',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}
