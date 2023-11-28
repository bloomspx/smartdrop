import React, { useState, useEffect } from 'react';
import FormField from '../components/FormField';
import Button from '../components/Button';
import { Link } from 'react-router-dom';
import { useFormSubmission } from '../api/useFormSubmission';
import { apiClient } from '../api/apiClient';
import { setUserSession } from '../service/AuthService';


const LoginPage = () => {
  const { isLoading, handleSubmit } = useFormSubmission((...params) => 
    apiClient.login(...params).then((data) => {
      setUserSession(data.user, data.token);
      console.log(data, data.user, data.token);
    }), '/dashboard')

  const [formData, setFormData] = useState({
    phoneNumber: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const submitForm = (e) => {
    e.preventDefault();
    handleSubmit(formData);
  };

  return (
    <div className="flex justify-center items-center min-h-screen">
    <div className="max-w-md w-full bg-white rounded-lg shadow-md p-8">
      <h1 className="text-2xl font-bold text-center my-4">Login</h1>
        <form onSubmit={submitForm}>
          <FormField
            label="Phone Number"
            type="tel"
            name="phoneNumber"
            placeholder="Enter Phone Number"
            value={formData.phone}
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
          <Button type="submit" className="w-full mt-6">
            {isLoading ? 'Loading...' : 'Login'}
          </Button>
          <p className="mt-4 text-center text-white">
            Don't have an account yet?
            <Link to="/register" className="text-purple-600 hover:text-purple-700 font-semibold"> Sign up here!</Link>
          </p>
        </form>
      </div>
    </div>
  );
};

export default LoginPage;
