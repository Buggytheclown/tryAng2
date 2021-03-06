import {Content} from "./post/content/content.interface";

export interface Posts {
    viewed: boolean;
    commentsCount: number;
    p_id: number;
    rating: number;
    post_link: string;
    title: string;
    timestamp: string;
    description: string;
    contents: Array<Content>;
    friendsViewed: Array<string>;
}