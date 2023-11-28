import React from 'react';

const FormField = ({ label, type, name, placeholder, value, onChange, validationPattern, required, title}) => {
  const inputClassName = `shadow appearance-none border ${
    // required && !value ? 'border-red-500' : 'border-gray-300'
    'border-grey-300'
  } rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline`;

  const handleInvalid = (e) => {
    e.target.classList.add('border', 'border-red-500');
  };

  const handleInput = (e) => {
    e.target.classList.remove('border', 'border-red-500');
  };

  return (
    <div className="mb-4">
      <label htmlFor={name} className="block text-gray-700 text-sm font-bold mb-2">
        {label} {required && <span className="text-red-500">*</span>}
      </label>
      <input
        id={name}
        name={name}
        type={type}
        required={required}
        pattern={validationPattern}
        className={inputClassName}
        placeholder={placeholder}
        value={value}
        title={title}
        onChange={onChange}
        onInvalid={handleInvalid}
        onInput={handleInput}
      />
    </div>
  );
};

export default FormField;

