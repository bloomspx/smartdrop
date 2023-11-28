import React, { useState } from 'react';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const CopyButton = ({ textToCopy }) => {
  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(textToCopy);
      toast.success('Copied successfully!', {
        position: "top-right",
        autoClose: 5000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
    } catch (err) {
      toast.error('Failed to copy!', {
        position: "top-right",
        autoClose: 5000,
        hideProgressBar: false,
        closeOnClick: true,
        pauseOnHover: true,
        draggable: true,
        progress: undefined,
      });
    }
  };

  return (
    <div className="w-full max-w-xs mx-auto h-auto">
      <div className="text-purple-700 p-2 rounded-t-lg border border-purple-500">
        Copy delivery instruction template with passcode
      </div>
      <button 
        onClick={handleCopy} 
        className="bg-purple-500 text-white p-2 rounded-b-lg w-full border border-purple-500 hover:bg-purple-600 focus:outline-none focus:bg-purple-600 transition-colors"
      >
        Copy
      </button>
    </div>
  );
};

export default CopyButton;
