import {Injectable} from "angular2/core";
import {Http} from "angular2/http";
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/delay';
import {Headers} from "angular2/http";
import {AuthHttp} from 'angular2-jwt';

@Injectable()
export class PostsService {
    constructor(private _http:Http, private _AuthHttp:AuthHttp) {
    };

    //getPosts(from, to) {return this._http.get('/api/posts/'+'?postFrom=' + from + '&postTo=' + to).delay(500)
    //        // Call map on the response observable to get the parsed people object
    //        .map(res => res.json());
    //        // Subscribe to the observable to get the parsed people object and attach it to the
    //        // component
    //}
    getPosts(from, to, date) {
        return this._AuthHttp.get('/api/PiParse/' + '?postFrom=' + from + '&postTo=' + to + '&date=' + date )
            // Call map on the response observable to get the parsed people object
            .map(res => res.json());
        // Subscribe to the observable to get the parsed people object and attach it to the
        // component
    }

    saveViewed(viewed:number[]) {
        let headers = new Headers();
        headers.append('X-CSRFToken', this.getCookie('csrftoken'));
        headers.append('Content-Type', 'application/json');
        let body = JSON.stringify({'viewed': viewed});
        return this._AuthHttp.post('/api/viewed/', body, {headers: headers})
            .map(res => res.json());
    }

    getCookie(name) {
        let value = "; " + document.cookie;
        let parts = value.split("; " + name + "=");
        if (parts.length == 2)
            return parts.pop().split(";").shift();
    }
}

