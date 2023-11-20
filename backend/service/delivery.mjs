import { DynamoDB, PutItemCommand, QueryCommand } from "@aws-sdk/client-dynamodb";
import { buildResponse }from "../utils/utils.mjs";

const client = new DynamoDB ({region: 'ap-southeast-1'});
const userTable = 'User';
const orderTable = 'Order';

export async function getOrders(user) {
    
    const {phoneNumber} = user;
    const params = {
        TableName: orderTable,
        KeyConditionExpression: 'phoneNumber = :phoneNumber',
        ExpressionAttributeValues: {
            ':phoneNumber': { S: phoneNumber },
        },
    };

    try {
        const command = new QueryCommand(params);
        const response = await client.send(command);
        console.log("getOrders:", response.Items); // This will contain the items from the 'Order' table for the specified username
        return buildResponse(200, response.Items);
    } catch (error) {
        console.error('getOrders Error:', error.message, error.stack);
        return buildResponse(503, { message: "Server Error, please try again later" });
    }
}

export async function newDelivery(order) {
    const {phoneNumber, itemName, shopName} = order;
    
    // check for blank fields
    if (!phoneNumber || !itemName || !shopName) {
        return buildResponse(401, {message: "Item name and shop name are required fields to add new delivery"})
    }

    // generate unique random 6-code passcode and saves order
    const saveOrderResponse = await saveOrder(phoneNumber, itemName, shopName);
    if (!saveOrderResponse) {
        return buildResponse(503, { message: "Server Error, please try again later" });
    }

    return buildResponse(200, saveOrderResponse);
}

async function saveOrder(phoneNumber, itemName, shopName) {
    try {
        const passcode = generateRandomCode();
        // Check if an entry with the same phoneNumber and passcode exists
        const existingEntry = await getOrder(phoneNumber, passcode);

        // Handle existing entry
        while (existingEntry) {
            console.log('Entry already exists:', existingEntry);
            passcode = generateRandomCode();
            existingEntry = await getOrder(phoneNumber, passcode);
        } 

        const currentDateTime = new Date().toLocaleString('en-US', { timeZone: 'Asia/Singapore' });

        // Save the new entry to the 'Order' table
        const params = {
            TableName: orderTable,
            Item: {
                phoneNumber: { S: phoneNumber },
                passcode: { S: passcode },
                itemName: { S: itemName },
                shopName: { S: shopName }, 
                orderDate: { S: currentDateTime },
                isDelivered: { S: "False" },
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

async function getOrder(phoneNumber, passcode) {
    const params = {
        TableName: orderTable,
        KeyConditionExpression: 'phoneNumber = :phoneNumber AND passcode = :passcode',
        ExpressionAttributeValues: {
            ':phoneNumber': { S: phoneNumber },
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

export default { getOrders, newDelivery };