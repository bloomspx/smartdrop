// ParcelList.jsx
import React from 'react';
import ParcelItem from './ParcelItem';
import Button from './Button'; // Assume Button component is already created
import { useNavigate } from 'react-router-dom'; // Import useHistory from react-router-dom


const ParcelList = ({ parcels }) => {
  const navigate = useNavigate();

  const handleCreateNew = () => {
    navigate('/new-delivery'); // Use the actual route for creating a new delivery
  };

  return (
    <div className="container mx-auto p-4"> {/* This should match the background of your design */}
      <div className="flex justify-end mb-6">
        <Button className="bg-blue-500 hover:bg-blue-700 text-white py-2 px-4 rounded" onClick={handleCreateNew}>
          Create New Delivery
        </Button>
      </div>
      {parcels.map((parcel) => (
        <ParcelItem key={parcel.id} item={parcel} />
      ))}
    </div>
  );
};

export default ParcelList;
