import React, { useState } from 'react';
import axios from 'axios';
import { setUserSession } from '../../service/AuthService';
import { useNavigate } from 'react-router-dom';

const loginUrl = 'https://teqt6xqjj5.execute-api.ap-southeast-1.amazonaws.com/beta/login';


const Login = (props) => {
  // State variables for form fields
  const [username, setUsername] = useState('');
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
                'x-api-key': '7gtRwFhD5g7wpTMA3Fbyk2CvXkoPZnJR67qFELR1'
            }
        }

        const requestBody = {
            username: username,
            password: password,
        }
        axios.post(loginUrl, requestBody, requestConfig).then(response => {
            console.log(response);
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

  return (
    <div className="register-container">
        <div className="header-container">
            <h1>Login</h1>
        </div>
        {loading && <p>Loading....</p>}
        {!loading && <form onSubmit={handleSubmit}>
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
            <button type="submit">Login</button>
        </form>}
        {errorMessage && <p className='message'>{errorMessage}</p>}
    </div>
  );
};

export default Login;
