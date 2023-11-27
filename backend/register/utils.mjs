export function buildResponse(statusCode, body){
    return {
    statusCode: statusCode,
    headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type':'application/json'
    },
    body: JSON.stringify(body)
    };
}

export function buildCORSResponse(statusCode, body) {
    return {
        statusCode: statusCode,
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'content-type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT,DELETE',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(body)
    };
}

export default {buildResponse, buildCORSResponse};