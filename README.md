# RentEase: A Comprehensive Commodity Rental Platform

## Introduction
**RentEase** is a web-based solution for seamless commodity rentals. Users can sign up either as **Lenders** to list items for rent or as **Renters** to browse available commodities and place bids. The platform manages the entire lifecycle of a rental transaction—from listing, bidding, to closing deals—offering a user-friendly experience.

## Features
- **User Roles**: Sign up as a Lender or Renter.
- **Commodity Listings**: Lenders can list items with descriptions, categories, and rental terms.
- **Bidding System**: Renters can place bids on listed commodities, ensuring competitive pricing.
- **Secure Authentication**: JWT token-based authentication ensures secure login and access.
- **Rental Management**: Both Lenders and Renters can track the status of rental transactions.
- **Responsive UI**: Mobile and desktop-friendly user interfaces.

## Technology Stack
- **Backend**: Django (Python), MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: JWT Tokens
- **Deployment**: Docker

## Getting Started

### Prerequisites
- Python 3.x
- Django 4.x
- MySQL
- Docker

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/rentease.git
   cd rentease
2. Set up a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
  ```
  pip install -r requirements.txt
  ```
4. Set up the MySQL database:
  ```
  # Access MySQL and create the database
  CREATE DATABASE rentease_db;
  # Apply Django migrations
  python manage.py migrate
```
5. Run the development server:
  ```
  python manage.py runserver
  ```
6. Access the app on:
  ```
  http://127.0.0.1:8000
  ```
## Docker Setup 
  - Build and run the Docker container:
```
    docker-compose up --build
```
## API Endpoints

  - User Registration: /api/register/
  - User Login: /api/login/
  - List Commodities: /api/commodities/
  - Place Bid: /api/commodities/{id}/bid/
  - Manage Rentals: /api/rentals/

## Future Improvements

  - Integrate payment gateway for rental transactions.
  - Enable real-time notifications for bids and rental status updates.
  - Implement rating and review system for lenders and commodities.

## Contributing

- You are welcome contributions! Please fork the repository and submit a pull request for any changes.
License
## License
- This project is licensed under the MIT License.
