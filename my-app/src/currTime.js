import React, { useState , useEffect } from 'react'

export const CurrTime = () => {

    var [date, setDate] = useState(new Date());

    useEffect(() => {
        var timer = setInterval(()=>setDate(new Date()), 1000)

        return function cleanup() {
            clearInterval(timer)
        }
    });

    return(
        <div>
            <p> Current Time: {date.toLocaleTimeString()}</p>
            <p> Date: {date.toLocaleDateString()}</p>
        </div>
    )
}

export default CurrTime