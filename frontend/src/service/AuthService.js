// Denotes all authentication functions for a user
const BACKEND_API_ADDRESS = 'https://teqt6xqjj5.execute-api.ap-southeast-1.amazonaws.com/beta/'
const API_KEY = '7gtRwFhD5g7wpTMA3Fbyk2CvXkoPZnJR67qFELR1'

module.exports = {
    // constants
    BACKEND_API_ADDRESS: BACKEND_API_ADDRESS,
    API_KEY: API_KEY,
    
    // checks if we have a user in database
    getUser: function() {
        const user = sessionStorage.getItem('user');
        if (user === 'undefined' || !user) {
            return null;
        } else {
            return JSON.parse(user);
        }
    },

    getToken: function() {
        return sessionStorage.getItem('token');
    },
    
    getOrders: function() {
        return sessionStorage.getItem('orders');
    },

    setUserSession: function(user, token) {
        sessionStorage.setItem('user', JSON.stringify(user));
        sessionStorage.setItem('token', token);
    },

    resetUserSession: function() {
        sessionStorage.removeItem('user');
        sessionStorage.removeItem('token');
    }
}