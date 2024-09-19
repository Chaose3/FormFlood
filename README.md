# Google Form Flooder

A Python script to automate submissions to Google Forms using Burp Suite.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Chaose3/FormFlood.git
    cd FormFlood
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Replace the Google Form link on line 4 of the script with your form's URL.
2. Launch **Burp Suite** and enable monitoring.
3. Visit your Google Form, fill in any fields (e.g., multiple-choice questions), and submit the form.
4. In Burp Suite, forward the requests until you reach the form submission request (typically around line 24).
5. Look for the `entry.something=value` fields in the request, where `something` represents each question.
6. Use the numbers from Burp Suite in your script, starting from line 8 onwards.

### Example

If Burp Suite shows:

```text
entry.123456=name1&entry.1294434&entry.654321=name2

\'\'\'
