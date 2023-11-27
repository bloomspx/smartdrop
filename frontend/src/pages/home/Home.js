import React, { useState } from 'react';
import axios from 'axios';
import { setUserSession, BACKEND_API_ADDRESS, API_KEY } from '../../service/AuthService';
import { useNavigate } from 'react-router-dom';

const loginUrl = BACKEND_API_ADDRESS + 'login';

const Home = () => {
    // State variables for form fields
    const [phoneNumber, setPhoneNumber] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState(null);
    const [loading, setLoading] = useState(false);
    let navigate = useNavigate()

    // Function to handle form submission
    const handleSubmit = (event) => {
        event.preventDefault();
        setLoading(true)
        setErrorMessage(null)

        const requestConfig = {
            headers: {
                'x-api-key': API_KEY
            }
        }

        const requestBody = {
            phoneNumber: phoneNumber,
            password: password,
        }
        axios.post(loginUrl, requestBody, requestConfig).then(response => {
            console.log("login response:", response.data);
            setUserSession(response.data.user, response.data.token);
            setLoading(false);
            navigate('/dashboard');
        }).catch(error => {
            // 401: user error
            setLoading(false);
            if (error.response.status === 401 || error.response.status === 403) {
                setErrorMessage(error.response.data.message);
            } else {
                setErrorMessage('Backend server is down, please try again later')
            }
        })
    };

    const onNavigatetoRegister = () => navigate(`/register`)

    return (
        <div className="container">
            <div className="header-container">
                <h1>IOT Smart Delivery Box</h1>
            </div>
            {loading && <p>Loading....</p>}
            {!loading && <form onSubmit={handleSubmit}>
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
                <button type="submit">Login</button>
            </form>}
            <button type="button" onClick={onNavigatetoRegister}>Register</button>
            {errorMessage && <p className='message'>{errorMessage}</p>}
        </div>
    );
}

export default Home