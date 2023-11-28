import { useApi } from './useApi';
import { useNavigate } from 'react-router-dom';
import { toast } from 'react-toastify';
import { useState } from 'react';

export const useFormSubmission = (apiFunc, successPath) => {
  const [isLoading, setIsLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (formData) => {
    setIsLoading(true);
    try {
      const data = await apiFunc(formData);
      navigate(successPath);
      toast.success('Success!');
    } catch (error) {
      toast.error(error.message || 'An error occurred');
    } finally {
      setIsLoading(false);
    }
  };

  return {
    isLoading,
    handleSubmit,
  };
};
