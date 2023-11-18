import React, { useState } from 'react';
import axios from 'axios';

const registerUrl = 'https://teqt6xqjj5.execute-api.ap-southeast-1.amazonaws.com/beta/register';

const Register = () => {
  // State variables for form fields
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [address, setAddress] = useState('');
  const [message, setMessage] = useState('');

  // Function to handle form submission
  const handleSubmit = (event) => {
    event.preventDefault();
    setMessage(null)
    
    const requestConfig = {
        headers: {
            'x-api-key': '7gtRwFhD5g7wpTMA3Fbyk2CvXkoPZnJR67qFELR1'
        }
    }

    const requestBody = {
        username: username,
        password: password,
        name: name,
        address: address
    }
    axios.post(registerUrl, requestBody, requestConfig).then(response => {
        setMessage('Registration Successful')
        // Reset form fields after submission
        setUsername('');
        setPassword('');
        setName('');
        setAddress('');
    }).catch(error => {
        // 401: user error
        if (error.response.status === 401) {
            setMessage(error.response.data.message);
        } else {
            setMessage('Backend server is down, please try again later')
        }
    })
  };

  return (
    <div className="register-container">
        <div className="header-container">
            <h1>Register</h1>
        </div>
        <form onSubmit={handleSubmit}>
            <label>
                Username:
                <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required/>
            </label>
            <br />

            <label>
                Password:
                <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
            </label>
            <br />

            <label>
                Name:
                <input type="text" value={name} onChange={(e) => setName(e.target.value)} required/>
            </label>
            <br />
            <label>
                Address:
                <textarea value={address} onChange={(e) => setAddress(e.target.value)} required/>
            </label>
            <br />
            <button type="submit">Register</button>
        </form>
        {message && <p className='message'>{message}</p>}
    </div>
  );
};

export default Register;
