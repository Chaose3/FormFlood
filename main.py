import requests

# Google Form submission URL
form_url = 'Insert link Here'

# Form data captured from BurpSuite
form_data = {
    'entry.325547176': 'Elysse Champion',       # Selecting Elysse Champion
    'entry.1013163851': 'Danny Winnerkrans',    # Selecting Danny Winnerkrans
    'entry.325547176_sentinel': '',             # Sentinel value (may be empty)
    'entry.1013163851_sentinel': '',            # Sentinel value (may be empty)
    'fvv': '1',                                 # fvv parameter from the proxy
    'partialResponse': '[null,null,"161857952453305933"]',  # Partial response data
    'pageHistory': '0',                         # Page history parameter
    'fbzx': '161857952453305933',               # Unique identifier, could change on refresh
    'submissionTimestamp': '1726603733666'      # Timestamp when the form was submitted
}

# Send the form submission request
response = requests.post(form_url, data=form_data)

# Check if the submission was successful
if response.status_code == 200:
    print('Form submitted successfully!')
else:
    print(f'Failed to submit form. Status code: {response.status_code}')
