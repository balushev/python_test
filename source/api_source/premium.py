# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 14:45:36 2022

@author: bbalushev
"""


# ========================================= GET the Premiums Collection (GET) ==========================================
# ============================== Return the hypermedia of a Premiums Collection (OPTIONS) ==============================
premium_collection = {
    'url': 'Replace1/financials/premiums',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ========================================== GET the Premiums Document (GET) ===========================================
# =============================== Return the hypermedia of a Premiums Document (OPTIONS)= ==============================
premium_document = {
    'url': 'Replace1/financials/premiums/Replace2',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================  GET the Savings Flows Collection (GET) =======================================
# =========================== Return the hypermedia of a Savings Flows Collection (OPTIONS) ============================
savings_flow_collection_of_the_premium = {
    'url': 'Replace1/financials/premiums/Replace2/savings_flows',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ======================================= GET the Savings Flows Document (GET) =========================================
# ============================ Return the hypermedia of a Savings Flows Document (OPTIONS) =============================
savings_flow_document_of_the_premium = {
    'url': 'Replace1/financials/premiums/Replace2/savings_flows/Replace3',
    'request_methods_list': ['GET', 'OPTIONS']
}
