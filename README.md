# 50.046 CCIOT Project: IOT Smart Delivery Box


## Features Implemented

### Backend API Calls (Running on AWS Lambda)

Backend API URL: https://woqp7vxlb1.execute-api.ap-southeast-1.amazonaws.com/beta

`/register`: takes in a dict of {deviceID, phoneNumber, password, address} and returns {message} depending on whether registration was successful

`/login`: takes in a dict of {phoneNumber, password} and returns { {user: deviceID, phoneNumber}, token}

`/verify`: takes in a dict of {{user: phoneNumber}, token} and returns {verified, message}

`/getallorders`: takes in a dict of {deviceID} and returns a list of objects containing order info

`/neworder`: takes in a dict of {deviceID, itemName, shopName} and returns dict of {deviceID, passcode, itemName, shopName, orderDate, isDelivered, imageURL, deliveredDate}

`/updateorder`: takes in a dict of {deviceID, passcode} and returns dict of {deviceID, passcode, itemName, shopName, orderDate, isDelivered, imageURL, deliveredDate}

### Hardware
1. Installation of Ubuntu 22.04 and Python 3.10.2 on Raspberry Pi 4
2. Wiring of 4x3 Keypad, Reading of keypad input and validating hardcoded passcode

## Resources
- [Figma Diagram](https://www.figma.com/file/BpAjt1A0xH5UF9vkK0eMGI/Untitled?type=design&node-id=0-1&mode=design)
- [Application Workflow](https://miro.com/app/board/uXjVNQhIkzs=/)


## Credits
- Kenny Lu's [Authentication System with AWS](https://www.youtube.com/watch?v=ReNkQ0Xkccw)
