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
![ESP32](https://img.shields.io/badge/-ESP32-070807?style=for-the-badge&logo=Espressif)
![Tkinter](https://img.shields.io/badge/tkinter-blue.svg?logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiA/PjwhRE9DVFlQRSBzdmcgIFBVQkxJQyAnLS8vVzNDLy9EVEQgU1ZHIDEuMS8vRU4nICAnaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkJz48c3ZnIGhlaWdodD0iNTEycHgiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTI7IiB2ZXJzaW9uPSIxLjEiIHZpZXdCb3g9IjAgMCA1MTIgNTEyIiB3aWR0aD0iNTEycHgiIHhtbDpzcGFjZT0icHJlc2VydmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiPjxnIGlkPSJjb21wX3g1Rl8yNjctcHl0aG9uIj48Zz48Zz48Zz48cGF0aCBkPSJNMTk0LjAwNSwyNDAuMjUyaDEwNS4wNTRjMjkuMjE2LDAsNTIuNTI5LTI0LjEwMSw1Mi41MjktNTMuNDE0Vjg2LjYwMyAgICAgIGMwLTI4LjUyNS0yNC4wMDItNDkuODcxLTUyLjUyOS01NC42OTFjLTM1LjIxNC01LjgwNC03My40NzktNS41MDktMTA1LjA1NCwwLjA5N2MtNDQuNDYyLDcuODctNTIuNTI3LDI0LjI5OC01Mi41MjcsNTQuNjkzICAgICAgdjIxLjQ1M0gyNDYuNjN2MzEuOTU5SDEwMi4wMzJjLTMwLjU5MSwwLTU3LjM0OSwxOC4zOTQtNjUuNzA5LDUzLjMxNWMtOS42NCw0MC4wMzUtMTAuMDMyLDY1LjAyLDAsMTA2LjgyNiAgICAgIGM3LjQ3NywzMS4wODUsMjUuMjgsNTMuMzE0LDU1Ljg3Miw1My4zMTRoMzYuMTAxdi00OC4wMDFDMTI4LjI5NiwyNzAuODQ1LDE1OC4yOTgsMjQwLjI1MiwxOTQuMDA1LDI0MC4yNTJMMTk0LjAwNSwyNDAuMjUyeiIgc3R5bGU9ImZpbGw6IzM0N0FCNDsiLz48Zz48cGF0aCBkPSJNMTI4LjI5NiwzNjMuNTY5SDkyLjE5NWMtMzIuODQyLDAtNTYuMTM3LTIxLjY1NS02NS41OTUtNjAuOTc2ICAgICAgIGMtMTAuMTQ2LTQyLjI3Ni0xMC4xNDUtNjkuMzcsMC0xMTEuNTA1YzQuNTIxLTE4Ljg4NSwxNC4yNDMtMzQuNTU5LDI4LjExMi00NS4zMTRjMTMuMjEtMTAuMjQ1LDI5LjU3My0xNS42Niw0Ny4zMTktMTUuNjYgICAgICAgSDIzNi42M3YtMTEuOTU5aC05NS4xNTJjLTUuNTIzLDAtMTAtNC40NzctMTAtMTBWODYuNzAyYzAtMTMuOTU0LDEuNDIzLTI5Ljg4OSwxMS45NzktNDIuMjc4ICAgICAgIGM5LjQ1Mi0xMS4wOTQsMjQuNTA0LTE3Ljk2LDQ4LjgwNi0yMi4yNjFjMTYuNTEyLTIuOTMyLDM1LjEyNy00LjQ4Miw1My44MjktNC40ODJjMTguNjU1LDAsMzcuMDIzLDEuNDY5LDU0LjU5NCw0LjM2NSAgICAgICBjMTYuMzQ1LDIuNzYyLDMxLjM4MywxMC4yOTksNDIuMzg1LDIxLjIyOWMxMS45NDEsMTEuODY1LDE4LjUxOSwyNy4yNTMsMTguNTE5LDQzLjMyOXYxMDAuMjM1ICAgICAgIGMwLDM0Ljk2Ny0yOC4wNTEsNjMuNDE0LTYyLjUyOSw2My40MTRIMTk0LjAwNWMtMjkuNjc3LDAtNTUuNzA5LDI1Ljg0OS01NS43MDksNTUuMzE2djQ4LjAwMSAgICAgICBDMTM4LjI5NiwzNTkuMDkyLDEzMy44MTksMzYzLjU2OSwxMjguMjk2LDM2My41Njl6IE0xMDIuMDMyLDE1MC4xMTRjLTI4LjIxMywwLTQ5LjE0MiwxNy4wNjMtNTUuOTg0LDQ1LjY0MyAgICAgICBjLTkuNTI2LDM5LjU2My05LjUyNSw2Mi40NzUtMC4wMDEsMTAyLjE2NWM1LjAwOCwyMC44MjEsMTcuMDgxLDQ1LjY0Nyw0Ni4xNDgsNDUuNjQ3aDI2LjEwMXYtMzguMDAxICAgICAgIGMwLTE5LjI2Myw4LjE1OS0zOC40ODcsMjIuMzg2LTUyLjc0M2MxNC41MjctMTQuNTU3LDMzLjQ2NC0yMi41NzMsNTMuMzIzLTIyLjU3M2gxMDUuMDU0ICAgICAgIGMyMy40NTEsMCw0Mi41MjktMTkuNDc2LDQyLjUyOS00My40MTRWODYuNjAzYzAtMjQuNTI5LTIyLjIzMy00MS4xMi00NC4xOTUtNDQuODMxYy0xNi40Ni0yLjcxMy0zMy43MzMtNC4wOTItNTEuMzAyLTQuMDkyICAgICAgIGMtMTcuNTQ5LDAtMzQuOTU2LDEuNDQ0LTUwLjMzNyw0LjE3NWMtMzkuOTA4LDcuMDY0LTQ0LjI3NSwxOS42ODktNDQuMjc1LDQ0Ljg0N3YxMS40NTNoOTUuMTUyYzUuNTIzLDAsMTAsNC40NzcsMTAsMTB2MzEuOTU5ICAgICAgIGMwLDUuNTIzLTQuNDc3LDEwLTEwLDEwSDEwMi4wMzJ6IiBzdHlsZT0iZmlsbDojMjc1Qzg3OyIvPjwvZz48L2c+PGc+PHBhdGggZD0iTTQ3NC45NzUsMjA5LjM3MmMtNy41NzUtMzAuMzk1LTIxLjkzNS01My4zMTUtNTIuNTI3LTUzLjMxNWgtMzkuNDQzdjQ2LjYyNiAgICAgIGMwLDM2LjE5OS0zMC42OTIsNjYuNjkxLTY1LjcxLDY2LjY5MUgyMTIuMjRjLTI4LjcyNCwwLTUyLjUyOCwyNC41OTQtNTIuNTI4LDUzLjQxNHYxMDAuMTM4ICAgICAgYzAsMjguNTI0LDI0Ljc4OCw0NS4yNDYsNTIuNTI4LDUzLjQxM2MzMy4yNDcsOS43MzcsNjUuMjE1LDExLjUwOSwxMDUuMDU0LDBjMjYuNDYyLTcuNjc1LDUyLjUyOS0yMy4xMTYsNTIuNTI5LTUzLjQxM3YtMjAuOTk3ICAgICAgSDI2NC44Njd2LTMyLjQxN2gxNTcuNThjMzAuNTkzLDAsNDEuOTA0LTIxLjM0Niw1Mi41MjctNTMuMzE0QzQ4NS45OTIsMjgzLjI0NCw0ODUuNTAxLDI1MS41Nyw0NzQuOTc1LDIwOS4zNzJMNDc0Ljk3NSwyMDkuMzcyICAgICAgeiIgc3R5bGU9ImZpbGw6I0ZGQ0ExRDsiLz48Zz48cGF0aCBkPSJNMjY0LjQzMSw0OTQuMzJjLTE3Ljc0NywwLTM1LjczOC0yLjc0My01NS4wMDEtOC4zODUgICAgICAgYy0zOC41MTUtMTEuMzM5LTU5LjcxOC0zMy43MTUtNTkuNzE4LTYzLjAxVjMyMi43ODhjMC0zNC4zNzQsMjguNjM0LTYzLjQxNCw2Mi41MjgtNjMuNDE0aDEwNS4wNTQgICAgICAgYzI5LjY3OCwwLDU1LjcxLTI2LjQ5MSw1NS43MS01Ni42OTF2LTQ2LjYyNmMwLTUuNTIzLDQuNDc4LTEwLDEwLTEwaDM5LjQ0M2MxNy4yNzYsMCwzMS41NDYsNi4yNzksNDIuNDEyLDE4LjY2NCAgICAgICBjOC43MzQsOS45NTUsMTUuMjE3LDIzLjc3LDE5LjgxOCw0Mi4yMzJjMTEuMTkxLDQ0Ljg2MywxMS4xMjYsNzguNDgzLTAuMjE5LDExMi40MTVjLTEwLjExLDMwLjQyNC0yMy4yMyw2MC4xNDQtNjIuMDEyLDYwLjE0NCAgICAgICBoLTE0Ny41OHYxMi40MTdoOTQuOTU2YzUuNTIyLDAsMTAsNC40NzgsMTAsMTB2MjAuOTk3YzAsMjAuODQ0LTEwLjM2NSw0OC42OTYtNTkuNzQ0LDYzLjAxOCAgICAgICBDMzAwLjU2Myw0OTEuNTgxLDI4Mi4zNjQsNDk0LjMyLDI2NC40MzEsNDk0LjMyeiBNMjEyLjI0LDI3OS4zNzRjLTIzLjA1MywwLTQyLjUyOCwxOS44ODEtNDIuNTI4LDQzLjQxNHYxMDAuMTM4ICAgICAgIGMwLDI2LjUxLDI4LjQxNSwzOC44MzQsNDUuMzUzLDQzLjgyYzE3LjYzOSw1LjE2NiwzMy4zMyw3LjU3NCw0OS4zNjYsNy41NzRjMTYuMDI4LDAsMzIuNDEzLTIuNDgyLDUwLjA4OC03LjU4OSAgICAgICBjMzAuMDU5LTguNzE4LDQ1LjMwNS0yMy40NTcsNDUuMzA1LTQzLjgwNnYtMTAuOTk3aC05NC45NTZjLTUuNTIyLDAtMTAtNC40NzgtMTAtMTB2LTMyLjQxN2MwLTUuNTIyLDQuNDc4LTEwLDEwLTEwaDE1Ny41OCAgICAgICBjMjEuMTQ4LDAsMzEuMjA0LTEwLjg1Nyw0My4wMzctNDYuNDY4YzEwLjE4OS0zMC40NzYsMTAuMTI2LTU5LjgwNS0wLjIxMy0xMDEuMjUyYy03Ljg4My0zMS42MzEtMjEuMDktNDUuNzM1LTQyLjgyNC00NS43MzUgICAgICAgaC0yOS40NDN2MzYuNjI2YzAsNDEuNTcxLTM0LjY3MSw3Ni42OTEtNzUuNzEsNzYuNjkxSDIxMi4yNHoiIHN0eWxlPSJmaWxsOiNCRjk4MTY7Ii8+PC9nPjwvZz48cGF0aCBkPSJNMTg3LjQxNCw4OS41OTRjLTEwLjQ3OSwwLTE4Ljk3NS04LjU5MS0xOC45NzUtMTkuMTY0YzAuMDk0LTEwLjY2OCw4LjQ5Ni0xOS4yNTksMTguOTc1LTE5LjI1OSAgICAgYzEwLjM4NiwwLDE4Ljk3Niw4LjY4NSwxOC45NzYsMTkuMjU5QzIwNi4zOSw4MS4wMDMsMTk3Ljg5NCw4OS41OTQsMTg3LjQxNCw4OS41OTR6IiBzdHlsZT0iZmlsbDojRkZGRkZGOyIvPjxwYXRoIGQ9Ik0zMTQuOTA4LDQ2MC4wNzZjLTEwLjQ3OSwwLTE4Ljk3Ni04LjU5MS0xOC45NzYtMTkuMTY0YzAuMDk1LTEwLjY2OCw4LjQ5Ni0xOS4yNTksMTguOTc2LTE5LjI1OSAgICAgYzEwLjM4NSwwLDE4Ljk3Niw4LjY4NSwxOC45NzYsMTkuMjU5QzMzMy44ODQsNDUxLjQ4NSwzMjUuMzg4LDQ2MC4wNzYsMzE0LjkwOCw0NjAuMDc2eiIgc3R5bGU9ImZpbGw6I0ZGRkZGRjsiLz48L2c+PC9nPjwvZz48ZyBpZD0iTGF5ZXJfMSIvPjwvc3ZnPg==)
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

