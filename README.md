# Automate-Daily-Email-Reports

## Description

This project is a Python script that automates the process of sending daily email reports. It uses the `smtplib` and `email.mime` libraries to send emails via an SMTP server. The email content includes tasks completed, issues faced, and plans for the next day.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/aloukikjoshi/Automate-Daily-Email-Reports.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Automate-Daily-Email-Reports
    ```
3. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Update the `smtp_host`, `smtp_port`, `smtp_user`, and `smtp_password` variables in `daily_report.py` with your SMTP server details and login credentials.

2. Update the `sender` and `receiver` variables in `daily_report.py` with the sender and receiver email addresses.

3. Run the script:
    ```bash
    python daily_report.py
    ```
    The script will send an email with the daily report to the receiver email address.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details