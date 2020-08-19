#import arabic2roman as a2r

from A2R import arabic2roman

def test_valid():               
  assert arabic2roman(1) == 'I';
  assert arabic2roman(4) == 'IV';
  assert arabic2roman(9) == 'IX';
  assert arabic2roman(59) == 'LIX';
  assert arabic2roman(94) == 'XCIV';
  assert arabic2roman(999) == 'CMXCIX';
  assert arabic2roman(1010) == 'MX';
  assert arabic2roman(3999) == 'MMMCMXCIX';
  
def test_invalid():
  assert arabic2roman('string') == 'Error'; 
  assert arabic2roman(4.2) == 'Error';    
  assert arabic2roman(-1) == 'Error';   
  assert arabic2roman(0) == 'Error';
  assert arabic2roman(4000) == 'Error';
