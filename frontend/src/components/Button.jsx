import React from 'react';

const Button = ({ onClick, type, className, children, disabled }) => {
  // Base styles for the button
  const baseStyles = "inline-block text-center px-6 py-2 text-base font-medium leading-6 shadow rounded-md transition ease-in-out duration-150";

  // Combine all classes together
  const classes = `${baseStyles} ${className} ${disabled ? 'bg-gray-400 cursor-not-allowed' : 'bg-purple-600 hover:bg-purple-700'}`;

  return (
    <button onClick={onClick} type={type} className={classes} disabled={disabled}>
      {children}
    </button>
  );
};

export default Button;
