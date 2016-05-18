export interface Posts {
    'id':number;
    'viewed': boolean;
    "p_id": number;
    "rating": number;
    "post_link": string;
    "title": string;
    "timestamp": string;
    "description": string;
    "Meta"?: {
        "height"?:number;
        "doTrunk"?:boolean;
    }
    "contents": Array<{
        "type": string;
        "pre_content": string;
        "content": string;
        "Meta"?: {
            "play"?:boolean;
        }
    }>
    "userGroups": Array<{
         "name"?: string,
         "users"?: Array <{
            "id": number,
            "username": string,
         }>
    }>
}