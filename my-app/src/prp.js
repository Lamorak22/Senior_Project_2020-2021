const axios = require('axios');

var config = {headers:{"Access-Control-Allow-Origin": "*",'Content-Type': 'application/x-www-form-urlencoded'}}


export function callPRP(selected_date, zipcode, weatherJSON){
    return axios.get('http://192.168.1.43/testFlask/prp', {params : 
    { 
      date_string: selected_date, 
      zipcode_str: zipcode,
      weatherJSONdata: weatherJSON
    } }, config)
  .then(function (response){
    console.log(response);
    return response.data
  })
  .catch(function (error){
    console.log(error);
  });


}