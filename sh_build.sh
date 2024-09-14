#!/bin/bash

# Install python3-venv with Elevated Privileges
sudo apt install python3.12-venv

# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt

# Run the Streamlit app and make it accessible externally
streamlit run app/01_Home.py --server.port 8501 --server.address 0.0.0.0
