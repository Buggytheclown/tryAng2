export interface Comments {
    //TODO rating string or number?
    useravatar: string;
    username: string;
    rating: string;
    time: string;

    content: string;
    child: Array<Comments>;
}