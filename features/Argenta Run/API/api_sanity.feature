Feature: Create Quote with API
""" This feature contains all scenarios for quote creation using APIs """

  @new
  Scenario: Create a Quote for Home insurance with API (Home) - no UI
  """ This UI scenario testing creation of a quote for Home insurance with API (Home) """

    * Get distributor
      | distributorPositionInList |
      | 1                         |

    * Create quotes
  """
    {
      "quote:distributor_id": "3588",
      "quote:product_id": "VZWP01"
    }
   """

    * Get owner
      | ownerPositionInList |
      | random              |

    * Get person
      | firstName  | lastName | clientID | dateOfBirth |indexInTheList|
      | Lamxxxxxxx | skip     | skip     | skip        |random|

#    * Update quote owner person link
