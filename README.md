# 5G-Based Remote Patient Monitoring System

A proof-of-concept remote healthcare monitoring system using
Open5GS, UERANSIM, Python and Flask.

## Features
- Simulated 5G standalone network using Open5GS and UERANSIM
- Successful UE registration and PDU session establishment
- Patient vital-sign simulation
- Real-time heart rate, SpO2 and temperature monitoring
- Abnormal patient health alerts
- Verified HTTP patient-data transmission over GTP-U

## Technology Stack
- Open5GS — 5G Core Network
- UERANSIM — Simulated UE and gNodeB
- Python — Patient Data Simulation
- Flask — REST API
- HTML, CSS, JavaScript — Monitoring Dashboard
- tcpdump — Network Packet Analysis

## Architecture
Patient Data → 5G UE → gNodeB → Open5GS UPF → Flask API → Dashboard

The continuous patient simulator currently uses localhost.
A separate HTTP POST test was successfully transmitted through
the simulated 5G user plane and verified using GTP-U packet capture.

## Experimental Results
- UE registration: Successful
- PDU session: Established
- Average ping RTT: 2.781 ms
- Packet loss: 0% across 4 packets
- GTP-U HTTP POST transmission: Verified

Results were measured in a local software simulation,
not a physical 5G radio network.

## Running the Healthcare Application

Create a Python virtual environment and install dependencies:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install flask requests

Start the backend:

    cd backend
    python app.py

In another terminal:

    cd ~/5g-healthcare
    source .venv/bin/activate
    python sensors/patient_simulator.py

Open http://localhost:5000 in your browser.

## 5G Network

Open5GS and UERANSIM must be installed and configured separately.
Start the Open5GS core services, UERANSIM gNodeB and UE
using the configured network and subscriber settings.

## Disclaimer
This project uses simulated patient readings and a software-based
5G network. It is intended for academic demonstration only.
