# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 13:25:50 2022

@author: bbalushev
"""


# ======================================== GET the Memberships Collection (GET) ========================================
# ============================= Return the hypermedia of a Memberships Collection (OPTIONS) ============================
# ====================================== POST the Memberships Collection (POST) ========================================
membership_collection = {
    'url': 'membership_collection',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Memberships Document (GET) ==========================================
# ============================= Return the hypermedia of a Memberships Document (OPTIONS) ==============================
# ====================================== PATCH the Memberships Document (PATCH) ========================================
membership_document = {
    'url': 'Replace1/memberships/Replace2',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Save Save Controller (GET) =========================================
# ============================== Return the hypermedia of a Save Save Controller (OPTIONS) =============================
# ======================================== POST the Save Save Controller (POST) ========================================
save_membership_save_controller = {
    'url': 'Replace1/memberships/Replace2/save',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================= GET the Cancel Save Controller (GET) =========================================
# ============================ Return the hypermedia of a Cancel Save Controller (OPTIONS) =============================
# ====================================== POST the Cancel Save Controller (POST) ========================================
cancel_membership_save_controller = {
    'url': 'Replace1/memberships/Replace2/cancel',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Billings Collection (GET) ===========================================
# ============================= Return the hypermedia of a Billings Collection (OPTIONS) ===============================
billing_collection_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/billings',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Billings Document (GET) ===========================================
# =============================== Return the hypermedia of a Billings Document (OPTIONS) ===============================
# ======================================== PATCH the Billings Document (PATCH) =========================================
billing_document_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/billings/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ========================================= GET the Clauses Collection (GET) ===========================================
# ============================== Return the hypermedia of a Clauses Collection (OPTIONS) ===============================
clause_collection_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/clauses',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Clauses Document (GET) ============================================
# =============================== Return the hypermedia of a Clauses Document (OPTIONS) ================================
# ======================================== PATCH the Clauses Document (PATCH) ==========================================
clause_document_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/clauses/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ======================================== GET the Co Insureds Collection (GET) ========================================
# ============================= Return the hypermedia of a Co Insureds Collection (OPTIONS) ============================
# ====================================== POST the Co Insureds Collection (POST) ========================================
resume_in_aia_activity_bridge_resource_of_the_person_of_the_claim_party_of_the_claim = {
    'url': 'Replace1/memberships/Replace2/co_insureds',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Co Insureds Document (GET) ==========================================
# ============================= Return the hypermedia of a Co Insureds Document (OPTIONS) ==============================
# ===================================== DELETE the Co Insureds Document (DELETE) =======================================
# ====================================== PATCH the Co Insureds Document (PATCH) ========================================
co_insured_document_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/co_insureds/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# =================================== GET the Membership Components Collection (GET) ===================================
# ======================== Return the hypermedia of a Membership Components Collection (OPTIONS) =======================
# ================================= POST the Membership Components Collection (POST) ===================================
membership_component_collection_of_the_co_insured_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/co_insureds/Replace3/membership_components',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Membership Components Document (GET) ====================================
# ========================= Return the hypermedia of a Membership Components Document (OPTIONS) ========================
# ================================== PATCH the Membership Components Document (PATCH) ==================================
membership_component_document_of_the_co_insured_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/co_insureds/Replace3/membership_components/Replace4',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# =================================== GET the Membership Components Collection (GET) ===================================
# ======================== Return the hypermedia of a Membership Components Collection (OPTIONS) =======================
# ================================= POST the Membership Components Collection (POST) ===================================
membership_component_collection_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/membership_components',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ==================================== GET the Membership Components Document (GET) ====================================
# ========================= Return the hypermedia of a Membership Components Document (OPTIONS) ========================
# ================================= PATCH the Membership Components Document (PATCH) ===================================
membership_component_document_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/membership_components/Replace3',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}

# ================================== GET the Premium Simulation Save Controller (GET) ==================================
# ======================= Return the hypermedia of a Premium Simulation Save Controller (OPTIONS) ======================
# ================================ POST the Premium Simulation Save Controller (POST) ==================================
premium_simulation_membership_save_controller = {
    'url': 'Replace1/memberships/Replace2/premium_simulation',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ======================================== GET the Premiums Collection (GET) ===========================================
# ============================= Return the hypermedia of a Premiums Collection (OPTIONS) ===============================
premium_collection_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/premiums',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Premiums Document (GET) ===========================================
# =============================== Return the hypermedia of a Premiums Document (OPTIONS) ===============================
premium_document_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/premiums/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ====================================== GET the Savings Flows Collection (GET) ========================================
# =========================== Return the hypermedia of a Savings Flows Collection (OPTIONS) ============================
savings_flow_collection_of_the_premium_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/premiums/Replace3/savings_flows',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Savings Flows Document (GET) =========================================
# ============================ Return the hypermedia of a Savings Flows Document (OPTIONS) =============================
savings_flow_document_of_the_premium_of_the_membership = {
    'url': 'Replace1/memberships/Replace2/premiums/Replace3/savings_flows/Replace4',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================== GET the Verify Membership Save Controller (GET) ===================================
# ======================= Return the hypermedia of a Verify Membership Save Controller (OPTIONS) =======================
# ================================= POST the Verify Membership Save Controller (POST) ==================================
verify_membership_membership_save_controller = {
    'url': 'Replace1/memberships/Replace2/verify_membership',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}
