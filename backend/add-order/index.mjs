import { buildResponse, buildCORSResponse } from "./utils.mjs";
import { DynamoDB, PutItemCommand, QueryCommand } from "@aws-sdk/client-dynamodb";

const client = new DynamoDB ({region: 'ap-southeast-1'});
const orderTable = 'Order';

export const handler = async (event) => {
    console.log("Request Event:", event);
    let response;
    
    try{
        switch(true) {
            case event.httpMethod === 'POST' && event.path === '/neworder':
                const ordersBody = JSON.parse(event.body)
                response = await newOrder(ordersBody)
                break;
            case event.httpMethod === 'OPTIONS':
                response = buildCORSResponse(200, 'Success');
                break;
            default:
                response = buildResponse(404, '404 Not Found');
        }
    } catch (error) {
        console.error("Error:", error);
        response = buildResponse(500, 'Internal Server Error');
    }
    return response;
};

async function newOrder(order) {
    const {deviceID, itemName, shopName} = order;
    
    // check for blank fields
    if (!deviceID || !itemName || !shopName) {
        return buildResponse(401, {message: "Item name and shop name are required fields to add new delivery"})
    }

    // generate unique random 6-code passcode and saves order
    const saveOrderResponse = await saveOrder(deviceID, itemName, shopName);
    if (!saveOrderResponse) {
        return buildResponse(503, { message: "Server Error, please try again later" });
    }

    return buildResponse(200, saveOrderResponse);
}

async function saveOrder(deviceID, itemName, shopName) {
    try {
        const passcode = generateRandomCode();
        // Check if an entry with the same deviceID and passcode exists
        const existingEntry = await getOrder(deviceID, passcode);

        // Handle existing entry
        while (existingEntry) {
            console.log('Entry already exists:', existingEntry);
            passcode = generateRandomCode();
            existingEntry = await getOrder(deviceID, passcode);
        } 

        // Save the new entry to the 'Order' table
        const params = {
            TableName: orderTable,
            Item: {
                deviceID: { S: deviceID },
                passcode: { S: passcode },
                itemName: { S: itemName },
                shopName: { S: shopName }, 
                orderDate: { S: new Date().toLocaleString('en-US', { timeZone: 'Asia/Singapore' })},
                isDelivered: { BOOL: false },
                imageURL: { S: "" },
                deliveredDate: { S: "" },
            },
        };

        const putCommand = new PutItemCommand(params);
        await client.send(putCommand);

        console.log('New entry saved:', params.Item);
        return params.Item;
        
    } catch (error) {
        console.error('saveOrder error:', error.message);
        return false;
    }
}

async function getOrder(deviceID, passcode) {
    const params = {
        TableName: orderTable,
        KeyConditionExpression: 'deviceID = :deviceID AND passcode = :passcode',
        ExpressionAttributeValues: {
            ':deviceID': { S: deviceID },
            ':passcode': { S: passcode },
        },
    };

    const queryCommand = new QueryCommand(params);
    const response = await client.send(queryCommand);
    return response.Items[0]; // Return the first matching item (if any)
}

function generateRandomCode() {
    // Generate a random number between 100000 and 999999
    const randomCode = Math.floor(Math.random() * 900000) + 100000;
    return randomCode.toString(); // Convert to string to ensure it is exactly 6 digits
}