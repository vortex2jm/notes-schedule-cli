# Notes CLI
This app is for daily organization. It gives you a way to create google calendar events and write notes by a command line interface at linux terminal.
 
## Instructions
 - Before using the app you have to create a directory to credentials into *src/*:

```bash
cd src && mkdir token
```

 - Now you have to download your google developer credentials and put into *token/* with name *credentials.json*
 - To use notes, you have to create an account at MongoDB Atlas and save *username* and *password* into *token/* with _.env_ 

## Requirements
To run app you have to install some libraries. These libraries are in *./documentation/requirements.txt*

```bash
pip install -r requirements.txt
```

## Recommendations
 - You can add this app on PATH and run it anywhere.