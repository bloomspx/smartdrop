import React from "react";
import { Navigate } from "react-router-dom";
import { getToken } from "../service/AuthService";

const PrivateRoute = ({ children }) => {
    return getToken() ? children : <Navigate to ='/login'/>;
};

export default PrivateRoute;
