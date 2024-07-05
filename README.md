# P_URL_Shortner
It is a Python project for the url shortner

# Set-up the server
# create venv
python -m venv env

# Activate that venv
<!-- Powershell -->
Scripts\activate.ps1

# Install requirements
pip install -r requirements.txt
# Run
uvicorn main:app --reload