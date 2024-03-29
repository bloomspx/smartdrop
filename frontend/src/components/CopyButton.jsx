import React, { useState } from 'react';
import { toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const CopyButton = ({ textToCopy }) => {
  const deliveryMsg = `Hello, you will be delivering to a SmartDrop!
Kindly follow the instructions on the SmartDrop and enter the passcode ${textToCopy} when prompted.
Thank you!`

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(deliveryMsg);
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
    <div className="flex flex-col justify-center w-full max-w-xs h-auto">
      <div className="text-black p-2 text-center rounded-t-lg shadow-md border-2 border-indigo-600">
        {/* Copy delivery instruction template with passcode */}
        {textToCopy}
      </div>
      <button 
        onClick={handleCopy} 
        className="bg-indigo-600 text-white p-2 rounded-b-lg w-full hover:bg-indigo-800 focus:outline-none focus:bg-indigo-700 transition-colors"
      >
        Copy delivery instructions
      </button>
    </div>
  );
};

export default CopyButton;
