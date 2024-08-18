# Hospital Management System

## Overview

The **Hospital Management System** is a Django-based web application designed to streamline the appointment booking process in hospitals. The system enables patients to book appointments with doctors across multiple hospitals, utilizing a token system to minimize wait times and reduce the burden on hospital reception staff. 

### Key Features

- **Appointment Booking**: Patients can book appointments with doctors and receive a token number for queue management.
- **Token System**: A token-based system to reduce wait times and manage patient flow efficiently.
- **Email Notifications**: OTP verification during signup and appointment confirmation emails with details sent to patients.
- **Multi-Hospital Support**: Allows booking appointments with doctors from multiple hospitals.

## Installation

To set up and run this project locally, follow these steps:

### Prerequisites

- Python 3.x
- Django 4.x
- A virtual environment tool like `venv` or `virtualenv`
- PostgreSQL (or any other database supported by Django)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/hospital-management-system.git
   cd hospital-management-system
