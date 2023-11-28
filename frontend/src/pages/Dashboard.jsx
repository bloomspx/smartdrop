// ParcelManagementPage.jsx
import React, { useEffect } from 'react';
import ParcelList from '../components/ParcelList';
import { useApi } from '../api/useApi';
import { apiClient } from '../api/apiClient';
import { getDeviceID, resetUserSession } from '../service/AuthService';

import { formatDistance, parse } from 'date-fns';
import { useNavigate } from 'react-router-dom';
import { ReactComponent as RefreshIcon } from '../icons/refresh.svg';


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
  return {
    productName: item.itemName.S,
    dateOrdered: item.orderDate.S.split(',')[0],
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
  const { data, request } = useApi(apiClient.getAllOrders);
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
    <div className="min-h-screen">
      <h1 className="text-2xl font-bold text-center my-4">Parcel Management</h1>
      {data && <ParcelList parcels={data.map(it => apiItemAdapte(it))} />}
      <button onClick={handleLogout} className="text-white bg-gray-400 hover:bg-gray-600 rounded absolute bottom-0 left-0 m-4 p-4">
        Logout
      </button>
      <button
        onClick={() => {request(getDeviceID());}}
        className="absolute bottom-0 right-0 m-4 p-2 text-gray-600 hover:text-gray-800 bg-purple-200 rounded-xl"
      >
        <RefreshIcon className="w-12 h-12"/>
      </button>
    </div>
  );
};

export default ParcelManagementPage;
