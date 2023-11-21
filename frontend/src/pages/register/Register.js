import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { BACKEND_API_ADDRESS, API_KEY } from '../../service/AuthService';

const registerUrl = BACKEND_API_ADDRESS + 'register';

const Register = () => {
  // State variables for form fields
  const [deviceID, setDeviceID] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [password, setPassword] = useState('');
  const [address, setAddress] = useState('');
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  // Function to handle form submission
  // TODO: error checking for fields (make sure they follow ther right format)


  const handleSubmit = (event) => {
    event.preventDefault();
    setLoading(true);
    setMessage(null);
    
    const requestConfig = {
        headers: {
            'x-api-key': API_KEY
        }
    }

    const requestBody = {
        deviceID: deviceID,
        phoneNumber: phoneNumber,
        password: password,
        address: address
    }
    axios.post(registerUrl, requestBody, requestConfig).then(response => {
        setLoading(false);
        setMessage('Registration is successful, you will be redirected to login in 5s...')
        // Reset form fields after submission
        setDeviceID('');
        setPhoneNumber('');
        setPassword('');
        setAddress('');
        setTimeout(() => {
            navigate('/')
          }, 5000)
    }).catch(error => {
        setLoading(false);
        // 401: user error
        if (error.response.status === 401) {
            setMessage(error.response.data.message);
        } else {
            setMessage('Backend server is down, please try again later')
        }
    })
  };

  return (
    <div className="container">
        <div className="header-container">
            <h1>Register</h1>
        </div>
        {loading && <p>Loading....</p>}
        {!loading && <form onSubmit={handleSubmit}>
            <label>
                Device ID:
                <input type="text" value={deviceID} onChange={(e) => setDeviceID(e.target.value)} required/>
            </label>
            <br />

            <label>
                Phone Number:
                <input type="text" value={phoneNumber} onChange={(e) => setPhoneNumber(e.target.value)} required/>
            </label>
            <br />

            <label>
                Password:
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
            </label>
            <br />
            <label>
                Address:
                <textarea value={address} onChange={(e) => setAddress(e.target.value)} required/>
            </label>
            <br />
            <button type="submit">Register</button>
        </form>}
        {message && <p className='message'>{message}</p>}
    </div>
  );
};

export default Register;
