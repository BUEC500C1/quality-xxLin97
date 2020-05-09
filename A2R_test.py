import arabic2roman as a2r

def test_valid():               
  assert a2rr.arabic2roman(1) == 'I';
  assert a2r.arabic2roman(4) == 'IV';
  assert a2r.arabic2roman(9) == 'IX';
  assert a2r.arabic2roman(59) == 'LIX';
  assert a2r.arabic2roman(94) == 'XCIV';
  assert a2r.arabic2roman(999) == 'CMXCIX';
  assert a2r.arabic2roman(1010) == 'MX';
  assert a2r.arabic2roman(3999) == 'MMMCMXCIX';
  
def test_invalid():
  assert a2r.arabic2roman('string') == 'Error'; 
  assert a2r.arabic2roman(4.2) == 'Error';    
  assert a2r.arabic2roman(-1) == 'Error';   
  assert a2r.arabic2roman(0) == 'Error';
  assert a2r.arabic2roman(4000) == 'Error';