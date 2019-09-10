# Indian Bank Finder app
### URL: https://indianbankfinder.herokuapp.com 

This is a Django app build for fetching Bank branch details of the banks in India.
This app has 2 API' as following:

1. API to get a branch by IFSC code:
   URL: http://indianbankfinder.herokuapp.com/api/branch-ifsc/<here_comes the desireds IFSC code>/
   e.g. http://indianbankfinder.herokuapp.com/api/branch-ifsc/ABHY0065001/
   
   Expected status codes
   
   * '200': IFSC code found 
   * '404': IFSC code not found 

2. API to get a branch by City name and Bank name:
   URL: https://indianbankfinder.herokuapp.com/api/bank-branch/?city=<city_name>&bank=<bank name>
   e.g. https://indianbankfinder.herokuapp.com/api/bank-branch/?city=Pune&bank=state%20bank%20of%20india
   
   Expected status codes
   
   * '200': If records found for given City and Bank name
   * '404': If records not found for given City and Bank name
   * '422': City name or Bank name or both are not provided in API
 
You can access admin panel at:

https://indianbankfinder.herokuapp.com/admin

username: admin password: admin123
  
 