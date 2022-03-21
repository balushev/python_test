@nightly_run
Feature: Create Quote
""" This feature contains all scenarios for quote creation """

#  @test
  Scenario Template: Create a Quote for Home insurance (Add Home)
  """ This UI scenario testing creation of a quote for Home insurance (Add Home) """

    * Set resource name for locators Argenta Run => Quote => Home insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Choose English for language options area
    * Choose <quoteInsurance> for Quote drop-down menu
    * Select a distributor with id 3588
    * Click "Search Owner" button
    * Fill 3083383 in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Home" button
    * Click Add home => Address page => "Next" button
    * Choose Apartment for Add home => Home details page => "Type" options area
    * Choose Owner non occupant for Add home => Home details page => "Usage" options area
    * Fill 1 in Add home => Home details page => "Bedrooms" field
    * Fill 1 in Add home => Home details page => "Bathrooms" field
    * Choose No for Add home => Home details page => "Alarm system" options area
    * Choose No for Add home => Home details page => "Classified property" options area
    * Choose Closed for Add home => Home details page => "Abutment" options area
    * Choose before 1995 for Add home => Home details page => "Building year" drop-down menu
    * Choose Habitation only for Add home => Home details page => "Habitation usage" options area
    * Choose No for Add home => Home details page => "Irregular habitation" options area
    * Choose No for Add home => Home details page => "Flammable construction" options area
    * Click Add home => Home details page => "Next" button

    Scenarios: Test data for Home insurance (Home)
      | quoteInsurance | ownerFirstName | vehicleMake | vehicleModel | vehicleType   | firstUseDate | numberOfSeats | registrationNumber | chassisNumber | registrationType | fuelType | usageType | vehicleValue | accessoriesEquipment | claimNature | claimDate  | claimLiability | claimDriverType | claimDriverDateOfBirth | claimJokerUsed | claimAmount | claimRiskFullyRepaired | driverLicenseDate | driverLicenseCategory | certificates | coverageTariffs    | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth |
      | Home insurance | Lamxxxxxxx     | peugeot     | 3008         | Passenger car | 09/09/2021   | 5             | CA1111CA           | 11183765      | Normal Plate     | Electric | Private   | 30000        | 5000                 | Accident    | 08/08/2018 | 0 percent      | Primary         | 08/08/1980             | Yes            | 3000        | No                     | 12/02/2019        | B                     | No           | Own damage comfort | Direct credit | Annual           | 13                | 5                   |


#  @test
  Scenario Template: Create a Quote for Home insurance (Add Family)
  """ This UI scenario testing creation of a quote for Home insurance (Add Family) """

    * Set resource name for locators Argenta Run => Quote => Home insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Choose English for language options area
    * Choose <quoteInsurance> for Quote drop-down menu
    * Select a distributor with id 3588
    * Click "Search Owner" button
    * Fill <ownerID> in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Family" button
    * Choose 60 plus for Add family page => "Family situation" options area
    * Click Add family page => "OK" button
    * Click "Coverage Tariffs" button
    * Click "Summary" button
    * Click "Proceed to Offer" button
    * Click "Risk" button
    * Click "Add Home" button
    * Click Add family => Add home => Address page => "Next" button
    * Choose Apartment for Add family => Add home => Home details page => "Type" options area
    * Choose Owner non occupant for Add family => Add home => Home details page => "Usage" options area
    * Fill 1 in Add family => Add home => Home details page => "Bedrooms" field
    * Fill 1 in Add family => Add home => Home details page => "Bathrooms" field
    * Choose No for Add family => Add home => Home details page => "Alarm system" options area
    * Choose No for Add family => Add home => Home details page => "Classified property" options area
    * Choose Closed for Add family => Add home => Home details page => "Abutment" options area
    * Choose before 1995 for Add family => Add home => Home details page => "Building year" drop-down menu
    * Choose Habitation only for Add family => Add home => Home details page => "Habitation usage" options area
    * Choose No for Add family => Add home => Home details page => "Irregular habitation" options area
    * Choose No for Add family => Add home => Home details page => "Flammable construction" options area
    * Click Add family => Add home => Home details page => "Next" button

    Scenarios: Test data for Home insurance (Family)
      | quoteInsurance | ownerID | vehicleMake | vehicleModel | vehicleType   | firstUseDate | numberOfSeats | registrationNumber | chassisNumber | registrationType | fuelType | usageType | vehicleValue | accessoriesEquipment | claimNature | claimDate  | claimLiability | claimDriverType | claimDriverDateOfBirth | claimJokerUsed | claimAmount | claimRiskFullyRepaired | driverLicenseDate | driverLicenseCategory | certificates | coverageTariffs    | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth |
      | Home insurance | 3083383 | peugeot     | 3008         | Passenger car | 09/09/2021   | 5             | CA1111CA           | 11183765      | Normal Plate     | Electric | Private   | 30000        | 5000                 | Accident    | 08/08/2018 | 0 percent      | Primary         | 08/08/1980             | Yes            | 3000        | No                     | 12/02/2019        | B                     | No           | Own damage comfort | Direct credit | Annual           | 13                | 5                   |


#  @test
  Scenario: Create a Quote for Car insurance (Add Car)
  """ This UI scenario testing creation of a quote for Car insurance (Add Car) """

    * Set resource name for locators Argenta Run => Quote => Car insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Choose English for language options area
    * Choose Car insurance for Quote drop-down menu
    * Select a distributor with id 3588
    * Click "Search Owner" button
    * Fill 3083383 in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Car" button
    * Click Add car => Vehicle details page => "Referential search" button
    * Fill peugeot in Add car => Preferential vehicle search page => "Make"  field
    * Fill 3008 in Add car => Preferential vehicle search page => "Model" field
    * Click Add car => Preferential vehicle search page => "Search" button
    * Click Referential first search result
    * Choose Passenger car for Add car => Vehicle details page => "Vehicle type" drop-down menu
    * Fill 09/09/2021 in Add car => Vehicle details page => "First use date" field
    * Fill 5 in Add car => Vehicle details page => "Number of seats" field
    * Fill CA1111CA in Add car => Vehicle details page => "Registration number" field
    * Fill 11183765 in Add car => Vehicle details page => "Chassis number" field
    * Choose Normal Plate for Add car => Vehicle details page => "Registration type" options area
    * Choose Electric for Add car => Vehicle details page => "Fuel type" options area
    * Choose Private for Add car => vehicle details page => "Usage type" options area
    * Click Add car => vehicle details page => "Next" button
    * Fill 30000 in Add car => Risk evaluation page => "Vehicle value" field
    * Fill 5000 in Add car => Risk evaluation page => "Accessories equipment value" field
    * Click Add car => Risk evaluation page => "Next" button
    * Click Add car => Claim history page => "Add claim" button
    * Choose Accident for Add car => Add claim page => "Nature" drop-down menu
    * Fill 08/08/2018 in Add car => Add claim page => "Date" field
    * Choose 0 percent for Add car => Add claim page => "Liability" drop-down menu
    * Choose Primary for Add car => Add claim page => "Driver type" drop-down menu
    * Fill 08/08/1980 in Add car => Add claim page => "Driver date of birth" field
    * Choose Yes for Add car => Add claim page => "Joker used" options area
    * Fill 3000 in Add car => Add claim page => "Amount" field
    * Choose No for Add car => Add claim page => "Risk fully repaired" options area
    * Click Add car => Add claim page => "OK" button
    * Click Add car => Claim history page => "Next" button
    * Click Add car => Drivers page => "Add driver" button
    * Click Add car => Add driver page => "Next" button
    * Fill 12/02/2019 in Add car => Add driver => Driver license page => "License date" field
    * Choose B for Add car => Add driver => Driver license page => "License category" options area
    * Click Add car => Add driver => Driver license page => "Next" button
    * Click Add car => Add driver => Address page => "Next" button
    * Click Add car => Add driver page => "OK" button
    * Click Add car => Drivers page => "Next" button
    * Choose No for Add car => Risk background page => "Certificates" options area
    * Click Add car => Risk background page => "Next" button
    * Click Add car page => "OK" button
    * Click  "Coverage tariffs" button
    * Choose Own damage comfort for Add car => Coverage tariffs page options area
    * Click "Summary" button
    * Click "Proceed to offer" button
    * Click "Risk" button
    * Click  "Coverage tariffs" button
    * Click "Billing" button
    * Choose Direct credit for Billing page => "Type" options area
    * Choose Annual for Billing page => "Frequency" options area
    * Fill 21 in Billing page => Renewal day field
    * Fill 3 in Billing page => Renewal month field
    * Click "Risk acceptance" button
    * Click "Risk acceptance answer" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text

#  @test
  Scenario Template: Create a Quote for Car insurance (Add Car)
  """ This UI scenario testing creation of a quote for Car insurance (Add Car) """

    * Set resource name for locators Argenta Run => Quote => Car insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Choose English for language options area
    * Choose <quoteInsurance> for Quote drop-down menu
    * Select a distributor with id 3588
    * Click "Search Owner" button
    * Fill <ownerID> in Search owner page => "Client ID" field
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
    * Choose <usageType> for Add car => Vehicle details page => "Usage type" options area
    * Click Add car => Vehicle details page => "Next" button
    * Fill <vehicleValue> in Add car => Risk evaluation page => "Vehicle value" field
    * Fill <accessoriesEquipment> in Add car => Risk evaluation page => "Accessories equipment value" field
    * Click Add car => Risk evaluation page => "Next" button
    * Click Add car => Claim history page => "Add Claim" button
    * Choose <claimNature> for Add car => Add claim page => "Nature" drop-down menu
    * Fill <claimDate> in Add car => Add claim page => "Date" field
    * Choose <claimLiability> for Add car => Add claim page => "Liability" drop-down menu
    * Choose <claimDriverType> for Add car => Add claim page => "Driver type" drop-down menu
    * Fill <claimDriverDateOfBirth> in Add car => Add claim page => "Driver date of birth" field
    * Choose <claimJokerUsed> for Add car => Add claim page => "Joker used" options area
    * Fill <claimAmount> in Add car => Add claim page => "Amount" field
    * Choose <claimRiskFullyRepaired> for Add car => Add claim page => "Risk fully repaired" options area
    * Click Add car => Add claim page => "OK" button
    * Click Add car => Claim history page => "Next" button
    * Click Add car => Drivers page => "Add Driver" button
    * Click Add car => Add driver page => "Next" button
    * Fill <driverLicenseDate> in Add car => Add driver => Driver license page => "License date" field
    * Choose <driverLicenseCategory> for Add car => Add driver => Driver license page => "License category" options area
    * Click Add car => Add driver => Driver license page => "Next" button
    * Click Add car => Add driver => Address page => "Next" button
    * Click Add car => Add driver page => "OK" button
    * Click Add car => Drivers page => "Next" button
    * Choose <certificates> for Add car => Risk background page => "Certificates" options area
    * Click Add car => Risk background page => Certificates => "Next" button
    * Click Add car page => "OK" button
    * Click  "Coverage tariffs" button
    * Choose <coverageTariffs> for Add car => Coverage tariffs page options area
    * Click "Summary" button
    * Click "Proceed to offer" button
    * Click "Risk" button
    * Click  "Coverage tariffs" button
    * Click "Billing" button
    * Choose <billingType> for Billing page => "Type" options area
    * Choose <billingFrequency> for Billing page => "Frequency" options area
    * Fill <billingRenewalDay> in Billing page => "Renewal day" field
    * Fill <billingRenewalMonth> in Billing page => "Renewal month" field
    * Click "Risk acceptance" button
    * Click "Risk acceptance answer" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text

    Scenarios: Test data for Car insurance (Add Car)
      | quoteInsurance | ownerID | vehicleMake | vehicleModel | vehicleType   | firstUseDate | numberOfSeats | registrationNumber | chassisNumber | registrationType | fuelType   | usageType    | vehicleValue | accessoriesEquipment | claimNature | claimDate  | claimLiability | claimDriverType | claimDriverDateOfBirth | claimJokerUsed | claimAmount | claimRiskFullyRepaired | driverLicenseDate | driverLicenseCategory | certificates | coverageTariffs    | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth |
      | Car insurance  | 3083383 | peugeot     | 3008         | Passenger car | 09/09/2021   | 5             | CA1111CA           | 11183765      | Normal Plate     | Electric   | Private      | 30000        | 5000                 | Accident    | 08/08/2018 | 0 percent      | Primary         | 08/08/1980             | Yes            | 3000        | No                     | 12/02/2019        | B                     | No           | Own damage comfort | Direct credit | Annual           | do not execute    | do not execute      |
      | Car insurance  | 3083383 | citroen     | jumper       | Minibus       | 09/09/2021   | 5             | CO13CA             | 46748gh7      | Trader plate     | Diesel oil | Professional | 50000        | 0                    | Fire        | 08/08/2018 | 100 percent    | Secondary       | 08/08/1980             | No             | 1530        | Yes                    | 12/02/2019        | BE                    | No           | Driver plus        | Direct credit | semi annual      | do not execute    | do not execute      |


#  @test
  Scenario Template: Create a Quote for Car insurance (Add Old timer)
  """ This UI scenario testing creation of a quote for Car insurance (Add Old timer) """

    * Set resource name for locators Argenta Run => Quote => Car insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Choose English for language options area
    * Choose <quoteInsurance> for Quote drop-down menu
    * Select a distributor with id 3588
    * Click Search Owner button
    * Fill <ownerID> in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Old timer" button
    * Fill <vehicleMake> in Add Old timer => Vehicle details page => "Make"  field
    * Fill <vehicleModel> in Add Old timer => Vehicle details page => "Model" field
    * Fill <vehicleVersion> in Add Old timer => Vehicle details page => "Version" field
    * Choose <vehicleType> for Add Old timer => Vehicle details page => "Vehicle type" drop-down menu
    * Fill <vehiclePower> in Add Old timer => Vehicle details page => "Power" field
    * Fill <firstUseDate> in Add Old timer => Vehicle details page => "First use date" field
    * Fill <numberOfSeats> in Add Old timer => Vehicle details page => "Number of seats" field
    * Fill <registrationNumber> in Add Old timer => Vehicle details page => "Registration number" field
    * Fill <chassisNumber> in Add Old timer => Vehicle details page => "Chassis number" field
    * Choose <registrationType> for Add Old timer => Vehicle details page => "Registration type" options area
    * Choose <fuelType> for Add Old timer => Vehicle details page => "Fuel type" options area
    * Choose <usageType> for Add Old timer => Vehicle details page => "Usage type" options area
    * Click Add Old timer => Vehicle details page => "Next" button
    * Click Add Old timer => Claim history page => "Add claim" button
    * Choose <claimNature> for Add Old timer => Add claim page => "Nature" drop-down menu
    * Fill <claimDate> in Add Old timer => Add claim page => "Date" field
    * Choose <claimLiability> for Add Old timer => Add claim page => "Liability" drop-down menu
    * Choose <claimDriverType> for Add Old timer => Add claim page => "Driver type" drop-down menu
    * Fill <claimDriverDateOfBirth> in Add Old timer => Add claim page => "Driver date of birth" field
    * Choose <claimJokerUsed> for Add Old timer => Add claim page => "Joker used" options area
    * Fill <claimAmount> in Add Old timer => Add claim page => "Amount" field
    * Choose <claimRiskFullyRepaired> for Add Old timer => Add claim page => "Risk fully repaired" options area
    * Click Add Old timer => Add claim page => "OK" button
    * Click Add Old timer => Claim history page => "Next" button
    * Click Add Old timer => Drivers page => "Add driver" button
    * Click Add Old timer => Add driver page => "Next" button
    * Fill <driverLicenseDate> in Add Old timer => Add driver => Driver license page => "License date" field
    * Choose <driverLicenseCategory> for Add Old timer => Add driver => Driver license page => "License category" options area
    * Click Add Old timer => Add driver => Driver license page => "Next" button
    * Click Add Old timer => Add driver => Address page => "Next" button
    * Click Add Old timer => Add driver page => "OK" button
    * Click Add Old timer => Drivers page => "Next" button
    * Choose <certificates> for Add Old timer => Risk background page => "Certificates" options area
    * Click Add Old timer => Risk background page => "Next" button
    * Click Add Old timer page => "OK" button
    * Click "Coverage tariffs" button
    * Choose <coverageTariffs> for Add Old timer => Coverage tariffs page options area
    * Click "Summary" button
    * Click "Proceed to offer" button
    * Click "Risk" button
    * Click  "Coverage tariffs" button
    * Click "Billing" button
    * Choose <billingType> for Billing page => "Type" options area
    * Choose <billingFrequency> for Billing page => "Frequency" options area
    * Fill <billingRenewalDay> in Billing page => "Renewal day" field
    * Fill <billingRenewalMonth> in Billing page => "Renewal month" field
    * Click "Risk acceptance" button
    * Click "Risk acceptance answer" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text

    Scenarios: Test data for Car insurance (Add Old timer)
      | quoteInsurance | ownerID | vehicleMake | vehicleModel | vehicleVersion | vehicleType           | vehiclePower | firstUseDate | numberOfSeats | registrationNumber | chassisNumber | registrationType | fuelType | usageType | claimNature | claimDate  | claimLiability | claimDriverType | claimDriverDateOfBirth | claimJokerUsed | claimAmount | claimRiskFullyRepaired | driverLicenseDate | driverLicenseCategory | certificates | coverageTariffs       | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth |
      | Car insurance  | 3083383 | Rolls Royce | Phantom      | 5              | Old timer private car | 100          | 09/09/1990   | 5             | O1111CA            | 11183765      | Normal Plate     | Electric | Private   | Accident    | 08/08/2018 | 0 percent      | Primary         | 08/08/1980             | Yes            | 3000        | No                     | 12/02/2019        | B                     | No           | legal assistance safe | Direct credit | Annual           | do not execute    | do not execute      |


#  @test
  Scenario Template: Create a Quote for Car insurance (Add Van)
  """ This UI scenario testing creation of a quote for Car insurance (Add Van) """

    * Set resource name for locators Argenta Run => Quote => Car insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Choose English for language options area
    * Choose <quoteInsurance> for Quote drop-down menu
    * Select a distributor with id 3588
    * Click "Search Owner" button
    * Fill <ownerID> in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Van" button
    * Click Add Van => Vehicle details page => "Referential search" button
    * Fill <vehicleMake> in Add Van => Preferential vehicle search page => "Make"  field
    * Fill <vehicleModel> in Add Van => Preferential vehicle search page => "Model" field
    * Click Add Van => Preferential vehicle search page => "Search" button
    * Click Referential first search result
    * Choose <vehicleType> for Add Van => Vehicle details page => "Vehicle type" drop-down menu
    * Fill <firstUseDate> in Add Van => Vehicle details page => "First use date" field
    * Fill <numberOfSeats> in Add Van => Vehicle details page => "Number of seats" field
    * Fill <registrationNumber> in Add Van => Vehicle details page => "Registration number" field
    * Fill <chassisNumber> in Add Van => Vehicle details page => "Chassis number" field
    * Choose <registrationType> for Add Van => Vehicle details page => "Registration type" options area
    * Choose <fuelType> for Add Van => Vehicle details page => "Fuel type" options area
    * Choose <usageType> for Add Van => vehicle details page => "Usage type" options area
    * Click Add Van => vehicle details page => "Next" button
    * Fill <vehicleValue> in Add van => Risk evaluation page => "Vehicle value" field
    * Fill <accessoriesEquipmentValue> in Add van => Risk evaluation page => "Accessories equipment value" field
    * Click Add car => Risk evaluation page => "Next" button
    * Click Add Van => Claim history page => "Add claim" button
    * Choose <claimNature> for Add Van => Add claim page => "Nature" drop-down menu
    * Fill <claimDate> in Add Van => Add claim page => "Date" field
    * Choose <claimLiability> for Add Van => Add claim page => "Liability" drop-down menu
    * Choose <claimDriverType> for Add Van => Add claim page => "Driver type" drop-down menu
    * Fill <claimDriverDateOfBirth> in Add Van => Add claim page => "Driver date of birth" field
    * Choose <claimJokerUsed> for Add Van => Add claim page => "Joker used" options area
    * Fill <claimAmount> in Add Van => Add claim page => "Amount" field
    * Choose <claimRiskFullyRepaired> for Add Van => Add claim page => "Risk fully repaired" options area
    * Click Add Van => Add claim page => "OK" button
    * Click Add Van => Claim history page => "Next" button
    * Click Add Van => Drivers page => "Add driver" button
    * Click Add Van => Add driver page => "Next" button
    * Fill <driverLicenseDate> in Add Van => Add driver => Driver license page => "License date" field
    * Choose <driverlicenseCategory> for Add Van => Add driver => Driver license page => "license category" options area
    * Click Add Van => Add driver => Driver license page => "Next" button
    * Click Add Van => Add driver => Address page => "Next" button
    * Click Add Van => Add driver => "OK" button
    * Click Add Van => Drivers page => "Next" button
    * Choose <certificates> for Add Van => Risk background page => "Certificates" options area
    * Click Add Van => Risk background page =>  "Next" button
    * Click Add Van page => "OK" button
    * Click "Coverage tariffs" button
    * Choose <coverageTariffs> for Add Van => Coverage tariffs page options area
    * Click "Summary" button
    * Click "Proceed to offer" button
    * Click "Risk" button
    * Click  "Coverage tariffs" button
    * Click "Billing" button
    * Choose <billingType> for Billing page => "Type" options area
    * Choose <billingFrequency> for Billing page => "Frequency" options area
    * Fill <billingRenewalDay> in Billing page => "Renewal day" field
    * Fill <billingRenewalMonth> in Billing page => "Renewal month" field
    * Click "Risk acceptance" button
    * Click "Risk acceptance answer" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text

    Scenarios: Test data for Car insurance (Add Van)
      | quoteInsurance | ownerID | vehicleMake | vehicleModel | vehicleType | firstUseDate | numberOfSeats | registrationNumber | chassisNumber | registrationType | fuelType | usageType | claimNature | claimDate  | claimLiability | claimDriverType | claimDriverDateOfBirth | claimJokerUsed | claimAmount | claimRiskFullyRepaired | driverlicenseCategory | driverLicenseDate | certificates | coverageTariffs       | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth | vehicleValue | accessoriesEquipmentValue |
      | Car insurance  | 3083383 | PEUGEOT     | BOXER        | truck       | 09/09/1990   | 5             | O1111CA            | 11183765      | Normal Plate     | Electric | Private   | Accident    | 08/08/2018 | 0 percent      | Primary         | 08/08/1980             | Yes            | 3000        | No                     | B                     | 12/02/2019        | No           | legal assistance safe | Direct credit | Annual           | do not execute    | do not execute      | 47250        | 3300                      |


#  @test
  Scenario Template: Create a Quote for Car insurance (Add Truck Camper)
  """ This UI scenario testing creation of a quote for Car insurance (Add Truck Camper) """

    * Set resource name for locators Argenta Run => Quote => Car insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Choose English for language options area
    * Choose <quoteInsurance> for Quote drop-down menu
    * Select a distributor with id 3588
    * Click "Search Owner" button
    * Fill <ownerID> in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Truck Camper" button
    * Choose <vehicleType> for Add Truck Camper page => "Vehicle type" drop-down menu
    * Fill <vehicleMake> in Add Truck Camper page => "Make"  field
    * Fill <vehicleModel> in Add Truck Camper page => "Model" field
    * Fill <vehiclePower> in Add Truck Camper page => "Power" field
    * Fill <firstUseDate> in Add Truck Camper page => "First use date" field
    * Fill <numberOfSeats> in Add Truck Camper page => "Number of seats" field
    * Fill <registrationNumber> in Add Truck Camper page => "Registration number" field
    * Fill <chassisNumber> in Add Truck Camper page => "Chassis number" field
    * Choose <registrationType> for Add Truck Camper page => "Registration type" options area
    * Choose <fuelType> for Add Truck Camper page => "Fuel type" options area
    * Choose <usageType> for Add Truck Camper page => "Usage type" options area
    * Click Add Truck Camper => Vehicle details page => "Next" button
    * Fill <vehicleValue> in Add Truck Camper => Risk evaluation page => "Vehicle value" field
    * Fill <accessoriesEquipment> in Add Truck Camper => Risk evaluation page => "Accessories equipment value" field
    * Click Add Truck Camper => Risk evaluation page => "Next" button
    * Click  Add Truck Camper => Claim history page => "Add claim" button
    * Choose <claimNature> for  Add Truck Camper => Add claim page => "Nature" drop-down menu
    * Fill <claimDate> in Add Truck Camper => Add claim page => "Date" field
    * Choose <claimLiability> for  Add Truck Camper => Add claim page => "Liability" drop-down menu
    * Choose <claimDriverType> for  Add Truck Camper => Add claim page => "Driver type" drop-down menu
    * Fill <claimDriverDateOfBirth> in  Add Truck Camper => Add claim page => "Driver date of birth" field
    * Choose <claimJokerUsed> for  Add Truck Camper => Add claim page => "Joker used" options area
    * Fill <claimAmount> in  Add Truck Camper => Add claim page => "Amount" field
    * Choose <claimRiskFullyRepaired> for  Add Truck Camper => Add claim page => "Risk fully repaired" options area
    * Click  Add Truck Camper => Add claim page => "OK" button
    * Click Add Truck Camper => Claim history page => "Next" button
    * Click  Add Truck Camper => Drivers page => "Add driver" button
    * Click Add Truck Camper => Add driver => Driver details page => "Next" button
    * Fill <driverlicenseDate> in  Add Truck Camper => Add driver => Driver license page => "License date" field
    * Choose <driverlicenseCategory> for  Add Truck Camper => Add driver => Driver license page => "license category" options area
    * Click Add Truck Camper => Add driver => Driver license page => "Next" button
    * Click Add Truck Camper => Add driver => Address page => "Next" button
    * Click Add Truck Camper => Add driver page => "OK" button
    * Click Add Truck Camper => Drivers page => "Next" button
    * Choose <certificates> for  Add Truck Camper => Risk background page => "Certificates" options area
    * Click Add Truck Camper => Risk background page => Certificates page => "Next" button
    * Click Add Truck Camper page => "OK" button
    * Click "Coverage tariffs" button
    * Choose <coverageTariffs> for Add Old timer => Coverage tariffs page options area
    * Click "Summary" button
    * Click "Proceed to offer" button
    * Click "Risk" button
    * Click  "Coverage tariffs" button
    * Click "Billing" button
    * Choose <billingType> for Billing page => "Type" options area
    * Choose <billingFrequency> for Billing page => "Frequency" options area
    * Fill <billingRenewalDay> in Billing page => Renewal day field
    * Fill <billingRenewalMonth> in Billing page => Renewal month field
    * Click "Risk acceptance" button
    * Click "Risk acceptance answer" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text

    Scenarios: Test data for Car insurance (Add Truck Camper)
      | quoteInsurance | ownerID | vehicleMake   | vehicleModel   | vehicleType | vehiclePower | firstUseDate | numberOfSeats | registrationNumber | chassisNumber | registrationType | fuelType | usageType | vehicleValue | accessoriesEquipment | claimNature | claimDate  | claimLiability | claimDriverType | claimDriverDateOfBirth | claimJokerUsed | claimAmount | claimRiskFullyRepaired | driverlicenseDate | driverlicenseCategory | certificates | coverageTariffs       | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth |
      | Car insurance  | 3083383 | Mercedes-Benz | Grand Canyon S | Camping car | 100          | 09/09/1990   | 5             | O1111CA            | 11183765      | Normal Plate     | Electric | Private   | 75000        | 7500                 | Accident    | 08/08/2018 | 0 percent      | Primary         | 08/08/1980             | Yes            | 3000        | No                     | 12/02/2019        | B                     | No           | legal assistance safe | Direct credit | Annual           | do not execute    | do not execute      |


#  @test
  Scenario Template: Create a Quote for Family insurance
  """ This UI scenario testing creation of a quote for Family insurance """

    * Set resource name for locators Argenta Run => Quote => Family insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Choose English for language options area
    * Choose <quoteInsurance> for Quote drop-down menu
    * Select a distributor with id 3588
    * Click "Search Owner" button
    * Fill <ownerID> in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Choose <branchOwner> for Home => "Branch owner" drop-down menu
    * Click "Add Family" button
    * Choose <familySituation> for Add Family page => "Family situation" options area
    * Click Add Family page => "OK" button
    * Click "Coverage Tariffs" button
    * Click "Summary" button
    * Click "Proceed to Offer" button
    * Click "Risk" button
    * Click "Coverage Tariffs" button
    * Click "Billing" button
    * Choose <billingType> for Billing page => "Type" options area
    * Choose <billingFrequency> for Billing page => "Frequency" options area
    * Fill <billingRenewalDay> in Billing page => Renewal day field
    * Fill <billingRenewalMonth> in Billing page => Renewal month field
    * Click "Risk acceptance" button
    * Choose <addExtraInformation> for Risk acceptance page => "Add extra information" options area
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text

    Scenarios: Test data for Family insurance
      | quoteInsurance   | ownerID | branchOwner | familySituation | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth | addExtraInformation |
      | Family insurance | 3083383 | NC          | 60 plus         | Direct credit | Annual           | do not execute    | do not execute      | No                  |


#  @test
  Scenario Template: Create a Quote for Motorcycle insurance (Add Motorcycle)
  """ This UI scenario testing creation of a quote for Motorcycle insurance (Add Motorcycle) """

    * Set resource name for locators Argenta Run => Quote => Motorcycle insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Choose English for language options area
    * Choose <quoteInsurance> for Quote drop-down menu
    * Select a distributor with id 3588
    * Click "Search Owner" button
    * Fill <ownerID> in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Motorcycle" button
    * Fill <make> in Add motorcycle => Vehicle details page => "Make" field
    * Fill <model> in Add motorcycle => Vehicle details page => "Model" field
    * Choose <vehicleType> for Add motorcycle => Vehicle details page => "Vehicle type" drop-down menu
    * Fill <cubicCapacity> in Add motorcycle => Vehicle details page => "Cubic capacity" field
    * Fill <registrationNumber> in Add motorcycle => Vehicle details page => "Registration number" field
    * Fill <chassisNumber> in Add motorcycle => Vehicle details page => "Chassis number" field
    * Choose <registrationType> for Add motorcycle => Vehicle details page => "Registration type" options area
    * Choose <fuelType> for Add motorcycle => Vehicle details page => "Fuel type" options area
    * Choose <usageType> for Add motorcycle => Vehicle details page => "Usage type" options area
    * Click Add motorcycle => Vehicle details page => "Next" button
    * Click Add motorcycle => Claim history page => "Add claim" button
    * Choose Accident for Add motorcycle => Add claim page => "Nature" drop-down menu
    * Fill 08/08/2018 in Add motorcycle => Add claim page => "Date" field
    * Choose 0 percent for Add motorcycle => Add claim page => "Liability" drop-down menu
    * Choose Primary for Add motorcycle => Add claim page => "Driver type" drop-down menu
    * Fill 08/08/1980 in Add motorcycle => Add claim page => "Driver date of birth" field
    * Fill 3000 in Add motorcycle => Add claim page => "Amount" field
    * Choose No for Add motorcycle => Add claim page => "Risk fully repaired" options area
    * Click Add motorcycle => Add claim page => "OK" button
    * Click Add motorcycle => Claim history page => "Next" button
    * Click Add motorcycle => Drivers page => "Add driver" button
    * Click Add motorcycle => Add driver page => "Next" button
    * Fill 12/02/2019 in Add motorcycle => Add driver => Driver license page => "License date" field
    * Choose A1 for Add motorcycle => Add driver => Driver license page => "license category" options area
    * Click Add motorcycle => Add driver => Driver license page => "Next" button
    * Click Add motorcycle => Add driver => Address page => "Next" button
    * Click Add motorcycle => Add driver page => "OK" button
    * Click Add motorcycle page => "OK" button
    * Click "Coverage Tariffs" button
    * Choose <coverages> for Add motorcycle => Coverage Tariffs page => "Coverages" options area
    * Click "Summary" button
    * Click "Proceed to Offer" button
    * Click "Risk" button
    * Click "Coverage Tariffs" button
    * Click "Billing" button
    * Choose <billingType> for Billing page => "Type" options area
    * Choose <billingFrequency> for Billing page => "Frequency" options area
    * Fill <billingRenewalDay> in Billing page => Renewal day field
    * Fill <billingRenewalMonth> in Billing page => Renewal month field
    * Click "Risk acceptance" button
    * Click Add motorcycle => Risk acceptance page => "Answer No" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text

    Scenarios: Test data for Motorcycle insurance (Add Motorcycle)
      | quoteInsurance       | ownerID | make | model | vehicleType            | cubicCapacity | registrationNumber | chassisNumber | registrationType | fuelType | usageType | coverages              | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth |
      | Motorcycle insurance | 3083383 | BG   | Honda | Three wheel motorcycle | 100           | CA1111CA           | 1372918       | Normal Plate     | Electric | Private   | Legal assistance basis | Direct credit | Annual           | do not execute    | do not execute      |


#  @test
  Scenario Template: Create a Quote for Motorcycle insurance (Add Moped)
  """ This UI scenario testing creation of a quote for Motorcycle insurance (Add Moped) """

    * Set resource name for locators Argenta Run => Quote => Motorcycle insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Choose English for language options area
    * Choose <quoteInsurance> for Quote drop-down menu
    * Select a distributor with id 3588
    * Click "Search Owner" button
    * Fill <ownerID> in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Moped" button
    * Choose <vehicleType> for Add moped => Vehicle details page => "Vehicle type" drop-down menu
    * Fill <make> in Add moped => Vehicle details page => "Make" field
    * Fill <model> in Add moped => Vehicle details page => "Model" field
    * Fill <cubicCapacity> in Add moped => Vehicle details page => "Cubic capacity" field
    * Fill <registrationNumber> in Add moped => Vehicle details page => "Registration number" field
    * Fill <chassisNumber> in Add moped => Vehicle details page => "Chassis number" field
    * Choose <registrationType> for Add moped => Vehicle details page => "Registration type" options area
    * Choose <fuelType> for Add moped => Vehicle details page => "Fuel type" options area
    * Choose <usageType> for Add moped => Vehicle details page => "Usage type" options area
    * Click Add moped => Vehicle details page => "Next" button
    * Click Add moped => Claim history page => "Add claim" button
    * Choose Accident for Add moped => Add claim page => "Nature" drop-down menu
    * Fill 08/08/2018 in Add moped => Add claim page => "Date" field
    * Choose 0 percent for Add moped => Add claim page => "Liability" drop-down menu
    * Choose Primary for Add moped => Add claim page => "Driver type" drop-down menu
    * Fill 08/08/1980 in Add moped => Add claim page => "Driver date of birth" field
    * Fill 3000 in Add moped => Add claim page => "Amount" field
    * Choose No for Add moped => Add claim page => "Risk fully repaired" options area
    * Click Add moped => Add claim page => "OK" button
    * Click Add moped => Claim history page => "Next" button
    * Click Add moped => Drivers page => "Add driver" button
    * Click Add moped => Add driver page => "Next" button
    * Fill 12/02/2019 in Add moped => Add driver => Driver license page => "License date" field
    * Choose B for Add moped => Add driver => Driver license page => "license category" options area
    * Click Add moped => Add driver => Driver license page => "Next" button
    * Click Add moped => Add driver => Address page => "Next" button
    * Click Add moped => Add driver page => "OK" button
    * Click Add moped page => "OK" button
    * Click "Coverage Tariffs" button
    * Choose <coverages> for Add moped => Coverage Tariffs page => "Coverages" options area
    * Click "Summary" button
    * Click "Proceed to Offer" button
    * Click "Risk" button
    * Click "Coverage Tariffs" button
    * Click "Billing" button
    * Choose <billingType> for Billing page => "Type" options area
    * Choose <billingFrequency> for Billing page => "Frequency" options area
    * Fill <billingRenewalDay> in Billing page => "Renewal day" field
    * Fill <billingRenewalMonth> in Billing page => "Renewal month" field
    * Click "Risk acceptance" button
    * Click Add moped => Risk acceptance page => "Answer No" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text

    Scenarios: Test data for Motorcycle insurance (Add Moped)
      | quoteInsurance       | ownerID | make | model | vehicleType | cubicCapacity | registrationNumber | chassisNumber | registrationType | fuelType | usageType | coverages              | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth |
      | Motorcycle insurance | 3083383 | BG   | Honda | Class A     | 49            | CA1111CA           | 1372918       | Normal Plate     | Electric | Private   | Legal assistance basis | Direct credit | Annual           | do not execute    | do not execute      |
