import React, { useState, useEffect } from 'react'
import Calendar from 'react-calendar'
import './App.css'
import logo from './plant.png'
import loadgif from './plantgif.gif'
import CurrTime from './currTime'

import Button from 'react-bootstrap/Button'
import Table from 'react-bootstrap/Table'
import Image from 'react-bootstrap/Image'
import Form from 'react-bootstrap/Form'

import { fetch_sensor_data } from './app_client.js';
import { callPRP } from './prp.js';
import { waterGarden } from './waterGarden.js'



function App() {
  var caldate;

  //useState to update the date on the calendar per user input
  const [calendarVal, changeDate] = useState(new Date());

  //Get Zipcode from text box

    /********************************************************************
   * Function: updateField
   * 
   * Purpose: When the user types into the zipcode box, the function
   *  will update the data in the state variable
   * 
   * input: user keyboard input
   * 
   * output: None
  **************************************************************/
  const [inputZipcode, updateZip] = useState("")
  function updateField(event) {
      //console.log(event.target.value);
      updateZip(event.target.value)
    };


  /********************************************************************
   * Function: clickHandler
   * 
   * Purpose: Once a date and zipcode are selected/entered, this function
   *  will call the plant recommendation program from the Flask API
   * 
   * input: selected date and zipcode
   * 
   * output: array of vegetables that were deemed "good to plant"
  **************************************************************/

    //Data for plant recommendation program
    const [prpdata, setprpdata] = useState("");

  async function clickHandler(){
      
      caldate = calendarVal.toLocaleDateString();
      const data = await callPRP(caldate, inputZipcode);
      console.log("data: ", data);

      //Format prpdata
      var i;
      var prpresults = "";
      for (i = 0; i < data.prp.length; i++){
        if (data.prp.length - 1 === i){
          prpresults += "and " + data.prp[i];
        }
        else {
          prpresults += data.prp[i] + ", ";
        }  
      }
      prpresults += " are all options to plant based on the historical weather data of the date chosen."
      setprpdata(prpresults);
  }


  //GET request for sensor data
  const [stateData, setStateData] = useState({});
    useEffect(() => {
      setLoading(loadgif);
      fetch_sensor_data().then((data) => {
        setStateData(data);
      });
      }, []);
  
      
    /********************************************************************
   * Function: waterHandler
   * 
   * Purpose: This function will be called at a certain time each day.
   *  When it is called, a request will be made to the Flask API
   *  to open the solenoid valve and water the garden.
   * 
   * input: Time of day
   * 
   * output: Will water the garden with solenoid valve.
  **************************************************************/
 useEffect(() => {
  const timer = setInterval(() =>{
    caldate = calendarVal.toLocaleTimeString();
    console.log(caldate[0]);
    var ampm = caldate.slice(-2)
    console.log(ampm)
    if (caldate[0] === "9" && ampm === "PM"){
      waterHandler();
    }
  }, 60000);

  return () => clearInterval(timer);
 });

  function waterHandler(){
    waterGarden().then((data) => {
      console.log(data);
    });
  }
  

  const [loading, setLoading] = useState({});
 

  return (
  <div className="App">

    {/*Flex box for the plant image and other webpage headers*/}
    <div className="wrappingimage">
      <Image src={logo} alt="Plant" class="img-fluid" width="396" height="395"/>
      <Image src={loading} alt="Plantgif" class="img-fluid" width="396" height="395"/>
      <div className="imagetext">
      <div>Automated Garden Webpage</div>
      <div>Creator: Daniel Eberhart</div>
      <CurrTime></CurrTime>
      </div>
    </div>     
      
      {/*Table to hold all sensor data retrieved from Flask API*/}
    <h2>Sensor Table</h2>
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
          <td>Humidity Sensor</td>
          <td>{stateData.humidity}</td>

        </tr>
      </tbody>
    </Table>
  </div>

    {/*Flex box that holds all assets of the plant recommendation program*/}
    <h2>Plant Recommendation Program</h2>

  <prp>
    <div class="calendar">
    <Calendar
      onChange={changeDate}
      value={calendarVal}
      /> 
    </div>


    <div class="textentry">
    <Form>
      <Form.Group>
      <Form.Control 
      placeholder="Enter Zipcode"
      value={inputZipcode}
      onChange={updateField}
      />
      </Form.Group>
    </Form>

    <Button 
      variant="secondary"
      size="lg"
      onClick={clickHandler}
      >
        Submit
      </Button>
    </div>


    <div class="prpoutput">
      <p>{prpdata}</p>
    </div>

    <div class="chooseplant">
      <Form>
        <Form.Group>
          <Form.Label column="lg">Select what to plant </Form.Label>
          <Form.Control as="select" size="sm" custom>
            <option value="0">Basil</option>
            <option value="1">Beet</option>
            <option value="2">Beetroot</option>
            <option value="3">Bell Pepper</option>
            <option value="4">Broccoli</option>
            <option value="5">Cabbage</option>
            <option value="6">Carrot</option>
            <option value="7">Cauliflower</option>
            <option value="8">Celery</option>
            <option value="9">Cucumber</option>
            <option value="10">Green Bean</option>
            <option value="11">Kale</option>
            <option value="12">Lettuce</option>
            <option value="13">Mint</option>
            <option value="14">Onion</option>
            <option value="15">Pea</option>
            <option value="16">Potato</option>
            <option value="17">Radish</option>
            <option value="18">Red Pepper</option>
            <option value="19">Romaine</option>
            <option value="20">Spinach</option>
            <option value="21">Squash</option>
            <option value="22">Tomato</option>
            <option value="23">Zucchini</option>
          </Form.Control>
        </Form.Group>
      </Form>


    </div>
  </prp>

    
    <div>
    <Button 
      variant="secondary"
      size="sm"
      onClick={waterHandler}
      >
        WATER
      </Button>
    </div>
    
  </div>
  );
}

export default App;
