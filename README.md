# ChatGPT_Equipment_List

This originally was an experiment if I could have ChatGPT write a Flask base website to manage the equipment I use in the lab. 
So far I found it could not specifically write the entire program but it could give me a good number of code snippets with an
explaination. Without any python experience I don't think ChatGPT will be much help, but if you are learning or know python 
then ChatGPT is an excellent resource. For now I'll continue to write the script and ask ChatGPT for help along the way as I 
think it will really be useful to myself and possibly to others. 

Here are my goals for this script:
1. Track all the equipment across our group's labs.
  - Where is it?
  - Who has it?
  - When will it be returned to storage? (so someone else can use it)
  - What is it's status? (Broken, Lost, In Use, Stored, Out of Calibration, etc...)
  - What project is it being used for? (To be use later if equipment is out of spec and we need to which projects are affected)
2. Produce reports
  - List equipment out of calibration
  - List equipment overdue checkout
  - List equipment sent to calibration
  - List broken or lost equipment
3. Create a checkout/checkin process
  - List immediately availble equipment
  - List equipment already checked out but allow a user to reserve the equipment once retured
  - Create a form to force the user to input all the needed information (reservation dates, project)
  - Email equipment custodian when equipment is being requested and by whom
  - After the equipment has been checked out email the user a receipt of the reservation
  - Email users when their equipment needs to be returned. (Possibly allow users to add an extension)
  - Have a search filter equipment based on reservation dates so that the equipment reservation does not extend over a 
    scheduled calibration or maintenance date. (Maybe this should be a default?)
4. Different authentication levels
  - administrator - Can edit and add all equipment, assign roles, assign equipment to custodians, and see all reports
  - custodian - Can edit and add their own equipment, can transfer their equipment to another custodian, and see their reports. 
  - users - Can reserve equipment
5. Log all equipment changes and statuses

Database equipment fields:
  - id (auto assigned)
  - equipment custodian
  - equipment type
  - equipment manufactuer
  - equipment model
  - equipment manufactuer serial number
  - calibration serial number
  - calibration next due date
  - RFID tag
  - equipment current location
  - equipment checked out by (This could be a user id that will refer to another database of user information)
  - equipment checked out date
  - equipment return due date
  - equipment status (broken, calibration due, out for calibration, checked out, available, reserved?)
  - equipment long description
  - equipment photo
  
Database user fields:
  - username
  - password??
  - email
  - name
  - phone number (text?)
  - access (user, custodian, adminstrator)
  
  
