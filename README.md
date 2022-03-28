[![Build Status](https://dev.azure.com/dori1411/testing-course-man1/_apis/build/status/ddorenDK.testing-course-man1?branchName=main)](https://dev.azure.com/dori1411/testing-course-man1/_build/latest?definitionId=2&branchName=main)
### Group G
![testingMan1](https://user-images.githubusercontent.com/89907196/160425690-ff275589-d72a-4d2e-ba85-ec39ec19ce18.png)

Dorin Moldovan, Radu Cazacu

---

Coding Language: Python

CI: Azure Devops Pipelines (yaml)

Deadline: 29-03-2022 23:59

---


### System under test

The application generates fake information for non-existing Danish persons:

- Name and gender 
  - First Name
  - Last Name
  - Gender
  - *Randomly Extracted*

- CPR 10 numeric digits
  - First six - ddMMyy
  - Last four random (female final even, male even odd)

- Date of Birth 
  - Must Match the date in the CPR

- Address. Compound Information
  - Street. A random assortment of alphabetic characters
  - Number. A number from 1 to 999, optionally followed by an uppercase letter (e.g., 43B)
  - Floor. Either st or a number from 1 to 99
  - Door. “th”, “mf”, “tv”, a number from 1 to 50, or a lowercase letter optionally followed by a dash, then followed by one to three numeric digits (e.g., c3, d-14)
  - Postal code and town.Randomly extracted from the provided database addresses.sql

- Mobile Phone Number
  - Format: Eight numeric digits
  - It must start by some of the following digit combinations: 2, 30, 31, 40, 41, 42, 50, 51, 52, 53, 60, 61, 71, 81, 91, 92, 93, 342, 344-349, 356-357, 359, 362, 365-366, 389, 398, 431, 441, 462, 466,  468,  472,  474,  476,  478,  485-486,  488-489,  493-496,  498-499,  542-543,  545,  551-552, 556, 571-574, 577, 579, 584, 586-587, 589, 597-598, 627, 629, 641, 649, 658, 662-665, 667, 692-694, 697, 771-772, 782-783, 785-786, 788-789, 826-827,829

---

#### Functionalities
The Application must:
- Return a fake CPR
- Return a fake full name and gender
- Return a fake full name, genderand date of birth
- Return a fake CPR, full name and gender
- Return a fake CPR, full name, genderand date of birth
- Return a fake address
- Return a fake mobile phone number
- Return all information for a fake person (CPR, full name, gender, date of birth, address, mobile phone number)
- Return fake person information in bulk (all information for 2 to 100 persons)

---

#### Testing 
The following testing-related tasks must be implemented:
- Writing unit tests and integration tests whenever it is considered appropriate
- Designing the test cases based on:
  - Black-box design techniques (manual analysis)
  - White-box design techniques (automated analysis with tools)
- Use static testing tools toanalyse and improve the code. Also for white-box analysis, if the chosen unit testing framework does not provide it
- Create a Continuous Integration job or pipeline to test the integration of the application
- Run all unit and integration tests in the CI process

---




