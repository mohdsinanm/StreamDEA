# Makefile for Streamlit App

# Variables
APP_NAME = app.py  # Replace with your Streamlit app file name
VENV = venv  # Virtual environment directory

.PHONY: all install run clean

# Default target
# all: install run

# Install dependencies
# install:
# 	@echo "Installing dependencies..."
# 	@poetry install

# Run the Streamlit app
run:
	@echo "Running the Streamlit app..."
	@streamlit run $(APP_NAME)