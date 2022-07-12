def temp_is_ok(temperature):
  if(temperature < 0 or temperature > 45):
     print_console("temperature")
     return False
  return True
    
def soc_is_ok(soc):
  if(soc <20 or soc > 80):
    print_console("State of Change")
    return False
  return True

def charge_rate_is_ok(charge_rate):
  if(charge_rate > 0.8):
    print_console("charge rate")
    return False 
  return True


def print_console(string):
  print(string," is out of range")
  
def battery_is_ok(temperature, soc, charge_rate):
    function_pointer = [temp_is_ok,soc_is_ok,charge_rate_is_ok]
    values = [temperature,soc,charge_rate]
    j=0
    for i in function_pointer:
        feedback = i(values[j])
        if(feedback == False ):
            return False        
        j+=1
    return True
if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 90, 0.9) is False)
  assert(battery_is_ok(50, 80, 0.5) is False)
  assert(battery_is_ok(40, 90, 0.5) is False)
  assert(battery_is_ok(40, 75, 0.9) is False)
  assert(battery_is_ok(55, 90, 0.5) is False)
  assert(battery_is_ok(55, 70, 1.0) is False)
  assert(battery_is_ok(40, 90, 0.9) is False)
  
