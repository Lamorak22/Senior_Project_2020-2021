import React, { useState, useEffect } from 'react';
import Calendar from 'react-calendar'
import './App.css';
import { fetch_sensor_data } from './app_client.js';
import { callPRP } from './prp.js';
import logo from './plant.png'

import Button from 'react-bootstrap/Button'
import Table from 'react-bootstrap/Table'
import Image from 'react-bootstrap/Image'
import Form from 'react-bootstrap/Form'

import CurrTime from './currTime'
import { getWeatherData } from './weatherAPI';




function App() {
  var caldate;

  //Calendar
  const [calendarVal, changeDate] = useState(new Date());

  const [inputZipcode, updateZip] = useState("")

  function updateField(event) {
      console.log(event.nativeEvent.data);
      updateZip(inputZipcode + event.nativeEvent.data)
    };


  //PRP
  const [prpdata, setprpdata] = useState({});

  const [weatherdata, setweatherdata] = useState({});

  function clickHandler(){

    getWeatherData().then((data) => {
      console.log(data.data.weather[0]);
      setweatherdata(data);
      console.log(weatherdata.data.weather[0])
  })

    caldate = calendarVal.toLocaleDateString();
    callPRP(caldate, inputZipcode, weatherdata.data.weather[0]).then((data) => {
      setprpdata(data);
    })
    
    


  }

  //GET request for sensor data
  const [stateData, setStateData] = useState({});
    useEffect(() => {
      fetch_sensor_data().then((data) => {
        setStateData(data);
      });
      }, []);
      
  
  
  return (
  <div className="App">
    <div class="wrappingimage">
      <Image src={logo} alt="Plant" class="img-fluid" width="396" height="395"/>
      
      </div>
      <p>Automated Garden Webpage<br/>
        Creator: Daniel Eberhart
      </p>
      
      <h2>Sensor Table</h2>
      <h2>Last updated: {stateData.date}</h2>
      
    <CurrTime></CurrTime>
    <div>
    <Button variant="primary" size="sm">
      Refresh Sensor Data
    </Button>{' '}
    </div>
  <div>
    <Table striped bordered hover variant="dark" size="sm">
      <thead>
        <tr>
          <th>Sensor</th>
          <th>Value</th>

        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Soil Humidity Sensor</td>
          <td>{stateData.resultsms}</td>

        </tr>
        <tr>
          <td>Temperature Sensor</td>
          <td>{stateData.tempC} °C/ {stateData.tempF} °F</td>

        </tr>
        <tr>
          <td>Light Sensor</td>
          <td>{stateData.ldr}</td>

        </tr>
        <tr>
          <td>Humididty Sensor</td>
          <td>{stateData.humidity}</td>

        </tr>
      </tbody>
    </Table>
  </div>


  <div class="calendarwrapper">
    <Calendar
      onChange={changeDate}
      value={calendarVal}
      /> 
    <Button 
    variant="secondary"
    size="sm"
    onClick={clickHandler}
    >
      Submit
    </Button> 
    <p>prp data:{prpdata?.data}</p>
  </div>

    <div class="text_entry">
    <Form>
      <Form.Group>
      <Form.Control 
      placeholder="Enter Zipcode"
      value={inputZipcode}
      onChange={updateField}
      />
      
      
      </Form.Group>
    </Form>

      <p>form: {inputZipcode}</p>
    </div>

    
  </div>
  );
}

export default App;
