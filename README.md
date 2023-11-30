<h1 align="center" style="border-bottom: none">
    <b>SmartDrop</b>
    <br>
    2023 50.046 Cloud Computing & Internet of Things
    <br>
</h1>

<p align="center">
    A smart IOT delivery box built with AWS + React using a Raspberry Pi + ESP32
</p>

<div align="center">

![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi)
</div>

<table align="center">
<h2>Group 2: </h2>
  <tr>
    <td align="center"><a href="https://github.com/ssjh23"><img src="https://avatars.githubusercontent.com/u/64569228?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sean Soo</b><br/>1005263</sub></a><br />
    <td align="center"><a href="https://github.com/ryanpantk"><img src="https://avatars.githubusercontent.com/u/66586824?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Ryan Pan</b><br/> 1005037</sub></a><br />
    <td align="center"><a href="https://github.com/bloomspx"><img src="https://avatars.githubusercontent.com/bloomspx?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Soh Pei Xuan</b><br/> 1005552</sub></a><br/>
    <td align="center"><a href="https://github.com/xhhhhang"><img src="https://avatars.githubusercontent.com/u/151045393?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Liu Renhang</b><br/> 1004873</sub></a><br />
  </tr>
</table>

# Resources
- [Figma Design](https://www.figma.com/file/BpAjt1A0xH5UF9vkK0eMGI/Untitled?type=design&node-id=0-1&mode=design)
- [Application Workflow](https://miro.com/app/board/uXjVNQhIkzs=/)

# Table of Contents
-   [Getting Started](#getting-started)
-   [API Calling](#api-calling)
-   [AWS Lambda Functions for MQTT PUB/SUB](#aws-lambda-functions-for-mqtt-pubsub)
-   [File Directories](#file-directories)
-   [External Resources](#external-resources)

# Getting Started
### 1. Install Node dependencies 

```
cd frontend
npm install
```
### 2. Running Web Server
To begin running the web application, first start a new terminal and run the frontend React server (http://localhost:3000/)
```
npm start
```


# API Calling
Our frontend server makes API calls to the [AWS Server API](https://woqp7vxlb1.execute-api.ap-southeast-1.amazonaws.com/beta). Sample Postman calls can be found in `/postman`. 
Overall, there are 5 main endpoints, with each endpoint corresponding to its own AWS lambda function:

### 1. Register User: 
Function Name: `smart-locker-register`

Endpoint: `/register`: takes in a dict of {deviceID, phoneNumber, password, address} and returns {message} depending on whether registration was successful

### 2. Login User: 
Function Name: `smart-locker-login`

Endpoint: `/login`: takes in a dict of {phoneNumber, password} and returns { {user: deviceID, phoneNumber}, token}

### 3. Verify User is Logged In: 
Function Name: `smart-locker-login`

Endpoint: `/verify`: takes in a dict of {{user: phoneNumber}, token} and returns {verified, message}

### 4. Get All Orders:
Function Name: `smart-locker-get-all-orders`

Endpoint: `/getallorders`: takes in a dict of {deviceID} and returns a list of objects containing order info

### 5. Add New Order:
Function Name: `smart-locker-new-order`

Endpoint: `/neworder`: takes in a dict of {deviceID, itemName, shopName} and returns dict of {deviceID, passcode, itemName, shopName, orderDate, isDelivered, imageURL, deliveredDate}


# AWS Lambda Functions for MQTT PUB/SUB
The 2 following lambda functions facilitate the communication between the ESP32, Raspberry Pi and AWS IoT Core using MQTT.

### 1. `smart-locker-validate-order`
- SUB to `/cciot/validate`
- On trigger, uses {deviceID, passcode} to check for a valid order entry in DynamoDB
- PUB to `/cciot/validated` with {deviceID, passcode, isValidated} for status on whether passcode corresponds to a valid order in device

### 2. `smart-locker-publish-photo`
- SUB to `/cciot/publish-photo`
- On trigger, updates DynamoDB with imageURL, deliveredDate and deliveredStatus
- PUB to `/cciot/photo-published` with {deviceID, passcode, published} for successful entry update


# File Directories
```
📦backend              # AWS backend lambda functions
 ┣ 📂add-order
 ┣ 📂get-all-orders
 ┣ 📂login
 ┣ 📂publish-photo
 ┣ 📂register 
 ┣ 📂validate-order
 📦esp32-cam           # esp32 cam code
 📦frontend 
 ┣ 📂public            # images used for frontend
 ┣ 📂src
 ┃ ┣ 📂api             # custom api function
 ┃ ┣ 📂components      # building blocks for webpage
 ┃ ┣ 📂icons           # icons used for frontend
 ┃ ┣ 📂pages           # main webpages: login, register, dashboard, add order
 ┃ ┣ 📂routes          # routing for logged in / non-logged in users
 ┃ ┗ 📂service         # user authentication function
 📦hardware            # configuration for solonoid lock + keypad
 📦postman             # sample postman calls for backend api
 📦raspberry-pi        # raspberry pi configuration
 ```

# External Resources
- [Date-FNS](https://date-fns.org/)
- [TailwindCSS](https://tailwindcss.com/)
- [React-Toastify](https://github.com/fkhadra/react-toastify)

