# -*- coding: utf-8 -*-
"""
Created on Mon Jan  3 11:12:13 2022

@author: bbalushev
"""

str_1 = 'Contract Driver Collection of the Risk'
str_2 = 'Contract Driver Document of the Risk'
str_3 = 'Risk Equipment Collection of the Risk'
str_4 = 'Risk Equipment Document of the Risk'
str_5 = 'Property Recorded Claim Collection of the Risk'
str_6 = 'Property Recorded Claim Document of the Risk'
str_7 = 'Property Zone Collection of the Risk'
str_8 = 'Property Zone Document of the Risk'

risk_dict = {
    'Bus': [str_1, str_2, str_3, str_4, str_5, str_6],
    'Caravan': [str_1, str_2],
    'Family': [str_1, str_2],
    'GenericVehicle': [str_1, str_2, str_3, str_4, str_5, str_6],
    'Home': [str_1, str_2],
    'IndustrialBuilding': [str_1, str_2, str_3, str_4, str_5, str_6],
    'Machine': [str_1, str_2, str_3, str_4, str_5, str_6],
    'OtherRisk': [str_1, str_2, str_3, str_4, str_5, str_6, str_7, str_8],
    'SingleLife': [str_1, str_2, str_3, str_4, str_5, str_6, str_7, str_8],
    'Trailer': [str_1, str_2],
    'Truck': [str_1, str_2, str_3, str_4, str_5, str_6]
}



# ===================================  (GET) ====================================
# ========================  (OPTIONS) ========================
operation_collection_of_the_activity_of_the_person_of_the_claim_party_of_the_claim = {
    'url': '',
    'request_methods_list': ['GET', 'OPTIONS']
}

# ================================  (GET) ================================
# =====================  (OPTIONS) ====================
# ==============================  (POST) ===============================
resume_in_aia_activity_bridge_resource_of_the_person_of_the_claim_party_of_the_claim = {
    'url': '',
    'request_methods_list': ['GET', 'OPTIONS', 'POST']
}

# ================================  (GET) ================================
# =====================  (OPTIONS) ====================
# =============================  (DELETE) ===============================
# ==============================  (PATCH) ===============================
process_activity_operation_of_the_activity_of_the_person_of_the_claim_party_of_the_claim_with_process_id = {
    'url': '',
    'request_methods_list': ['GET', 'OPTIONS', 'DELETE', 'PATCH']
}

# ================================  (GET) ================================
# =====================  (OPTIONS) ====================
# ==============================  (PATCH) ===============================
resume_in_aia_activity_bridge_resource_of_the_person_of_the_claim_party_of_the_claim = {
    'url': '',
    'request_methods_list': ['GET', 'OPTIONS', 'PATCH']
}