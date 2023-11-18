import { DynamoDB, PutItemCommand, GetItemCommand } from "@aws-sdk/client-dynamodb";
import { buildResponse } from "../utils/utils.mjs";
import bcrypt from "bcryptjs";

const client = new DynamoDB ({region: 'ap-southeast-1'});
const userTable = 'User';

// registers new users
export default async function register(userInfo) {
    const { name, username, password, address } = userInfo;

    if (!name || !address || !username || !password) {
        return buildResponse(401, { message: "All fields are required" });
    }

    // check for duplicate usernames
    const dynamoUser = await getUser(username);

    if (dynamoUser && dynamoUser.username) {
        return buildResponse(401, { message: "Username already exists in database, please choose a different username" });
    }

    const encryptedPass = bcrypt.hashSync(password, 10);
    const user = {
        username: username.toLowerCase().trim(),
        name: name,
        password: encryptedPass,
        address: address
    }
    console.log('User Data:', user)

    // save new user to database
    const saveUserResponse = await saveUser(user);
    if (!saveUserResponse) {
        return buildResponse(503, { message: "Server Error, please try again later" });
    }

    return buildResponse(200, {username: username});
}

async function getUser(username) {
    const command = new GetItemCommand({
        TableName: userTable,
        Key: {
            "username": {
                "S": username
            }
        }
    });
    const response = await client.send(command).then(response => {
        return response.Item;
    }, error => {
        console.error("There is an error:", error)
    });
    console.log(response);
    return response;
}

async function saveUser(user){
    const command = new PutItemCommand ({
        TableName: userTable,
        Item: {
            username: { S: user.username },
            name: { S: user.name },        
            password: { S: user.password },
            address: { S: user.address },
        }
    })
    const response = await client.send(command).then(response => {
        return true;
    }, error => {
        console.error("There is an error:", error)
    });;
    console.log(response);
    return response;
}