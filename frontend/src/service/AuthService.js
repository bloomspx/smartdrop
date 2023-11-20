// Denotes all authentication functions for a user
module.exports = {
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

    setUserSession: function(user, token, orders) {
        sessionStorage.setItem('user', JSON.stringify(user));
        sessionStorage.setItem('token', token);
    },

    resetUserSession: function() {
        sessionStorage.removeItem('user');
        sessionStorage.removeItem('token');
    }
}