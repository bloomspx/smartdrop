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
    <div className={`flex h-52 justify-between items-center p-4 border-l-4 ${borderColorClass} bg-white rounded-lg shadow-md`}>
      {/* Left column: Item name, date, number of days, status */}
      <div className="flex flex-col h-full basis-2/3 justify-between gap-1">
        <h3 className="text-xl font-bold top left truncate mb-2">{item.productName}</h3>
        {item.isDelivered && <p className="text-sm"><strong>Date Delivered: </strong>{item.dateDelivered}</p>}
        <p className="text-sm"><strong>Date Ordered: </strong>{item.dateOrdered}</p>
        <p className="text-sm"><strong>Number of Days: </strong>{item.days}</p>
        {!item.isDelivered && <p className='text-sm'><strong>Passcode: </strong>{item.passcode}</p>}
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
      <div className="flex h-full basis-1/3 justify-end ">
        {item.isDelivered ? (
          <img src={item.imageSrc} alt={`Delivery ${item.productName}`} className="object-scale-down rounded" />
        ) : (
        <CopyButton textToCopy={deliveryMsg}/>
        )}
      </div>
    </div>
  );
};

export default ParcelItem;
