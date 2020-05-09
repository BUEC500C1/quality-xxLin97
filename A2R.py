def arabic2roman(aNum):
  if isinstance(aranum, int): 
    if (0 < aranum < 4000): 
      aranums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
      ronums = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
      ronum = '';
      i = 0;
      while aranum > 0: 
        for _ in range(aranum//aranums[i]):
          ronum += ronums[i];
          aranum -= aranums[i];
        i += 1;
      return ronum;
    else:
      return 'Error';
  else:
    return 'Error';