# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 08:34:24 2021

@author: bbalushev
"""

# ========================================== Get the activity collection (GET) =========================================
# ============================= Return the hypermedia of a Activities Collection (OPTIONS) =============================
activity_collection = {
    'url': 'Replace1/references_wm/activities',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Activities Document (GET) =========================================
# ============================== Return the hypermedia of a Activities Document (OPTIONS) ==============================
activities_document = {
    'url': 'Replace1/references_wm/activities/Replace2',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================== GET the Operations Collection (GET) =========================================
# ============================= Return the hypermedia of a Operations Collection (OPTIONS) =============================
operations_collection_of_the_activity = {
    'url': 'Replace1/references_wm/activities/Replace2/operations',
    'request_methods_list': ['GET', 'OPTIONS']
}

# =========================================== GET the Process Operation (GET) ==========================================
# =============================== Return the hypermedia of a Process Operation (OPTIONS) ===============================
# ========================================= POST the Process Operation (POST) ==========================================
process_activity_operation_of_the_activity = {
    'url': 'Replace1/references_wm/activities/Replace2/operations/process',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# =================================== GET the Process Operation with process id (GET) ==================================
# ======================= Return the hypermedia of a Process Operation with process id (OPTIONS) =======================
# ======================================= DELETE the Process Operation (DELETE) ========================================
# ======================================== PATCH the Process Operation (PATCH) =========================================
process_activity_operation_of_the_activity_with_process_id = {
    'url': 'Replace1/references_wm/activities/Replace2/operations/process/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ======================================= GET the Execute Save Controller (GET) ========================================
# ============================ Return the hypermedia of a Execute Save Controller (OPTIONS) ============================
# ====================================== POST the Execute Save Controller (POST) =======================================
execute_process_activity_save_controller_of_the_activity = {
    'url': 'Replace1/references_wm/activities/Replace2/operations/process/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ============================== GET the Execute Save Controller with process id (GET) =================================
# ===================== Return the hypermedia of Execute Save Controller with process id (OPTIONS) =====================
# ============================= POST the Execute Save Controller with process id (POST) ================================
execute_process_activity_save_controller_of_the_activity_with_process_id = {
    'url': 'Replace1/references_wm/activities/Replace2/operations/process/Replace3/execute',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Resume In Aia Bridge resource (GET) =====================================
# ========================= Return the hypermedia of a Resume In Aia Bridge resource (OPTIONS) =========================
# =================================== POST the Resume In Aia Bridge resource (POST) ====================================
resume_in_aia_activity_bridge_resource = {
    'url': 'Replace1/references_wm/activities/Replace2/resume_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}
