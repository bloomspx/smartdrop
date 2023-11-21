# 50.046 CCIOT Project: IOT Smart Delivery Box


## Features Implemented

### Backend API Calls (Running on AWS Lambda)

Backend API URL:  https://teqt6xqjj5.execute-api.ap-southeast-1.amazonaws.com/beta/

`/register`: takes in a dict of {deviceID, phoneNumber, password, address} and returns {message} depending on whether registration was successful

```python
# example input
{
    "deviceID": "test4",
    "phoneNumber": "test4",
    "password": "test4",
    "address": "test4"
}
# example output
{
    "message": "true"
}
```

`/login`: takes in a dict of {phoneNumber, password} and returns { {user: deviceID, phoneNumber}, token}

```python
# example input
{
    "phoneNumber": "test",
    "password": "test"
}
# example output
{
    "user": {
        "phoneNumber": "test",
        "deviceID": "test"
    },
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZU51bWJlciI6InRlc3QiLCJkZXZpY2VJRCI6InRlc3QiLCJpYXQiOjE3MDA1NzQ0OTIsImV4cCI6MTcwMDU3ODA5Mn0.2YHZu6qIKU4nck9nubI0W52c1ym5hTa4Qsxcj8C69vE"
}
```

`/verify`: takes in a dict of {{user: phoneNumber}, token} and returns {verified, message}

```python
# example input
{
    "user":{
        "phoneNumber": "test"
    },
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZU51bWJlciI6InRlc3QiLCJkZXZpY2VJRCI6InRlc3QiLCJpYXQiOjE3MDA1NzQ0OTIsImV4cCI6MTcwMDU3ODA5Mn0.2YHZu6qIKU4nck9nubI0W52c1ym5hTa4Qsxcj8C69vE"
}
# example output
{
    "verified": true,
    "message": "success",
    "user": {
        "phoneNumber": "test"
    },
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZU51bWJlciI6InRlc3QiLCJkZXZpY2VJRCI6InRlc3QiLCJpYXQiOjE3MDA1NzQ0OTIsImV4cCI6MTcwMDU3ODA5Mn0.2YHZu6qIKU4nck9nubI0W52c1ym5hTa4Qsxcj8C69vE"
}
```

`/getallorders`: takes in a dict of {deviceID} and returns a list of objects containing order info

```python
# example input
{
    "deviceID": "test"
}
# example output
[
    {
        "orderDate": {
            "S": "11/21/2023, 4:27:25 PM"
        },
        "deliveredDate": {
            "S": ""
        },
        "imageURL": {
            "S": ""
        },
        "deviceID": {
            "S": "test"
        },
        "isDelivered": {
            "BOOL": false
        },
        "passcode": {
            "S": "228477"
        },
        "itemName": {
            "S": "aaa"
        },
        "shopName": {
            "S": "aaa"
        }
    },
    {
        "orderDate": {
            "S": "11/21/2023, 4:16:37 PM"
        },
        "deliveredDate": {
            "S": ""
        },
        "imageURL": {
            "S": ""
        },
        "deviceID": {
            "S": "test"
        },
        "isDelivered": {
            "BOOL": false
        },
        "passcode": {
            "S": "834119"
        },
        "itemName": {
            "S": "shopeee"
        },
        "shopName": {
            "S": "shopeee"
        }
    }
]
```

`/neworder`: takes in a dict of {deviceID, itemName, shopName} and returns dict of {deviceID, passcode, itemName, shopName, orderDate, isDelivered, imageURL, deliveredDate}

```python
# example input
{
    "deviceID": "test",
    "itemName": "shoope",
    "shopName": "shoope"
}
# example output
{
    "deviceID": {
        "S": "test"
    },
    "passcode": {
        "S": "538160"
    },
    "itemName": {
        "S": "shoope"
    },
    "shopName": {
        "S": "shoope"
    },
    "orderDate": {
        "S": "11/21/2023, 9:50:58 PM"
    },
    "isDelivered": {
        "BOOL": false
    },
    "imageURL": {
        "S": ""
    },
    "deliveredDate": {
        "S": ""
    }
}
```

### Hardware
1. Installation of Ubuntu 22.04 and Python 3.10.2 on Raspberry Pi 4
2. Wiring of 4x3 Keypad, Reading of keypad input and validating hardcoded passcode

## Resources
- [Figma Diagram](https://www.figma.com/file/BpAjt1A0xH5UF9vkK0eMGI/Untitled?type=design&node-id=0-1&mode=design)
- [Application Workflow](https://miro.com/app/board/uXjVNQhIkzs=/)


## Credits
- Kenny Lu's [Authentication System with AWS](https://www.youtube.com/watch?v=ReNkQ0Xkccw)
