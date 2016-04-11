import {Injectable} from "angular2/core";
import {Http} from "angular2/http";
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/delay';
import {Headers} from "angular2/http";
import {tokenNotExpired} from 'angular2-jwt';

@Injectable()
export class LoginService {
    constructor(private _http:Http) {
    };

    login(name, pass) {
        let body = JSON.stringify({'username': name, 'password': pass});
        let headers = new Headers();
        headers.append('Content-Type', 'application/json');
        return this._http.post('/api-token-auth/', body, {headers: headers})
            .map(res => res.json());
    }

    register(name, pass, email) {
        let headers = new Headers();
        headers.append('X-CSRFToken', this.getCookie('csrftoken'));
        headers.append('Content-Type', 'application/json');
        let body = JSON.stringify({'username': name, 'password': pass, 'email': email });
        return this._http.post('/api-register/', body, {headers: headers})
            .map(res => res.json());
    }

    getCookie(name) {
        let value = "; " + document.cookie;
        let parts = value.split("; " + name + "=");
        if (parts.length == 2)
            return parts.pop().split(";").shift();
    }
}

