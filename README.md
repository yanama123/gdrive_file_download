# Download files from Google Drive

Feature 1: 

download: download files from google drive by file name

### Prerequisites:

    Python 3.5 or above need to be installed

    Note: If permissions are not there to set the environmental variables use the absolute path of python to execute the script:

    Example: C:\python3.6\python sample.py
    
### Steps to download files from google drive:

Step 1: Clone github repository using following command from command line:

    git clone https://github.com/yanama123/gdrive_file_download.git
    
Step 2: Execute the python file main_work_flow.py which is the Entry for Download files from Google Drive Flow:

    python main_work_flow.py
    
Step 3: The workflow will list 2 Options as shown below : 

    Please choose one option from following:
   
    1.  Enter File Name
    2.  Terminate programme
    
    Option 1: Download file with given File Name
    Option 2: Terminate Programme.
 
 
## Important Notes:

    1. Enable Google Drive API on Google Cloud Console: https://console.developers.google.com
    2. Check following google doc for more details on how to enable google drive API:
    https://developers.google.com/workspace/guides/create-project
    3. Once API is enabled and credentials.json/token.json is created , 
    make sure the file is copied to same directory where project was cloned.
    4. Run commandline as administrator.
      
### File Usage:
    main_work_flow.py - Entry for Download files from Google Drive Flow
    operations.py - Main logic to download files by file name.
    log.py - Creates logging using Python Decorator.
    
### Sample Input: 
    python main_work_flow.py
    
    ################## START #####################
    Please choose one option from following:
            1.  Enter File Name
            2.  Terminate programme
            1
    ################ Enter File Name ##################
    You have selected Enter File Name
    Enter File Name: DSC_6549.JPG


### Sample Output:

    03-Jun-21 00:14:27-operations-root-INFO : Search result: [('1dCi-nMsdSQJb7v23BNqRCi2kMCPemOdR', 'DSC_6549.JPG', 'image/jpeg')]
    03-Jun-21 00:14:27-operations-root-INFO : file id: 1dCi-nMsdSQJb7v23BNqRCi2kMCPemOdR
    03-Jun-21 00:14:27-log-root-INFO : Entering download_file_from_google_drive...
    03-Jun-21 00:14:27-log-root-INFO : Input Value: download_file_from_google_drive (<googleapiclient.discovery.Resource object at 0x0000020A012D3C08>, '1dCi-nMsdSQJb7v23BNqRCi2kMCPemOdR', 'DSC_6549.JPG')
    03-Jun-21 00:14:48-operations-root-INFO : Download 100%.