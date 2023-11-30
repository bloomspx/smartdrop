import React, { useState } from 'react';
import CopyButton from './CopyButton';

const ParcelItem = ({ item }) => {

  const [isExpanded, setIsExpanded] = useState(false);
  const borderColorClass = item.isDelivered ? 'border-green-500' : 'border-yellow-400';
  const statusIcon = item.isDelivered ? '✅' : '🕗';
  const statusText = item.isDelivered ? 'Delivered' : 'Expected Delivery In Progress';

  const toggleImage = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <div className={`flex h-52 justify-between items-center p-4 border-l-4 ${borderColorClass} bg-white rounded-lg shadow-md`}>
      {/* Left column: Item name, date, number of days, status */}
      <div className="flex flex-col h-full basis-3/4 justify-between gap-1">
        <h3 className="text-xl font-bold top left truncate pb-2">{item.productName}</h3>
        {item.isDelivered && <p className="text-sm"><strong>Date Delivered: </strong>{item.dateDelivered}</p>}
        <p className="text-sm"><strong>Date Ordered: </strong>{item.dateOrdered}</p>
        <p className="text-sm"><strong>Number of Days: </strong>{item.days}</p>
        <p className='text-sm'><strong>Passcode: </strong>{item.passcode}</p>
        <p className="text-sm"><strong>Ordered From: </strong>{item.orderedFrom}</p>

        <div className="flex items-center mt-1">
          <span className={`text-sm font-bold ${item.isDelivered ? 'text-green-500' : 'text-yellow-500'}`}>
            {statusIcon}
            <span className="ml-2 text-sm">{statusText}</span>
          </span>
        </div>
      </div>

      {/* Right column: Image or Copy button */}
      {/* <div className="flex items-stretch justify-end flex-grow"> */}
      <div className="flex h-full basis-1/4 justify-end">
        {item.isDelivered ? (
        <img 
          src={item.imageSrc} 
          alt={`Delivery ${item.productName}`} 
          className={`object-scale-down rounded shadow-md cursor-pointer transition-transform duration-300 hover:scale-150`} 
          onClick={toggleImage}
        />)           
        : (
        <CopyButton textToCopy={item.passcode}/>
        )}
      </div>
    </div>
  );
};

export default ParcelItem;
