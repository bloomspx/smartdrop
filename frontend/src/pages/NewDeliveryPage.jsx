import React, { useState } from 'react';
import FormField from '../components/FormField';
import Button from '../components/Button';
import { useFormSubmission } from '../api/useFormSubmission';
import { apiClient } from '../api/apiClient';
import { getUser } from '../service/AuthService';
import { useNavigate } from 'react-router-dom';
import { ReactComponent as BackIcon } from '../icons/back-icon.svg'

const NewDeliveryPage = () => {
  const navigate = useNavigate();
  const { isLoading, handleSubmit } = useFormSubmission(apiClient.newOrder, '/dashboard')
  const [formData, setFormData] = useState({
    itemName: '',
    shopName: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const submitForm = (e) => {
    e.preventDefault();
    const data = { ...formData, deviceID: getUser().deviceID };
    console.log(data);
    handleSubmit(data);
    // Here you would typically handle the creation of a new delivery
  };

  return (
    <div className="flex justify-center items-center min-h-screen">
      <div className="relative max-w-md w-full bg-white rounded-lg shadow-md p-8">
        <button
          onClick={() => navigate('/dashboard')}
          className="absolute top-0 left-0 m-4 p-2 text-gray-600 hover:text-gray-800"
        >
          <BackIcon className="w-4 h-4" />
        </button>
        <h1 className="text-2xl font-bold text-center my-4">Create New Delivery</h1>
        <form onSubmit={submitForm}>
          <FormField
            label="Item Name"
            type="text"
            name="itemName"
            placeholder="Enter Item Name"
            value={formData.itemName}
            onChange={handleChange}
            required
          />
          <FormField
            label="Ordered From"
            type="text"
            name="shopName"
            placeholder="Enter Where Item Was Ordered From"
            value={formData.orderedFrom}
            onChange={handleChange}
            required
          />
          <Button type="submit" className="w-full mt-6 text-white">
            {isLoading ? 'Loading' : 'Create Delivery'}
          </Button>
        </form>
      </div>
    </div>
  );
};

export default NewDeliveryPage;
