import requests

API_URL = 'https://api.spurwing.io/api/v2/'

def get_appointment_types(provider_id, clients_can_book):
  return HTTP('GET', 'appointment_types.json',
    params = {
      'provider_id':provider_id,
      'clients_can_book': clients_can_book })

def get_days_available(provider_id, appointment_type_id, date_from_month, timezone, org_level):
  return HTTP('GET', 'bookings/days_available.json',
    params={
      'provider_id':provider_id,
      'appointment_type_id': appointment_type_id,
      'date_from_month': date_from_month,
      'timezone': timezone,
      'org_level': org_level })

def get_slots_available(provider_id, appointment_type_id, start_date, end_date, org_level):
  return HTTP('GET', 'bookings/slots_available.json',
    params = {
      'provider_id':provider_id,
      'appointment_type_id': appointment_type_id,
      'start_date': start_date,
      'end_date': end_date,
      'org_level': org_level })

def complete_booking(provider_id, appointment_type_id, date, timezone, first_name, last_name, email, phone_number, contact_type):
  return HTTP('POST', 'bookings/complete_booking.json',
    data={
      'provider_id':provider_id,
      'appointment_type_id': appointment_type_id,
      'date': date,
      'timezone': timezone,
      'first_name': first_name,
      'last_name': last_name,
      'email': email,
      'phone_number': phone_number,
      'contact_type': contact_type })

def list_appointments(authorization, page_size, offset, provider_id):
  return HTTP('GET', 'appointments',
    params={
      'page_size':page_size,
      'offset': offset,
      'provider_id': provider_id },
    headers={ 'authorization': 'Bearer ' + authorization })

def delete_appointment(appointment_id, authorization):
  return HTTP('DELETE', 'appointments/' + appointment_id, headers={ 'authorization': 'Bearer ' + authorization })


def HTTP(method, endpoint, params=None, data=None, headers=None):
  url = API_URL + endpoint
  
  if (method == 'GET'):    resp = requests.get(url,    params=params, headers=headers)
  elif method == 'POST':   resp = requests.post(url,   params=params, headers=headers, data=data,)
  elif method == 'PUT':    resp = requests.put(url,    params=params, headers=headers, data=data,)
  elif method == 'DELETE': resp = requests.delete(url, params=params, headers=headers)
  
  if resp.status_code == 200: return resp.json()
  else: raise Exception({'status':resp.status, 'text':resp.statusText, 'url':url})
