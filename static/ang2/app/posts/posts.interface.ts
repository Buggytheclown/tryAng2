export interface Posts {
    "p_id": number;
    "rating": number;
    "post_link": string;
    "title": string;
    "timestamp": string;
    "description": string;
    "Meta"?: {
        "height"?:number;
        "saw"?:boolean;
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
}