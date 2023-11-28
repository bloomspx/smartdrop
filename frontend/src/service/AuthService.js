// Denotes all authentication functions for a user
export const BACKEND_API_ADDRESS = 'https://teqt6xqjj5.execute-api.ap-southeast-1.amazonaws.com/beta/'
export const API_KEY = 'iMtIKmjyeD5UcQk1Ar6Od3VcfEs1c5Qm3Q8HcmuW'

// checks if we have a user in database
export const getUser = () => {
    const user = sessionStorage.getItem('user');
    if (user === 'undefined' || !user) {
        return null;
    } else {
        return JSON.parse(user);
    }
}

export const getDeviceID = () => {
    return getUser()?.deviceID;
}

export const getToken = () => {
    return sessionStorage.getItem('token');
}

export const getOrders = () => {
    return sessionStorage.getItem('orders');
}

export const setUserSession = (user, token) => {
    sessionStorage.setItem('user', JSON.stringify(user));
    sessionStorage.setItem('token', token);
}

export const resetUserSession = () => {
    sessionStorage.removeItem('user');
    sessionStorage.removeItem('token');
}