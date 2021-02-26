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
        <div>Current Time: {date.toLocaleTimeString()}</div>
        <div>Date: {date.toLocaleDateString()}</div>
        </div>
    )
}

export default CurrTime