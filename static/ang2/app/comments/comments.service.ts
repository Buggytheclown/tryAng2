import {Injectable} from "angular2/core";
import {COMMENTS} from "./mock-comments";
import {AuthHttp} from 'angular2-jwt';
import {Http} from "angular2/http";

@Injectable()
export class CommentsService {
    constructor(private _http:Http, private _AuthHttp:AuthHttp) {
    };

    getMockComments() {
        return Promise.resolve(COMMENTS);
    }

    getComments(url){
        return this._AuthHttp.get('/api/comments/' + '?page=' + url)
            // Call map on the response observable to get the parsed people object
            .map(res => res.json());
    }
}
