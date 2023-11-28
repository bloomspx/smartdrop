// ParcelManagementPage.jsx
import React from 'react';
import ParcelList from '../components/ParcelList';

const Dashboard = () => {
  // Replace with the mockParcels data
  const mockParcels = [
  {
    id: 1,
    productName: 'Raspberry Pi 4GB Model B Kit',
    dateOrdered: '18 November 2023',
    days: '1',
    orderedFrom: 'Shopee',
    passcode: '123456',
    isDelivered: false,
  },
  {
    id: 2,
    productName: 'Raspberry Pi Heatsinks',
    dateDelivered: '02 November 2023',
    timeDelivered: '11:02 am',
    days: '17',
    orderedFrom: 'Shopee',
    isDelivered: true,
  },
  {
    id: 3,
    productName: 'ESP32 Cam',
    dateDelivered: '01 November 2023',
    timeDelivered: '1:32 pm',
    days: '18',
    orderedFrom: 'Shopee',
    isDelivered: true,
  }
];


  return (
    <div className="min-h-screen"> 
      <h1 className="text-2xl font-bold text-center my-4">Parcel Management</h1>
      <ParcelList parcels={parcels} />
      <ParcelList parcels={mockParcels} />
    </div>
  );
};

export default Dashboard;
