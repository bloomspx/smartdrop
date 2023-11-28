import React from 'react';
import CopyButton from './CopyButton';

const ParcelItem = ({ item }) => {
  const borderColorClass = item.isDelivered ? 'border-green-500' : 'border-yellow-400';
  const statusIcon = item.isDelivered ? '✅' : '🕗';
  const statusText = item.isDelivered ? 'Delivered' : 'Expected Delivery In Progress';

  const deliveryMsg = `Hello, you will be delivering to a SmartDrop!
Kindly follow the instructions on the SmartDrop and enter the passcode ${item.passcode} when prompted.
Thank you!`

  return (
    <div className={`flex justify-between items-center p-4 border-l-4 ${borderColorClass} bg-white rounded-lg shadow`}>
      {/* Left column: Item name, date, number of days, status */}
      <div className="relative flex flex-col justify-between flex-grow">
        <h3 className="font-bold top left truncate">{item.productName}</h3>
        <p className="text-sm py-1">{item.isDelivered ? `Date Delivered: ${item.dateDelivered}` : `Date Ordered: ${item.dateOrdered}`}</p>
        <p className="text-sm py-1">Number of Days: {item.days}</p>
        <div className="flex items-center pt-3">
          <span className={`text-sm font-bold ${item.isDelivered ? 'text-green-500' : 'text-yellow-500'}`}>
            {statusIcon}
          </span>
          <span className="ml-2 text-sm">{statusText}</span>
        </div>
      </div>

      {/* Middle column: Time delivered, ordered from */}
      <div className="flex flex-col justify-between flex-grow">
        {item.isDelivered && <p className="text-sm py-1">Time Delivered: {item.timeDelivered}</p>}
        {!item.isDelivered && <p className='text-sm py-1'>Passcode: {item.passcode}</p>}
        <p className="text-sm py-1">Ordered From: {item.orderedFrom}</p>
      </div>

      {/* Right column: Image or Copy button */}
      {/* <div className="flex items-stretch justify-end flex-grow"> */}
      <div className="flex flex-col justify-between flex-grow">
        {item.isDelivered ? (
          <img src={item.imageSrc} alt={`Delivery ${item.productName}`} className="w-28 h-28 object-cover rounded" />
        ) : (
        <CopyButton textToCopy={deliveryMsg}/>
        )}
      </div>
    </div>
  );
};

export default ParcelItem;
