// ParcelList.jsx
import React from 'react';
import ParcelItem from './ParcelItem';


const ParcelList = ({ parcels }) => {
  console.log(parcels)

  return (
    <div className="flex flex-col gap-4 py-4 container mx-auto "> {/* This should match the background of your design */}
      {parcels.map((parcel) => (
        <ParcelItem key={parcel.passcode} item={parcel} />
      ))}
    </div>
  );
};

export default ParcelList;
