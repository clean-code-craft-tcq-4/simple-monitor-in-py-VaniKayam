def temp_is_ok(temperature,min,max):
  if(temperature < min or temperature > max):
     print_console("temperature")
     return False
  return True
    
def soc_is_ok(soc,min,max):
  if(soc <min or soc > max):
    print_console("State of Change")
    return False
  return True

def charge_rate_is_ok(charge_rate,min,max):
  if( charge_rate > min):
    print_console("charge rate")
    return False 
  return True


def print_console(string):
  print(string," is out of range")
  
def battery_is_ok(temperature, soc, charge_rate,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max):
    function_pointer = [temp_is_ok,soc_is_ok,charge_rate_is_ok]
    values = [temperature,soc,charge_rate]
    min_array = [temp_min,soc_min,charge_rate_min]
    max_array = [temp_max,soc_max,charge_rate_max]
    j=0
    for i in function_pointer:
        feedback = i(values[j],min_array[j],max_array[j])
        if(feedback == False ):
            return False        
        j+=1
    return True
if __name__ == '__main__':
  temp_min = 0
  temp_max = 45
  soc_min = 20
  soc_max = 80
  charge_rate_min = 0.8
  charge_rate_max = 100
  assert(battery_is_ok(25, 70, 0.7,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is True)
  assert(battery_is_ok(50, 90, 0.9,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(50, 80, 0.5,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(40, 90, 0.5,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(40, 75, 0.9,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(55, 90, 0.5,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(55, 70, 1.0,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  assert(battery_is_ok(40, 90, 0.9,temp_min,temp_max,soc_min,soc_max,charge_rate_min,charge_rate_max) is False)
  
