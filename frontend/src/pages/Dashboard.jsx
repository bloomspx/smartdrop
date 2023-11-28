// ParcelManagementPage.jsx
import React, { useEffect } from 'react';
import ParcelList from '../components/ParcelList';
import { useApi } from '../api/useApi';
import { apiClient } from '../api/apiClient';
import { getDeviceID, resetUserSession } from '../service/AuthService';

import { formatDistance, parse } from 'date-fns';
import { useNavigate } from 'react-router-dom';
import { ReactComponent as RefreshIcon } from '../icons/refresh.svg';
import Button from '../components/Button';


const calculateDays = (orderDate, deliveredDate) => {
  console.log(orderDate, deliveredDate)
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

  const handleCreateNew = () => {
    navigate('/new-delivery'); // Use the actual route for creating a new delivery
  };

  const handleLogout = () => {
    resetUserSession();
    navigate('/')
  }

  return (
    <div className="flex flex-col align-top mx-auto px-6 min-h-screen max-w-screen-lg bg-[#EBFEFA]"> {/* Adjust the background color */}
      <h1 className="text-2xl font-bold text-left py-6">SmartDrop Parcel Management</h1>
      <div className="flex justify-between gap-2">
        <div className='flex gap-2'>
          <Button className="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded" onClick={handleCreateNew}>
            Create New Delivery
          </Button>
          <Button onClick={handleLogout} className="text-white bg-red-600 hover:bg-red-700 py-2 px-4 rounded">
            Logout
          </Button>
        </div>
        <button
          onClick={() => {request(getDeviceID());}}
          className=" p-1 bg-white hover:bg-gray-100 rounded-xl"
        >
          <RefreshIcon className="w-10 h-10"/>
      </button>
    </div>
    {data && <ParcelList parcels={data.map(it => apiItemAdapte(it))} />}
  </div>
  );
};

export default ParcelManagementPage;
