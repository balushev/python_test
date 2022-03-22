@nightly_run
Feature: Create Offer
""" This feature contains all scenarios for offer creation """

#  @test
  Scenario: Create a Offer for Home insurance (Add Home)
  """ This UI scenario testing creation of a offer for Home insurance (Add Home) """

    * Set resource name for locators Argenta Run => Offer => Home insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Pause for 3 seconds
    * Choose English for language options area
    * Choose Home insurance for Offer drop-down menu
    * Select a distributor with id 3588
    * Click Search Person link
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
    * Click Add home => Equipment page => "Next" button
    * Choose By questions for Add home => Risk evaluation page => "Evaluation method" options area


#  @test
  Scenario: Create a Offer for Home insurance (Add Family)
  """ This UI scenario testing creation of a offer for Home insurance (Add Family) """

    * Set resource name for locators Argenta Run => Offer => Home insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Pause for 3 seconds
    * Choose English for language options area
    * Choose Home insurance for Offer drop-down menu
    * Select a distributor with id 3588
    * Click Search Person link
    * Fill 3083383 in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Family" button
    * Choose 60 plus for Add family page => "Family situation" options area
    * Click Add family page => "OK" button
    * Click Add Family page => "Add Home" button
    * Click Add Family => Add home => Address page => "Next" button
    * Switch to default content
    * Switch to the iframe
    * Choose Apartment for Add Family => Add home => Home details page => "Type" options area
    * Choose Owner non occupant for Add Family => Add home => Home details page => "Usage" options area
    * Fill 1 in Add Family => Add home => Home details page => "Bedrooms" field
    * Fill 1 in Add Family => Add home => Home details page => "Bathrooms" field
    * Choose No for Add Family => Add home => Home details page => "Alarm system" options area
    * Choose No for Add Family => Add home => Home details page => "Classified property" options area
    * Choose Closed for Add Family => Add home => Home details page => "Abutment" options area
    * Choose before 1995 for Add Family => Add home => Home details page => "Building year" drop-down menu
    * Choose Habitation only for Add Family => Add home => Home details page => "Habitation usage" options area
    * Choose No for Add Family => Add home => Home details page => "Irregular habitation" options area
    * Choose No for Add Family => Add home => Home details page => "Flammable construction" options area
    * Click Add Family => Add Home => Home details page => "Next" button
    * Click Add Family => Add Home => Equipment page => "Next" button
    * Choose By questions for Add Family => Add Home => Risk evaluation page => "Evaluation method" options area


#  @test
  Scenario: Create a Offer for Car insurance (Add Car)
  """ This UI scenario testing creation of a offer for Car insurance (Add Car) """

    * Set resource name for locators Argenta Run => Offer => Car insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Pause for 3 seconds
    * Choose English for language options area
    * Choose Car insurance for Offer drop-down menu
    * Select a distributor with id 3588
    * Click Search Person link
    * Fill 3083383 in Search owner page => "Client ID" field
    * Click Search owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Car" button
    * Click Add car => Vehicle details page => Referential vehicle search button
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
    * Click Add car => Add Driver => Driver details page => "Next" button
    * Fill 278383 in Add car => Add Driver => Driver license page => "License ID" field
    * Fill 12/01/2019 in Add car => Add Driver => Driver license page => "License date" field
    * Choose B for Add car => Add driver => Driver license page => "License category" options area
    * Click Add car => Add driver => Driver license page => "Next" button
    * Click Add car => Add driver => Address page => "Next" button
    * Click Add car => Add driver => Contact page => "Next" button
    * Click Add car => Add driver page => "OK" button
    * Click Add car => Drivers page => "Next" button
    * Click Add car => Previous insurer page => "Next" button
    * Choose No for Add car => Risk background page => "Certificates" options area
    * Click Add car => Risk background page => "Next" button
    * Click Add car page => "OK" button
    * Click  "Coverage tariffs" button
    * Choose Own damage comfort for Add car => Coverage tariffs page options area
    * Click "Billing" button
    * Choose Direct credit for Billing page => "Type" options area
    * Choose Annual for Billing page => "Frequency" options area
    * Click "Risk acceptance" button
    * Click "Risk acceptance answer" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text


#  @test
  Scenario Template: Create a Offer for Car insurance (Add Old timer)
  """ This UI scenario testing creation of a offer for Car insurance (Add Old timer) """

    * Set resource name for locators Argenta Run => Offer => Car insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Pause for 3 seconds
    * Choose English for language options area
    * Choose Car insurance for Offer drop-down menu
    * Select a distributor with id 3588
    * Click Search Person link
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
    * Click Add old timer => Drivers page => "Add driver" button
    * Click Add Old timer => Add Driver => Add driver page => "Next" button
    * Fill <licenseID> in Add Old timer => Driver license page => "License ID" field
    * Fill <driverLicenseDate> in Add Old timer => Add driver => Driver license page => "License date" field
    * Choose <driverLicenseCategory> for Add Old timer => Add driver => Driver license page => "License category" options area
    * Click Add Old timer => Add driver => Driver license page => "Next" button
    * Click Add Old timer => Add driver => Address page => "Next" button
    * Click Add Old timer => Add driver => Contact page => "Next" button
    * Click Add Old timer => Add driver page => "OK" button
    * Click Add Old timer => Drivers page => "Next" button
    * Click Add Old timer => Previous insurer page => "Next" button
    * Choose <certificates> for Add Old timer => Risk background page => "Certificates" options area
    * Click Add Old timer => Risk background page => Certificates => "Next" button
    * Click Add Old timer page => "OK" button
    * Click  "Coverage tariffs" button
    * Choose <coverageTariffs> for Add Old timer => Coverage tariffs page options area
    * Click "Billing" button
    * Choose <billingType> for Billing page => "Type" options area
    * Choose <billingFrequency> for Billing page => "Frequency" options area
    * Fill <billingRenewalDay> in Billing page => "Billing renewal day" field
    * Fill <billingRenewalMonth> in Billing page => "Billing renewal month" field
    * Click "Risk acceptance" button
    * Click "Risk acceptance answer" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains <verifyCongratulationsMessage> text

    Scenarios: Test data for Offer -> Car insurance (Add Old timer)
      | ownerID | vehicleMake | vehicleModel | vehicleVersion | vehicleType           | vehiclePower | firstUseDate | numberOfSeats | registrationNumber | chassisNumber | registrationType | fuelType | usageType | claimNature | claimDate  | claimLiability | claimDriverType | claimDriverDateOfBirth | claimJokerUsed | claimAmount | claimRiskFullyRepaired | licenseID | driverLicenseDate | driverLicenseCategory | certificates | coverageTariffs       | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth | verifyCongratulationsMessage |
      | 3083383 | Rolls Royce | Phantom      | 5              | Old timer private car | 100          | 09/09/1990   | 5             | O1111CA            | 11183765      | Normal Plate     | Electric | Private   | Accident    | 08/08/2018 | 0 percent      | Primary         | 08/08/1980             | Yes            | 3000        | No                     | 74898744  | 12/02/2019        | B                     | No           | Legal assistance safe | Direct credit | Annual           | do not execute    | do not execute      | Your proposition with number |
      | 3083383 | Jaguar      | E-Type       | do not execute | Old timer private car | 100          | 09/09/1990   | 5             | O1111CA            | 11183765      | Normal Plate     | Electric | Private   | Accident    | 08/08/2018 | 0 percent      | Primary         | 08/08/1980             | Yes            | 3000        | No                     | 74898744  | 12/02/2019        | B                     | No           | Legal assistance safe | Direct credit | Annual           | do not execute    | do not execute      | do not execute               |


#  @test
  Scenario Template: Create a Offer for Car insurance (Add Van)
  """ This UI scenario testing creation of a offer for Car insurance (Add Van) """

    * Set resource name for locators Argenta Run => Offer => Car insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Pause for 3 seconds
    * Choose English for language options area
    * Choose Car insurance for Offer drop-down menu
    * Select a distributor with id 3588
    * Click Search Person link
    * Fill <ownerID> in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Van" button
    * Click Add van => Vehicle details page => "Referential search" button
    * Fill <vehicleMake> in Add van => Preferential vehicle search page => "Make"  field
    * Fill <vehicleModel> in Add van => Preferential vehicle search page => "Model" field
    * Click Add van => Preferential vehicle search page => "Search" button
    * Click Referential first search result
    * Choose <vehicleType> for Add van => Vehicle details page => "Vehicle type" drop-down menu
    * Fill <firstUseDate> in Add van => Vehicle details page => "First use date" field
    * Fill <numberOfSeats> in Add van => Vehicle details page => "Number of seats" field
    * Fill <registrationNumber> in Add van => Vehicle details page => "Registration number" field
    * Fill <chassisNumber> in Add van => Vehicle details page => "Chassis number" field
    * Choose <registrationType> for Add van => Vehicle details page => "Registration type" options area
    * Choose <fuelType> for Add van => Vehicle details page => "Fuel type" options area
    * Choose <usageType> for Add van => vehicle details page => "Usage type" options area
    * Click Add van => vehicle details page => "Next" button
    * Fill <vehicleValue> in Add van => Risk evaluation page => "Vehicle value" field
    * Fill <accessoriesEquipmentValue> in Add van => Risk evaluation page => "Accessories equipment value" field
    * Click Add car => Risk evaluation page => "Next" button
    * Click Add van => Claim history page => "Add claim" button
    * Choose <claimNature> for Add van => Add claim page => "Nature" drop-down menu
    * Fill <claimDate> in Add van => Add claim page => "Date" field
    * Choose <claimLiability> for Add van => Add claim page => "Liability" drop-down menu
    * Choose <claimDriverType> for Add van => Add claim page => "Driver type" drop-down menu
    * Fill <claimDriverDateOfBirth> in Add van => Add claim page => "Driver date of birth" field
    * Choose <claimJokerUsed> for Add van => Add claim page => "Joker used" options area
    * Fill <claimAmount> in Add van => Add claim page => "Amount" field
    * Choose <claimRiskFullyRepaired> for Add van => Add claim page => "Risk fully repaired" options area
    * Click Add van => Add claim page => "OK" button
    * Click Add van => Claim history page => "Next" button
    * Click Add van => Drivers page => "Add driver" button
    * Click Add van => Add driver page => "Next" button
    * Fill <licenseID> in Add van => Driver license page => "license ID" field
    * Fill <driverlicenseDate> in Add van => Add driver => Driver license page => "License date" field
    * Choose <driverlicenseCategory> for Add van => Add driver => Driver license page => "license category" options area
    * Click Add van => Add driver => Driver license page => "Next" button
    * Click Add van => Add driver => Address page => "Next" button
    * Click Add van => Add driver => Contact page => "Next" button
    * Click Add van => Add driver page => "OK" button
    * Click Add van => Drivers page => "Next" button
    * Click Add van => Previous insurer page => "Next" button
    * Choose <certificates> for Add van => Risk background page => "Certificates" options area
    * Click Add van => Risk background page => Certificates => "Next" button
    * Click Add van page => "OK" button
    * Click  "Coverage tariffs" button
    * Choose <coverageTariffs> for Add van => Coverage tariffs page options area
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

    Scenarios: Test data for Offer -> Car insurance (Add Van)
      | ownerID | vehicleMake | vehicleModel | vehicleType                          | firstUseDate | numberOfSeats | registrationNumber | chassisNumber | registrationType | fuelType | usageType | claimNature | claimDate  | claimLiability | claimDriverType | claimDriverDateOfBirth | claimJokerUsed | claimAmount | claimRiskFullyRepaired | licenseID | driverlicenseDate | driverlicenseCategory | certificates | coverageTariffs       | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth | vehicleValue | accessoriesEquipmentValue |
      | 3083383 | Peugeot     | Traveller    | Station wagon or All-terrain vehicle | 09/09/1990   | 8             | O1111CA            | 11183765      | Normal Plate     | Electric | Private   | Accident    | 08/08/2018 | 0 percent      | Primary         | 08/08/1980             | Yes            | 3000        | No                     | 74898744  | 12/02/2019        | B                     | No           | Legal assistance safe | Direct credit | Annual           | do not execute    | do not execute      | 45000        | 3500                      |


#  @test
  Scenario Template: Create a Offer for Car insurance (Add Truck Camper)
  """ This UI scenario testing creation of a offer for Car insurance (Add Truck Camper) """

    * Set resource name for locators Argenta Run => Offer => Car insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Pause for 3 seconds
    * Choose English for language options area
    * Choose Car insurance for Offer drop-down menu
    * Select a distributor with id 3588
    * Click Search Person link
    * Fill <ownerID> in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Truck Camper" button
    * Choose <vehicleType> for Add Truck Camper => Vehicle details page => "Vehicle type" drop-down menu
    * Fill <vehicleMake> in Add Truck Camper => Vehicle details page => "Make"  field
    * Fill <vehicleModel> in Add Truck Camper => Vehicle details page => "Model" field
    * Fill <vehiclePower> in Add Truck Camper => Vehicle details page => "Power" field
    * Fill <firstUseDate> in Add Truck Camper => Vehicle details page => "First use date" field
    * Fill <numberOfSeats> in Add Truck Camper => Vehicle details page => "Number of seats" field
    * Fill <registrationNumber> in Add Truck Camper=> Vehicle details page => "Registration number" field
    * Fill <chassisNumber> in Add Truck Camper => Vehicle details page => "Chassis number" field
    * Choose <registrationType> for Add Truck Camper => Vehicle details page => "Registration type" options area
    * Choose <fuelType> for Add Truck Camper => Vehicle details page => "Fuel type" options area
    * Choose <usageType> for Add Truck Camper => Vehicle details page => "Usage type" options area
    * Click Add Truck Camper => Vehicle details page => "Next" button
    * Fill <vehicleValue> in Add Truck Camper => Risk evaluation page => "Vehicle value" field
    * Fill <accessoriesEquipment> in Add Truck Camper => Risk evaluation page => "Accessories equipment value" field
    * Click Add Truck Camper => Risk evaluation page => "Next" button
    * Click Add Truck Camper => Claim history page => "Add Claim" button
    * Choose <claimNature> for Add Truck Camper => Add Claim page => "Nature" drop-down menu
    * Fill <claimDate> in Add Truck Camper => Add claim page => "Date" field
    * Choose <claimLiability> for Add Truck Camper => Add claim page => "Liability" drop-down menu
    * Choose <claimDriverType> for Add Truck Camper => Add claim page => "Driver type" drop-down menu
    * Fill <claimDriverDateOfBirth> in Add Truck Camper => Add claim page => "Driver date of birth" field
    * Choose <claimJokerUsed> for Add Truck Camper => Add claim page => "Joker used" options area
    * Fill <claimAmount> in Add Truck Camper => Add claim page => "Amount" field
    * Choose <claimRiskFullyRepaired> for Add Truck Camper => Add claim page => "Risk fully repaired" options area
    * Click Add Truck Camper => Add claim page => "OK" button
    * Click Add Truck Camper => Claim history page => "Next" button
    * Click Add Truck Camper => Drivers page => "Add driver" button
    * Click Add Truck Camper => Add driver => Driver details page => "Next" button
    * Fill <licenseID> in Add Truck Camper => Add driver => Driver license page => "License ID" field
    * Fill <driverlicenseDate> in Add Truck Camper => Add driver => Driver license page => "License date" field
    * Choose <driverlicenseCategory> for Add Truck Camper => Add driver => Driver license page => "License category" options area
    * Click Add Truck Camper => Add driver => Driver license page => "Next" button
    * Click Add Truck Camper => Add driver => Address page => "Next" button
    * Click Add Truck Camper => Add driver => Contact page => "Next" button
    * Click Add Truck Camper => Add driver page => "OK" button
    * Click Add Truck Camper => Drivers page => "Next" button
    * Click Add Truck Camper => Previous insurer page => "Next" button
    * Choose <certificates> for Add Truck Camper => Risk background page => "Certificates" options area
    * Click Add Truck Camper => Risk background page => Certificates => "Next" button
    * Click Add Truck Camper page => "OK" button
    * Click  "Coverage tariffs" button
    * Choose <coverageTariffs> for Add Truck Camper => Coverage tariffs page options area
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

    Scenarios: Test data for Offer -> Car insurance (Add Truck Camper)
      | ownerID | vehicleMake   | vehicleModel   | vehicleType | vehiclePower | firstUseDate | numberOfSeats | registrationNumber | chassisNumber | registrationType | fuelType | usageType | vehicleValue | accessoriesEquipment | claimNature | claimDate  | claimLiability | claimDriverType | claimDriverDateOfBirth | claimJokerUsed | claimAmount | claimRiskFullyRepaired | licenseID | driverlicenseDate | driverlicenseCategory | certificates | coverageTariffs    | billingType   | billingFrequency | billingRenewalDay | billingRenewalMonth |
      | 3083383 | Mercedes-Benz | Grand Canyon S | Camping car | 100          | 09/09/1990   | 5             | O1111CA            | 11183765      | Normal Plate     | Electric | Private   | 75000        | 7500                 | Accident    | 08/08/2018 | 0 percent      | Primary         | 08/08/1980             | Yes            | 3000        | No                     | 74898744  | 12/02/2019        | B                     | No           | Own damage comfort | Direct credit | Annual           | do not execute    | do not execute      |


#  @test
  Scenario: Create a Offer for Family insurance
  """ This UI scenario testing creation of a offer for Family insurance """

    * Set resource name for locators Argenta Run => Offer => Family insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Pause for 3 seconds
    * Choose English for language options area
    * Choose Family insurance for Offer drop-down menu
    * Select a distributor with id 3588
    * Click Search Person link
    * Fill 3083383 in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Family" button
    * Choose 60 plus for Add Family page => "Family situation" options area
    * Click Add Family page => "OK" button
    * Click  "Coverage tariffs" button
    * Click "Billing" button
    * Choose Direct credit for Billing page => "Type" options area
    * Choose Annual for Billing page => "Frequency" options area
    * Fill 18 in Billing page => Renewal day field
    * Fill 3 in Billing page => Renewal month field
    * Click "Risk acceptance" button
    * Click Add Family page => Risk acceptance answer => "No" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text


#  @test
  Scenario: Create a Offer for Motorcycle insurance (Add Motorcycle)
  """ This UI scenario testing creation of a offer for Motorcycle insurance (Add Motorcycle) """

    * Set resource name for locators Argenta Run => Offer => Motorcycle insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Pause for 3 seconds
    * Choose English for language options area
    * Choose Motorcycle insurance for Offer drop-down menu
    * Select a distributor with id 3588
    * Click Search Person link
    * Fill 3083383 in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Motorcycle" button
    * Fill Honda in Add motorcycle => Vehicle details page => "Make" field
    * Fill Rebel 500 in Add motorcycle => Vehicle details page => "Model" field
    * Choose Three wheel motorcycle for Add motorcycle => Vehicle details page => "Vehicle type" drop-down menu
    * Fill 500 in Add motorcycle => Vehicle details page => "Cubic capacity" field
    * Fill HO1111JP in Add motorcycle => Vehicle details page => "Registration number" field
    * Fill 839020773 in Add motorcycle => Vehicle details page => "Chassis number" field
    * Choose Normal Plate for Add motorcycle => Vehicle details page => "Registration type" options area
    * Choose Electric for Add motorcycle => Vehicle details page => "Fuel type" options area
    * Choose Private for Add motorcycle => Vehicle details page => "Usage type" options area
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
    * Fill 3783826 in Add motorcycle => Driver license page => "license ID" field
    * Fill 12/01/2019 in Add motorcycle => Add driver => Driver license page => "License date" field
    * Choose A1 for Add motorcycle => Add driver => Driver license page => "license category" options area
    * Click Add motorcycle => Add driver => Driver license page => "Next" button
    * Click Add motorcycle => Add driver => Address page => "Next" button
    * Click Add motorcycle => Add driver => Contact page => "Next" button
    * Click Add motorcycle => Add driver page => "OK" button
    * Click Add motorcycle page => "OK" button
    * Click "Coverage Tariffs" button
    * Choose Legal assistance basis for Add motorcycle => Coverage Tariffs page => "Coverages" options area
    * Click "Billing" button
    * Choose Direct credit for Billing page => "Type" options area
    * Choose Annual for Billing page => "Frequency" options area
    * Click "Risk acceptance" button
    * Click Add motorcycle => Risk acceptance page => "Answer No" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text


  @test
  Scenario: Create a Offer for Motorcycle insurance (Add Moped)
  """ This UI scenario testing creation of a offer for Motorcycle insurance (Add Moped) """

    * Set resource name for locators Argenta Run => Offer => Motorcycle insurance
    * Log in to the application
    * Switch to the iframe
    * Choose Omnichannel for Application menu options area
    * Pause for 3 seconds
    * Choose English for language options area
    * Choose Motorcycle insurance for Offer drop-down menu
    * Select a distributor with id 3588
    * Click Search Person link
    * Fill 3083383 in Search owner page => "Client ID" field
    * Click Search Owner page => "Search" button
    * Click Referential first search result
    * Click "Risk" button
    * Click "Add Moped" button
    * Choose Class A for Add moped => Vehicle details page => "Vehicle type" drop-down menu
    * Fill Honda in Add moped => Vehicle details page => "Make" field
    * Fill Revo in Add moped => Vehicle details page => "Model" field
    * Fill 49 in Add moped => Vehicle details page => "Cubic capacity" field
    * Fill H377RVO in Add moped => Vehicle details page => "Registration number" field
    * Fill 939376627 in Add moped => Vehicle details page => "Chassis number" field
    * Choose Normal Plate for Add moped => Vehicle details page => "Registration type" options area
    * Choose Electric for Add moped => Vehicle details page => "Fuel type" options area
    * Choose Private for Add moped => Vehicle details page => "Usage type" options area
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
    * Fill 3783826 in Add moped => Driver license page => "license ID" field
    * Fill 12/01/2019 in Add moped => Add driver => Driver license page => "License date" field
    * Choose A1 for Add moped => Add driver => Driver license page => "license category" options area
    * Click Add moped => Add driver => Driver license page => "Next" button
    * Click Add moped => Add driver => Address page => "Next" button
    * Click Add moped => Add driver => Contact page => "Next" button
    * Click Add moped => Add driver page => "OK" button
    * Click Add moped page => "OK" button
    * Click "Coverage Tariffs" button
    * Choose Legal assistance basis for Add moped => Coverage Tariffs page => "Coverages" options area
    * Click "Billing" button
    * Choose Direct credit for Billing page => "Type" options area
    * Choose Annual for Billing page => "Frequency" options area
    * Click "Risk acceptance" button
    * Click Add moped => Risk acceptance page => "Answer No" button
    * Click "Summary" button
    * Click "Submission" button
    * Wait for Offer congratulations message
    * Verify Offer congratulations message contains "Your proposition with number" text
