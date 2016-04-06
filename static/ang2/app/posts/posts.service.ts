import {Injectable} from "angular2/core";
import {Http} from "angular2/http";
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/delay';

@Injectable()
export class PostsService {
    constructor(private _http:Http) {};

    getPosts(from, to) {return this._http.get('/api/posts/'+'?postFrom=' + from + '&postTo=' + to).delay(500)
            // Call map on the response observable to get the parsed people object
            .map(res => res.json());
            // Subscribe to the observable to get the parsed people object and attach it to the
            // component
    }
}

