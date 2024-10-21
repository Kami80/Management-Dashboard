# Management Dashboard

## Overview

The Management Dashboard is a web application built using Django, designed to help users manage and visualize various data efficiently. It incorporates functionalities to handle documents, spreadsheets, and PDF files, making it an essential tool for management tasks.

## Requirements

To run this project, you need to install the following Python packages:

- `asgiref==3.7.2`
- `colorama==0.4.6`
- `Django==4.2.3`
- `django-cleanup==8.0.0`
- `docx==0.2.4`
- `docx2pdf==0.1.8`
- `et-xmlfile==1.1.0`
- `lxml==4.9.3`
- `numpy==1.25.0`
- `openpyxl==3.1.2`
- `pandas==2.0.3`
- `Pillow==10.0.0`
- `PyPDF2==3.0.1`
- `python-dateutil==2.8.2`
- `python-docx==0.8.11`
- `pytz==2023.3`
- `pywin32==306`
- `six==1.16.0`
- `sqlparse==0.4.4`
- `subprocess.run==0.0.8`
- `tqdm==4.65.0`
- `typing_extensions==4.7.1`
- `tzdata==2023.3`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kami80/Management-Dashboard.git
   cd Management-Dashboard
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the Django server, run:
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to access the dashboard.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
