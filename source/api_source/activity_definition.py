# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:03:23 2021

@author: bbalushev
"""

# =================================== GET the Activity Definitions Collection (GET) ====================================
# ========================= Return the hypermedia of Activity Definitions Collection (OPTIONS) =========================
activity_definition_collection = {
    'url': 'Replace1/references_wm/activity_definitions',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ==================================== GET the Activity Definitions Document (GET) =====================================
# ========================== Return the hypermedia of Activity Definitions Document (OPTIONS) ==========================
activity_definition_document = {
    'url': 'Replace1/references_wm/activity_definitions/Replace2',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ============================== GET the Launch Activity In Aia Bridge resource (GET) ==================================
# ==================== Return the hypermedia of a Launch Activity In Aia Bridge resource (OPTIONS) =====================
# ============================== POST the Launch Activity In Aia Bridge resource (POST) ================================
launch_activity_in_aia_activity_definition_bridge_resource = {
    'url': 'Replace1/references_wm/activity_definitions/Replace2/launch_activity_in_aia',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}
