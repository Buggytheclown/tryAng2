import {Injectable} from "angular2/core";
import {Http} from "angular2/http";
import 'rxjs/add/operator/map';
import {Headers} from "angular2/http";
import {AuthHttp} from 'angular2-jwt';
import {headersUnsafe} from "../helpers/headersUnsafe";

@Injectable()
export class PostsService {
    constructor(private _http:Http, private _AuthHttp:AuthHttp, private _headersUnsafe:headersUnsafe) {
    };

    getPosts(from, to, date) {
        return this._AuthHttp.get('/api/PiParse/' + '?postFrom=' + from + '&postTo=' + to + '&date=' + date )
            // Call map on the response observable to get the parsed people object
            .map(res => res.json());
        // Subscribe to the observable to get the parsed people object and attach it to the
        // component
    }

    saveViewed(viewed:number[]) {
        let headers = this._headersUnsafe.getHeaders();
        let body = JSON.stringify({'viewed': viewed});
        return this._AuthHttp.post('/api/viewed/', body, headers)
            .map(res => res.json());
    }
}

