Feature: profile 1
""" This feature contains all scenarios for quote creation """

#  @test
  Scenario Template: Create a Quote for Car insurance (Add Car)
  """ This UI scenario testing creation of a quote for Car insurance (Add Car) """

    * Set resource name for locators Argenta Run => Quote => Car insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Pause for 3 seconds
    * Choose English for language options area
    * Choose Car insurance for Quote drop-down menu
    * Select a distributor with id 3588
    * Click "Search Owner" button
    * Fill <clientID> in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Car" button
    * Click Add Car => Vehicle details page => Referential search button
    * Fill <vehicleMake> in Add car => Preferential vehicle search page => "Make"  field
    * Fill <vehicleModel> in Add car => Preferential vehicle search page => "Model" field
    * Click Add car => Preferential vehicle search page => "Search" button
    * Click Referential first search result
    * Choose <vehicleType> for Add car => Vehicle details page => "Vehicle type" drop-down menu
    * Fill <firstUseDate> in Add car => Vehicle details page => "First use date" field
    * Fill <numberOfSeats> in Add car => Vehicle details page => "Number of seats" field
    * Fill <registrationNumber> in Add car => Vehicle details page => "Registration number" field
    * Fill <chassisNumber> in Add car => Vehicle details page => "Chassis number" field
    * Choose <registrationType> for Add car => Vehicle details page => "Registration type" options area
    * Choose <fuelType> for Add car => Vehicle details page => "Fuel type" options area
    * Choose <usageType> for Add car => vehicle details page => "Usage type" options area
    * Click Add car => Vehicle details page => "Next" button
    * Fill <vehicleValue> in Add car => Risk evaluation page => "Vehicle value" field
    * Fill <accessoriesEquipment> in Add car => Risk evaluation page => "Accessories equipment value" field
    * Click Add car => Risk evaluation page => "Next" button
    * Click <addClaimButton> button
    * Choose <claimNature> for Add car => Add claim page => "Nature" drop-down menu
    * Fill <claimDate> in Add car => Add claim page => "Date" field
    * Choose <claimLiability> for Add car => Add claim page => "Liability" drop-down menu
    * Choose <claimDriverType> for Add car => Add claim page => "Driver type" drop-down menu
    * Fill <claimDriverDateOfBirth> in Add car => Add claim page => "Driver date of birth" field
    * Choose <claimJokerUsed> for Add car => Add claim page => "Joker used" options area
    * Fill <claimAmount> in Add car => Add claim page => "Amount" field
    * Choose <claimRiskFullyRepaired> for Add car => Add claim page => "Risk fully repaired" options area
    * Click <addClaimPageOKButton> button
    * Click Add car => Claim history page => "Next" button
    * Click Add car => Drivers page => "Add Driver" button
    * Click Add car => Add driver page => "Next" button
    * Fill <driverlicenseDate> in Add car => Add driver => Driver license page => "License date" field
    * Choose <driverlicenseCategory> for Add car => Add driver => Driver license page => "license category" options area
    * Click Add car => Add driver => Driver license page => "Next" button
    * Click Add car => Add driver => Address page => "Next" button
    * Click Add car => Add driver page => "OK" button
    * Click Add car => Drivers page => "Next" button
    * Choose <certificates> for Add car => Risk background page => "Certificates" options area
    * Click Add car => Risk background page => Certificates => "Next" button
    * Click Add car page => "OK" button
    * Choose <commissionPercentage> for Add car => Risk page => "Branch owner" drop-down menu
    * Click  "Coverage tariffs" button
    * Choose <coverageTariffs1> for Add car => Coverage tariffs page options area
    * Choose <coverageTariffs2> for Add car => Coverage tariffs page options area
    * Choose <coverageTariffs3> for Add car => Coverage tariffs page options area
    * Choose <coverageTariffs4> for Add car => Coverage tariffs page options area
    * Click "Summary" button
    * Click "Proceed to offer" button
    * Click "Risk" button
    * Click  "Coverage tariffs" button
    * Choose <tariffAdjustment> for Add car => Add claim page => "Risk fully repaired" options area
    * Click "Billing" button
    * Click "Risk acceptance" button
    * Click "Risk acceptance answer" button
    * Click "Summary" button
    * Click "Submission" button
#    * Click "Save Quote" button
#    * Click "Submit to offer" button


    Scenarios: Test data for Car insurance (Car)
      | clientID | vehicleMake | vehicleModel | vehicleType   | firstUseDate | numberOfSeats | registrationNumber | chassisNumber  | registrationType | fuelType   | usageType | vehicleValue   | accessoriesEquipment | claimNature    | claimDate      | claimLiability | claimDriverType | claimDriverDateOfBirth | claimJokerUsed | claimAmount    | claimRiskFullyRepaired | driverlicenseDate | driverlicenseCategory | certificates | commissionPercentage | coverageTariffs1 | coverageTariffs2 | coverageTariffs3      | coverageTariffs4 | billingType  | billingFrequency | billingRenewalDay | billingRenewalMonth | tariffAdjustment | addClaimButton | addClaimPageOKButton |
      | 3083383  | AUDI        | A3           | Passenger car | 07/01/2022   | 5             | SA123RA            | do not execute | Normal Plate     | Diesel oil | Private   | do not execute | 2000                 | do not execute | do not execute | do not execute | do not execute  | do not execute         | do not execute | do not execute | do not execute         | 01/01/2019        | B                     | No           | 10.0%                | Partial omnium   | Own damage Basic | Legal assistance safe | do not execute   | Direct Debit | Annual           | do not execute    | do not execute      | do not execute   | do not execute | do not execute       |
#      | 3083383  | AUDI        | A3           | Passenger car | 07/01/2022   | 5             | SA123RA            | do not execute | Normal Plate     | Diesel oil | Private   | do not execute | 2000                 | do not execute | do not execute | do not execute | do not execute  | do not execute         | do not execute | do not execute | do not execute         | 01/01/2019        | B                     | No           | 10.0%                | Partial omnium   | Own damage Basic | Legal assistance safe | do not execute   | Direct Debit | Annual           | do not execute    | do not execute      |                  | Add car => Claim history page => "Add Claim" |Add car => Add claim page => "OK"|
     
      
      
      
