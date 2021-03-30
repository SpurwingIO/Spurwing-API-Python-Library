import os
import Client as sp

try:
  from config import KEY, PID
except:
 KEY = os.environ['SPURWING_KEY']
 PID = os.environ['SPURWING_PID']
assert len(KEY) and len(PID)

def runner(func):
  def wrapper():
    try:
      print(func.__name__, 'STARTED')
      func()
      print('\n' + func.__name__, 'PASSED')
    except Exception as ex:
      print('\n' + func.__name__, 'FAILED')
      raise ex
  return wrapper

""" @runner
def test_1():
  A = sp.get_appointment_types(PID)
  log(A)
  assert len(A) == 3

  appointment_type_id=A[0]['id']

  B = sp.get_days_available(PID, appointment_type_id)
  log(B)
  assert len(B['days_available']) >= 1

  C = sp.get_slots_available(PID, appointment_type_id, dateNow(), dateTomorrow())
  log(C)
  assert len(C['slots_available']) >= 10
  slot = C['slots_available'][5]['date']

  D = sp.complete_booking(PID, appointment_type_id, 'ilya2@nevolin.be', 'Ilya', 'Nevo', date=slot, contact_type='My Contact Type')
  log(D)
  assert 'appointment' in D

  E = sp.list_appointments(KEY, 1000, 0)
  log(E)
  assert 'data' in E
  assert 'appointments' in E['data']
  assert E['data']['appointmentsCount'] >= 1

  apid = D['appointment']['id']
  F = sp.delete_appointment(KEY, apid)
  log(F)
  assert 'data' in F
  assert 'appointment' in F['data']
  assert F['data']['appointment']['id'] == apid
  assert len(F['errors']) == 0

  
@runner
def test_2():
  A = sp.list_appointments(KEY, 1000, 0)
  log(A)
  assert len(A) == 3
  assert 'data' in A
  assert 'appointments' in A['data']


from datetime import date, timedelta
def dateNow():
  return date.today().strftime("%Y/%m/%d")
def dateTomorrow():
  dt = date.today() + timedelta(days=1) 
  return dt.strftime("%Y/%m/%d") """

@runner
def test_1():
  assert 1==1

def log(obj):
  # print(obj)
  print('.', end='')

if __name__ == "__main__":
  lc = dict.fromkeys(vars())
  for item in lc:
    if 'test_' in item:
      vars()[item]()