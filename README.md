# HotelStay

## Overview
This project creates a custom app in ChatGPT that allows users to search for places to stay based on the city provided. The app utilizes a JSON data file containing various hotels, including details such as the cities, amenities, and price per night.

## Project Structure
- **web/**: Contains the frontend application built with React and TypeScript.
- **server/**: Contains the backend application built with Python.
- **data/**: Includes JSON data files used in the application.

## Getting Started
### Prerequisites
- Node.js and npm for the frontend.
- Python 3.x for the backend.

### Setup

- Check [https://developers.openai.com/apps-sdk/deploy/connect-chatgpt](https://developers.openai.com/apps-sdk/deploy/connect-chatgpt) for instructions on testing the app in ChatGPT.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd listo-technical-exercise
   ```
2. Install frontend dependencies:
   ```bash
   cd web
   npm install
   ```
3. Install backend dependencies:
   ```bash
   cd server
   pip install -r requirements.txt
   ```

### Running the Application
- Start the backend server:
   ```bash
   python app.py
   ```
- Start the frontend application:
   ```bash
   cd web
   npm install
   npm run build
   ```

## License
This project is licensed under the MIT License.
