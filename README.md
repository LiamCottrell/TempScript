# TempScript: Temperature Data Processor

## Description
This application processes `.dat` files to extract temperature data and saves it in a `.csv` file. 

## Prerequisites
- Python 3.x
- Pip package manager
- Virtual Environment (Optional but recommended)

## Installation
Clone the repository to your local machine:

(Optional) Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration

Copy the example `.env` file to create your own configuration.

```bash
cp .env.example .env
```

Edit the `.env` file to set the required configuration values:

```
# .env
DAT_DIRECTORY="path/to/dat/files"
CSV_FILENAME="temperature_log.csv"
FILE_EXTENSION=".dat"
TEMP_PREFIX="TEMP"
```

## Usage

Run the script:

```bash
python src/your_app/main.py
```
This will process all `.dat` files in the configured directory and generate a `.csv` file with the extracted temperature data.

## Running Tests
To run tests, execute:

```bash
pytest
```