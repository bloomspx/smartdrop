// ParcelList.jsx
import React from 'react';
import ParcelItem from './ParcelItem';


const ParcelList = ({ parcels }) => {
  console.log(parcels)

  // parcels.sort((b, a) => a.isDelivered - b.isDelivered || a.dateDelivered.split(',')[0] - b.dateDelivered.split(',')[0]);
  parcels.sort((a, b) => {
    const dateA = new Date(a.dateDelivered).getTime();
    const dateB = new Date(b.dateDelivered).getTime();
  
    return dateB - dateA;
  });


  return (
    <div className="flex flex-col gap-4 py-4 container mx-auto w-full"> {/* This should match the background of your design */}
      {parcels.map((parcel) => (
        <ParcelItem key={parcel.isDelivered} item={parcel} />
      ))}
    </div>
  );
};

export default ParcelList;
