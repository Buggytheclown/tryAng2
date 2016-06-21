export interface Comments {
    useravatar: string;
    username: string;
    rating: string;
    time: string;

    content: string;
    child: Array<Comments>;
}