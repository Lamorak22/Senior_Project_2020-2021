const axios = require('axios');

var config = {headers:{"Access-Control-Allow-Origin": "*",'Content-Type': 'application/x-www-form-urlencoded'}}


export function getWeatherData(){
    return axios.get('http://api.worldweatheronline.com/premium/v1/past-weather.ashx', 
    {params : 
        {
            q: 97601,
            date: "2010-01-01", 
            enddate: "2021-01-01",
            includelocation: "yes",
            tp: 24,
            format: "json",
            key: "0909c9292f294476aba41920211701"
        } }, config)
  .then(function (response){
    //console.log(response);
    return response.data;
  })
  .catch(function (error){
    console.log(error);
  });


}