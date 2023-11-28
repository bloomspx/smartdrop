import { useState } from 'react';

export const useApi = (apiFunc) => {
  const [data, setData] = useState(null);
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const request = async (...params) => {
    setIsLoading(true);
    setError('');
    try {
      const result = await apiFunc(...params);
      setData(result);
      return result;
    } catch (error) {
      setError(error.message || 'Something went wrong');
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  return {
    data,
    error,
    isLoading,
    request,
  };
};
