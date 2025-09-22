from fastapi.testclient import TestClient
from src.main import api

client = TestClient(api)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}


def test_add_ticket():
    ticket_data = {
        "id": 1,
        "flight_name": "Biman Bangladesh",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Dhaka"
    }
    response = client.post("/ticket", json=ticket_data)
    assert response.status_code == 200
    assert response.json() == ticket_data


def test_get_tickets():
    response = client.get("/ticket")
    assert response.status_code == 200
    tickets = response.json()
    assert isinstance(tickets, list)
    assert len(tickets) > 0  


def test_update_ticket():
    updated_data = {
        "id": 1,
        "flight_name": "NovoAir",
        "flight_date": "2025-10-16",
        "flight_time": "15:30",
        "destination": "Chattogram"
    }
    response = client.put("/ticket/1", json=updated_data)
    assert response.status_code == 200
    assert response.json() == updated_data


def test_delete_ticket():
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    deleted_ticket = response.json()
    assert deleted_ticket["id"] == 1

    
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    assert response.json() == {"error": "Ticket not found, deletion failed"}
