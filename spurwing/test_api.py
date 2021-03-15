from config import KEY, PID
import Client as sp

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

@runner
def test_1():
  tz = "Europe/Brussels";

  A = sp.get_appointment_types(PID, True)
  log(A)
  assert len(A) == 3

  B = sp.get_days_available(PID, A[0]['id'], dateNow(), tz, False)
  log(B)
  assert len(B['days_available']) >= 1

  C = sp.get_slots_available(PID, A[0]['id'], dateNow(), dateTomorrow(), False)
  log(C)
  assert len(C['slots_available']) >= 10
  slot = C['slots_available'][5]['date']

  D = sp.complete_booking(PID, A[0]['id'], slot, tz, 'Ilya', 'Nevo', 'ilya2@nevolin.be', '111-111-7777', 'My Contact Type')
  log(D)
  assert 'appointment' in D

  E = sp.list_appointments(KEY, 1000, 0, PID)
  log(E)
  assert 'data' in E
  assert 'appointments' in E['data']
  assert E['data']['appointmentsCount'] >= 1

  apid = D['appointment']['id']
  F = sp.delete_appointment(apid, KEY)
  log(F)
  assert 'data' in F
  assert 'appointment' in F['data']
  assert F['data']['appointment']['id'] == apid
  assert len(F['errors']) == 0

  
@runner
def test_2():
  A = sp.list_appointments(KEY, 1000, 0, PID)
  log(A)
  assert len(A) == 3
  assert 'data' in A
  assert 'appointments' in A['data']


from datetime import date, timedelta
def dateNow():
  return date.today().strftime("%Y/%m/%d")
def dateTomorrow():
  dt = date.today() + timedelta(days=1) 
  return dt.strftime("%Y/%m/%d")

def log(obj):
  # print(obj)
  print('.', end='')

if __name__ == "__main__":
  lc = dict.fromkeys(vars())
  for item in lc:
    if 'test_' in item:
      vars()[item]()