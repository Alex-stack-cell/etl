# ETL Data Processing Project

## Overview

This project implements an Extract, Transform, Load (ETL) pipeline to process data from multiple file formats and prepare it for database loading.

## Goal

This script aims to:

- Read CSV, JSON, and XML file types
- Extract the required data from different file types
- Transform data to the required format
- Save the transformed data in a ready-to-load format, which can be loaded into an RDBMS

## Features

- **Multi-format support**: Handles CSV, JSON, and XML files
- **Data transformation**: Converts data to standardized format
- **Logging**: Comprehensive logging of ETL operations
- **Output generation**: Creates transformed data in CSV format

## Prerequisites

- Python 3.7+
- pandas library
- Virtual environment (recommended)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Alex-stack-cell/etl.git
   cd etl
   ```

2. **Extract the source data:**

   ```bash
   unzip source.zip
   ```

   This will extract the following files:

   - `source1.csv`, `source1.json`, `source1.xml`
   - `source2.csv`, `source2.json`, `source2.xml`
   - `source3.csv`, `source3.json`, `source3.xml`

3. **Create and activate virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

4. **Install dependencies:**
   ```bash
   pip install pandas
   ```

## Usage

1. **Ensure virtual environment is activated:**

   ```bash
   source venv/bin/activate
   ```

2. **Run the ETL script:**

   ```bash
   python3 etl.py
   ```

3. **Check the output:**
   - Transformed data will be saved to `transformed_data.csv`
   - Logs will be written to `log_file.txt`

## File Structure

```
etl/
├── etl.py                 # Main ETL script
├── source.zip             # Compressed source data files
├── transformed_data.csv   # Output transformed data
├── log_file.txt          # ETL operation logs
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

**Note:** After extracting `source.zip`, you'll have access to:

- `source1.csv`, `source1.json`, `source1.xml`
- `source2.csv`, `source2.json`, `source2.xml`
- `source3.csv`, `source3.json`, `source3.xml`

## Output

The script generates:

- **transformed_data.csv**: Clean, standardized data ready for database loading
- **log_file.txt**: Detailed log of all ETL operations with timestamps

## Data Format

The transformed data includes:

- **name**: Person's name
- **height**: Height in meters
- **weight**: Weight in kilograms

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is part of the IBM Python for Data Engineering course.

## Author

Alex Stack Cell
