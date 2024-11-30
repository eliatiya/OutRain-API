# Drive Status and Weather API Service

This project provides two main services: 
1. **Drive Status API** - Fetches the status of drives including details such as name, size, free space, and other metadata. 
2. **Weather API** - Fetches weather information for a specified location .

Both services are containerized using Docker for easy deployment.

## Features

- **Drive Status API**:
  - Fetch drive status filtered by `online` or `offline`.
  - Outputs drive details including size, free space, log size, path, etc.
  
- **Weather API**:
  - Fetch weather details for a given location.

- **Containerized with Docker** for easy deployment.

## Requirements

- Python 3.9 or later
- Docker (optional, for containerized setup)
- Flask and other dependencies defined in `requirements.txt`

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/drive-status-weather-api.git
cd drive-status-weather-api
```

In app/weather_service.py file add to API_KEY var KEY

### 2. Build the Docker container:

```
sudo docker build -t weather-drive-api .
```

### 3. Run the Docker container:

```
sudo docker run -it -p 5000:5000 weather-drive-api
```

## Example Requests

### Check Current Weather:

```
curl -X GET http://localhost:5000/v1/api/checkCurrentWeather
```

### Check Weather for City:

```
curl -X GET "http://localhost:5000/v1/api/checkCityWeather?city=Tel-Aviv"
```

### Post Drive Status:

```
curl -X POST -H "Content-Type: application/json" -d @input.json http://localhost:5000/v1/api/driveStatus
```

### Get Drive Status by Filter:

```
curl -X GET "http://localhost:5000/v1/api/driveStatus?status=offline"
```
