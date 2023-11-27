import React from "react";
import { Navigate } from "react-router-dom";
import { getToken } from "../service/AuthService";

const PublicRoute = ({ children }) => {
    return (!getToken()) ? children : <Navigate to ='/dashboard'/>;
};

export default PublicRoute;
