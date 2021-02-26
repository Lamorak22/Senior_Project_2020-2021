const axios = require('axios');

var config = {headers:{"Access-Control-Allow-Origin": "*",'Content-Type': 'application/x-www-form-urlencoded'}}

export function waterGarden(){
    return axios.get('http://192.168.1.43/testFlask/water', config)
    .then(function (response) {
      // handle success
      return response.data
    })
    .catch(function(error){
    
      console.log(error)
    }
    );
}