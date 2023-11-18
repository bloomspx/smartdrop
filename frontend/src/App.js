import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/home/Home"
import Register from "./pages/register/Register"
import Error from "./pages/error/Error"
import Dashboard from "./pages/dashboard/Dashboard";
import PublicRoute from "./routes/PublicRoute";
import PrivateRoute from "./routes/PrivateRoute";
import { useEffect, useState } from "react";
import { getToken, getUser, resetUserSession, setUserSession } from "./service/AuthService";
import axios from "axios";

const verifyTokenUrl = 'https://teqt6xqjj5.execute-api.ap-southeast-1.amazonaws.com/beta/verify';

function App() {

  const [isAuthenticating, setAuthenticating] = useState(true)

  // checks for validity of token
  useEffect(() => {
    const token = getToken();
    if (token === 'undefined' || token === undefined || token === null || !token) {
      return;
    }

    const requestConfig = {
      headers: {
          'x-api-key': '7gtRwFhD5g7wpTMA3Fbyk2CvXkoPZnJR67qFELR1'
      }
    }
    const requestBody = {
      user: getUser(),
      token: token
    }
    axios.post(verifyTokenUrl, requestBody, requestConfig).then(response => {
      setUserSession(response.data.user, response.data.token);
      setAuthenticating(false);
    }).catch( () => {
      resetUserSession();
      setAuthenticating(false);
    })
  }, []);

  const token = getToken();
  if (isAuthenticating && token) {
    return <div className="content">Authenticating...</div>
  }

  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <PublicRoute>
                <Home/>
              </PublicRoute>
            }
          />
          <Route
            path="/register"
            element={
              <PublicRoute>
                <Register />
              </PublicRoute>
            }/>
          <Route
            path="/dashboard"
            element={
              <PrivateRoute>
                <Dashboard/>
              </PrivateRoute>
            }
          />
          <Route path='*' element = {<Error/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
