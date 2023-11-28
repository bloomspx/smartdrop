import { BrowserRouter, Routes, Route } from "react-router-dom";
import Error from "./pages/error/Error"
import Dashboard from "./pages/Dashboard";
import PublicRoute from "./routes/PublicRoute";
import PrivateRoute from "./routes/PrivateRoute";
import { useEffect, useState } from "react";
import { getToken, getUser, resetUserSession, setUserSession, BACKEND_API_ADDRESS, API_KEY } from "./service/AuthService";
import LoginPage from "./pages/LoginPage";
import RegistrationPage from "./pages/RegistrationPage";
import NewDeliveryPage from "./pages/NewDeliveryPage";
import { ToastContainer } from "react-toastify";
import { useApi } from "./api/useApi";
import { apiClient } from "./api/apiClient";

function App() {

  const { isLoading: isAuthenticating, request } = useApi(apiClient.verify);
  useEffect(() => {
    const token = getToken();
    if (token === 'undefined' || token === undefined || token === null || !token) {
      return;
    }

    request({user:getUser(), token})
    .catch( (e) => {
      console.log('Verification Failed' + e);
      resetUserSession();
    })
  }, []);

  // useEffect(() => {
  //   if (data) {
  //     console.log('Verify Success');
  //   } else {
  //     console.log('Verification Failed' + error);
  //     // resetUserSession();
  //   }
  //   console.log(data)
  // }, [isAuthenticating, data])

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
                <LoginPage/>
              </PublicRoute>
            }
          />
          <Route
            path="/register"
            element={
              <PublicRoute>
                <RegistrationPage />
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
          <Route
            path="/new-delivery"
            element={
              <PrivateRoute>
                <NewDeliveryPage/>
              </PrivateRoute>
            }
          />
          <Route path='*' element = {<Error/>}/>
        </Routes>
      </BrowserRouter>
    <ToastContainer/>
    </div>
  );
}

export default App;
