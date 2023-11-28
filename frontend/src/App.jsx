import { useEffect } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import { apiClient } from "./api/apiClient";
import { useApi } from "./api/useApi";
import Dashboard from "./pages/Dashboard";
import Error from "./pages/Error";
import LoginPage from "./pages/LoginPage";
import NewDeliveryPage from "./pages/NewDeliveryPage";
import RegistrationPage from "./pages/RegistrationPage";
import PrivateRoute from "./routes/PrivateRoute";
import PublicRoute from "./routes/PublicRoute";
import { getToken, getUser, resetUserSession } from "./service/AuthService";

function App() {

  const { isLoading: isAuthenticating, request } = useApi(apiClient.verify);
  useEffect(() => {
    const token = getToken();
    if (token === 'undefined' || token === undefined || token === null || !token) {
      return;
    }

    request({ user: getUser(), token })
      .catch((e) => {
        console.log('Verification Failed: ' + e);
        resetUserSession();
      })
  }, []);

  if (isAuthenticating) {
    return <div className="content">Authenticating...</div>
  }

  return (
    <div className="App bg-[#EBFEFA]">
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <PublicRoute>
                <LoginPage />
              </PublicRoute>
            }
          />
          <Route
            path="/register"
            element={
              <PublicRoute>
                <RegistrationPage />
              </PublicRoute>
            } />
          <Route
            path="/dashboard"
            element={
              <PrivateRoute>
                <Dashboard />
              </PrivateRoute>
            }
          />
          <Route
            path="/new-delivery"
            element={
              <PrivateRoute>
                <NewDeliveryPage />
              </PrivateRoute>
            }
          />
          <Route path='*' element={<Error />} />
        </Routes>
      </BrowserRouter>
      <ToastContainer />
    </div>
  );
}

export default App;
