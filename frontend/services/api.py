"""API service for frontend."""
import requests

BASE_URL = "http://localhost:8000"


def get_students():
    response = requests.get(f"{BASE_URL}/students/")
    response.raise_for_status()
    return response.json()


def get_questions():
    response = requests.get(f"{BASE_URL}/questions/")
    response.raise_for_status()
    return response.json()


def get_assessments():
    response = requests.get(f"{BASE_URL}/assessments/")
    response.raise_for_status()
    return response.json()
