import {buildResponse, buildCORSResponse} from "./utils.mjs";
import { DynamoDB, QueryCommand } from "@aws-sdk/client-dynamodb";

const client = new DynamoDB ({region: 'ap-southeast-1'});
const orderTable = 'Order';

export const handler = async (event) => {
    console.log("Request Event:", event);
    let response;
    
    try{
        switch(true) {
            case event.httpMethod === 'POST' && event.path === '/getallorders':
                const ordersBody = JSON.parse(event.body)
                response = await getAllOrders(ordersBody)
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

async function getAllOrders(user) {
    
    const { deviceID } = user;
    const params = {
        TableName: orderTable,
        KeyConditionExpression: 'deviceID = :deviceID',
        ExpressionAttributeValues: {
            ':deviceID': { S: deviceID },
        },
    };

    try {
        const command = new QueryCommand(params);
        const response = await client.send(command);
        console.log("getAllOrders:", response.Items); // This will contain the items from the 'Order' table for the specified username
        return buildResponse(200, response.Items);
    } catch (error) {
        console.error('getAllOrders Error:', error.message, error.stack);
        return buildResponse(503, { message: "Server Error, please try again later" });
    }
}