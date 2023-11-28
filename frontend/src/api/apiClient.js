import { API_KEY } from "../service/AuthService";
const BASE_URL = 'https://woqp7vxlb1.execute-api.ap-southeast-1.amazonaws.com/beta';
// const BASE_URL = 'https://teqt6xqjj5.execute-api.ap-southeast-1.amazonaws.com/beta'

async function callApi(endpoint, method, data) {
  const url = `${BASE_URL}/${endpoint}`;
  const options = {
    method,
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': API_KEY
    },
    body: JSON.stringify(data),
  };
  const response = await fetch(url, options);
  if (!response.ok) {
    throw new Error(`API call failed: ${response.status}`);
  }
  return response.json();
}

export const apiClient = {
  register: (userData) => callApi('register', 'POST', userData),
  login: (credentials) => callApi('login', 'POST', credentials),
  verify: (verificationData) => callApi('verify', 'POST', verificationData),
  getAllOrders: (deviceID) => callApi('getallorders', 'POST', { deviceID }),
  newOrder: (orderData) => callApi('neworder', 'POST', orderData),
};

