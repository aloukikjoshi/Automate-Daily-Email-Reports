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

## Scheduled Execution

To automate sending this email daily, you can use a task scheduler like `cron` (Linux/Mac) or Task Scheduler (Windows).

### Example using `cron` (Linux/Mac):

1. Save your Python script (`daily_report.py`) in a suitable directory.

2. Open your terminal.

3. Edit your crontab file by running:
    ```bash
    crontab -e
    ```

4. Add the following line to run the script every day at a specific time (e.g., 8:00 AM):
    ```bash
    0 8 * * * /usr/bin/python3 /path/to/your/daily_report.py
    ```
    Replace `/usr/bin/python3` with the path to your Python interpreter if it's different, and replace `/path/to/your/daily_report.py` with the actual path to your Python script.

5. Save and exit the crontab editor. Your script will now execute daily at the specified time.

### Notes:

- Make sure your SMTP server allows sending emails programmatically. Some email providers may require you to enable "less secure app access" or generate app-specific passwords.
- Handle exceptions and errors in your script to ensure robustness.
- Test your script thoroughly before deploying it in a production environment.

By following these steps, you'll have a Python script set up to automate sending daily email reports. Adjustments can be made based on your specific requirements and environment.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
