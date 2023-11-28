// RegistrationPage.jsx
import React, { useState } from 'react';
import FormField from '../components/FormField';
import Button from '../components/Button';
import { useFormSubmission } from '../api/useFormSubmission';
import { apiClient } from '../api/apiClient'

const RegistrationPage = () => {
  const {isLoading, handleSubmit} = useFormSubmission(apiClient.register, '/')
  const [formData, setFormData] = useState({
    deviceID: '',
    phoneNumber: '',
    address: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const submitForm = (e) => {
    e.preventDefault();
    handleSubmit(formData)
  };

  return (
    <div className="flex justify-center items-center min-h-screen"> 
    <div className="max-w-md w-full bg-white rounded-lg shadow-md p-8">
      <h1 className="text-2xl font-bold text-center my-4">SmartDrop Registration</h1>
        <form onSubmit={submitForm}>
          <FormField
            label="Device ID"
            type="text"
            name="deviceID"
            placeholder="Enter Device ID"
            value={formData.deviceID}
            onChange={handleChange}
            required
          />
          <FormField
            label="Phone Number"
            type="tel"
            name="phoneNumber"
            placeholder="Enter Phone Number"
            value={formData.phone}
            onChange={handleChange}
            required
            validationPattern='^[0-9]+$'
            title="This isn't a correct phone number."
          />
          <FormField
            label="Address"
            type="text"
            name="address"
            placeholder="Enter Address"
            value={formData.address}
            onChange={handleChange}
            required
          />
          <FormField
            label="Password"
            type="password"
            name="password"
            placeholder="Enter Password"
            value={formData.password}
            onChange={handleChange}
            required
          />
          <Button type="submit" className="w-full mt-6 text-white">
            {isLoading ? 'Loading...' : 'Register'}
          </Button>
        </form>
      </div>
    </div>
  );
};

export default RegistrationPage;
