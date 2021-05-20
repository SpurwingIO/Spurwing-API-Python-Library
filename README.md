# Spurwing API Python Library

Lightweight Python library for Spurwing's API.

Spurwing's API makes it easy to add robust scheduling and booking to your application. We power millions of appointment bookings for thousands of companies, from marketplaces to SaaS & healthcare. 

![image](https://user-images.githubusercontent.com/9488406/119051697-c8968100-b9c3-11eb-8e5b-b40cb0007c91.png)

## Account
To use this API you need to obtain API credentials by signin up here: https://spurwing.io/

On your dashboard you will have the "API Info" page with your **API key** and **Provider ID**.

- **API Key:** This is your private API Key used for private and authorized operations.

- **Provider ID:** This is your public calendar identifier.

**Security Warning:** Never expose your **API Key** in front-end javascript code. All implementations that require your API Key should be handled by your back-end in a secure environment.

## Usage
You can use pip to install the library: `pip install spurwing`

If you use another method, make sure to install the dependencies: `pip install -r requirements.txt`

You can use it as such:
```py
from spurwing import Client as sp

PID = 'your_provider_id';
KEY = 'your_api_key';

A = sp.list_appointments(KEY)

```
## Documentation

The currently implemented API functions and features are:

- get_appointment_types
- get_days_available
- get_slots_available
- complete_booking
- create_group_appointment
- list_appointments
- delete_appointment

For additional demos and use cases have a look under `spurwing/test_api.py`.

Spurwing's REST API Reference and Docs: https://docs.spurwing.io/

## Testing
To run our predefined unit tests use the `spurwing/test_api.py` script.

You also need to provide the API credentials. You can use environment variables, or rename the `config.sample.py` file to `config.py` and enter your credentials (provider id and api key). Afterwards you can run the `npm tests` command. You can optionally use PyTest or another framework.

Environment variables:
```
SPURWING_PID=change_me
SPURWING_KEY=change_me
```

## Support
- For public issues and bugs please use the GitHub Issues Page.
- For enquiries and private issues reach out to us at support@spurwing.io
- Join our Discord Community Server: https://discord.gg/j3gd5Qk5uW
