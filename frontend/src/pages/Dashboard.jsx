// ParcelManagementPage.jsx
import React, { useEffect } from 'react';
import ParcelList from '../components/ParcelList';
import { useApi } from '../api/useApi';
import { apiClient } from '../api/apiClient';
import { getDeviceID, resetUserSession } from '../service/AuthService';

import { formatDistance, parse } from 'date-fns';
import { useNavigate } from 'react-router-dom';

const mockData = [
  {
      "orderDate": {
          "S": "11/21/2023, 4:27:25 PM"
      },
      "deliveredDate": {
          "S": ""
      },
      "imageURL": {
          "S": "https://wonderfulengineering.com/wp-content/uploads/2014/10/image-wallpaper-15.jpg"
      },
      "deviceID": {
          "S": "test"
      },
      "isDelivered": {
          "BOOL": true
      },
      "passcode": {
          "S": "228477"
      },
      "itemName": {
          "S": "aaa"
      },
      "shopName": {
          "S": "aaa"
      }
  },
  {
      "orderDate": {
          "S": "11/21/2023, 4:16:37 PM"
      },
      "deliveredDate": {
          "S": ""
      },
      "imageURL": {
          "S": ""
      },
      "deviceID": {
          "S": "test"
      },
      "isDelivered": {
          "BOOL": false
      },
      "passcode": {
          "S": "834119"
      },
      "itemName": {
          "S": "shopeee"
      },
      "shopName": {
          "S": "shopeee"
      }
  }
]

const calculateDays = (orderDate, deliveredDate) => {
  const formatString = 'MM/dd/yyyy, hh:mm:ss a';
  const startDate = parse(orderDate, formatString, new Date());

  let endDate;
  if (deliveredDate && deliveredDate !== '') {
    endDate = parse(deliveredDate, formatString, new Date());
  } else {
    endDate = new Date(); // Use current date if deliveredDate is not available
  }

  return formatDistance(startDate, endDate, { addSuffix: true });
};


const apiItemAdapte = (item) => {
  return  {
    productName: item.itemName.S,
    dateOrdered: item.orderDate.S,
    dateDelivered: item.deliveredDate.S,
    imageSrc: item.imageURL.S,
    deviceID: item.deviceID.S,
    isDelivered: item.isDelivered.BOOL,
    passcode: item.passcode.S,
    orderedFrom: item.shopName.S,
    days: calculateDays(item.orderDate.S, item.deliveredDate.S),
  }
}

const ParcelManagementPage = () => {
  const {data, request} = useApi(apiClient.getAllOrders);
  const navigate = useNavigate()

  useEffect(() => {
    request(getDeviceID());
    // const interval = setInterval(() => {
    //   request(getDeviceID());
    // }, 60000); // Adjust interval as needed, e.g., 60000 for 1 minute

    // return () => clearInterval(interval);
  }, []);

  const handleLogout = () => {
    resetUserSession();
    navigate('/')
  }

  return (
    <div className="min-h-screen bg-[#EBFEFA]"> {/* Adjust the background color */}
      <h1 className="text-2xl font-bold text-center my-4">Parcel Management</h1>
      {data && <ParcelList parcels={data.map(it => apiItemAdapte(it))} />}
      <button onClick={handleLogout} className="text-white bg-gray-400 hover:bg-gray-600 rounded absolute bottom-0 left-0 m-4 p-4">
        Logout
      </button>
    </div>
  );
};

export default ParcelManagementPage;
