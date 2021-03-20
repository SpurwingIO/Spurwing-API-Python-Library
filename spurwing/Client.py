import requests

API_URL = 'https://api.spurwing.io/api/v2/'

def get_appointment_types(provider_id=None, page_size=None, offset=None):
  return HTTP('GET', 'appointment_types.json',
    params = {
      'provider_id':provider_id,
      'page_size': page_size,
      'offset': offset })

def get_days_available(provider_id, appointment_type_id, date_from_month=None, organization_level=None, timezone=None):
  return HTTP('GET', 'bookings/days_available.json',
    params={
      'provider_id':provider_id,
      'appointment_type_id': appointment_type_id,
      'date_from_month': date_from_month,
      'timezone': timezone,
      'organization_level': organization_level })

def get_slots_available(provider_id, appointment_type_id, start_date, end_date, organization_level=None, timezone=None):
  return HTTP('GET', 'bookings/slots_available.json',
    params = {
      'provider_id':provider_id,
      'appointment_type_id': appointment_type_id,
      'start_date': start_date,
      'end_date': end_date,
      'timezone': timezone,
      'organization_level': organization_level })

def complete_booking(provider_id, appointment_type_id, email, first_name, last_name, date=None, contact_type=None, appointment_id=None, appointment_location_id=None, timezone=None, video_chat_url=None):
  return HTTP('POST', 'bookings/complete_booking.json',
    data={
      'provider_id':provider_id,
      'appointment_type_id': appointment_type_id,
      'date': date,
      'timezone': timezone,
      'first_name': first_name,
      'last_name': last_name,
      'email': email,
      'appointment_id': appointment_id,
      'appointment_location_id': appointment_location_id,
      'video_chat_url': video_chat_url,
      'contact_type': contact_type })

def list_appointments(authorization, page_size, offset, appointment_category=None, load_attendees=None, load_providers=None, load_appointment_type=None):
  return HTTP('GET', 'appointments',
    params={
      'page_size':page_size,
      'offset': offset,
      'appointment_category': appointment_category,
      'load_attendees': load_attendees,
      'load_providers': load_providers,
      'load_appointment_type': load_appointment_type },
    headers={ 'authorization': 'Bearer ' + authorization })

def delete_appointment(authorization, appointment_id):
  return HTTP('DELETE', 'appointments/' + appointment_id, headers={ 'authorization': 'Bearer ' + authorization })


def HTTP(method, endpoint, params=None, data=None, headers=None):
  url = API_URL + endpoint
  
  if (method == 'GET'):    resp = requests.get(url,    params=params, headers=headers)
  elif method == 'POST':   resp = requests.post(url,   params=params, headers=headers, data=data,)
  elif method == 'PUT':    resp = requests.put(url,    params=params, headers=headers, data=data,)
  elif method == 'DELETE': resp = requests.delete(url, params=params, headers=headers)

  if resp.status_code == 200: return resp.json()
  else: raise Exception({'status':resp.status, 'text':resp.statusText, 'url':url})
