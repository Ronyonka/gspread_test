# Gspread Test
A test python script used to access google sheets api using the [gspread](https://github.com/burnash/gspread) module
## Installation
Clone the repo
```bash
git clone https://github.com/Ronyonka/gspread_test.git
```
and enter the project folder
```bash
cd gspread_test
```
Create a virtual environment
```bash
python3 -m venv venv
```
and activate it
```
source venv/bin/activate
```
Inside the virtual environment use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Setting Up The API
 First you should create a developer account (follow below steps) and create the type of credentials depending on your need.
* First Head to [Google Developers Console](https://console.developers.google.com) and create a new project (or select the one you have.)
* You will be redirected to the Project Dashboard, there click on “Enable Apis and services”, search for “Sheets API”.
* In the API screen click on ‘ENABLE’ to enable this API.
* Similarly enable the “Drive API”. We require drives api for getting list of spreadsheets, deleting them etc.
* Go to “Credentials” tab and choose “Create Credentials > Service Account Key”.
* Next choose a service name, in role select Project > Editor and Key type as JSON and click create.
* You will now be prompted to download a .json file. This file contains the necessary private key for account authorization.
* Download the .json file and rename it as `client_secret.json` and store it in the project folder. it should look like this
```json
{
  "type": "service_account",
  "project_id": "your_project-<project id>",
  "private_key_id": "your_private_key_id",
  "private_key": "your_private_key",
  "client_email": "name@your_project-<project id>.iam.gserviceaccount.com",
  "client_id": "101046519912784499381",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/<meta-data>.iam.gserviceaccount.com"
}
```
* On [Google Sheets](https://docs.google.com/spreadsheets/) create a new sheet named `'TestSheet'`
* Copy the `"client_email"` from  `client_secret.json` and on TestSheet click share button and paste the email address there and give it edit access
## Usage

* In TestSheet create two columns named `'NodeAddr'` and `'IMEI'` with several random dummy values
* In the code try to crossreference the node address with the equivalent IMEI values by changing the value in the variable node and running the script
```python
node = '1440087'
```

## License
[MIT](https://choosealicense.com/licenses/mit/)