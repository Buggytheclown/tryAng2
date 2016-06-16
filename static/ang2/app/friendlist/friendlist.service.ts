import {Injectable} from "angular2/core";
import {Http} from "angular2/http";
import 'rxjs/add/operator/map';
import {Headers} from "angular2/http";
import {AuthHttp} from 'angular2-jwt';
import {headersUnsafe} from "../helpers/headersUnsafe";

@Injectable()
export class FriendlistService {
    constructor(private _http:Http, private _AuthHttp:AuthHttp, private _headersUnsafe:headersUnsafe) {
    };

    getFriendlist() {
        return this._AuthHttp.get('/api/friendlist/')
            .map(res => res.json());
    }

    deleteFriend(user){
        let headers = this._headersUnsafe.getHeaders();
        let body = JSON.stringify({'friend': user});
         return this._AuthHttp.patch('/api/friendlist/', body, headers)
            .map(res => res.json());
    }

    addFriend(user){
        let headers = this._headersUnsafe.getHeaders();
        let body = JSON.stringify({'friend': user});
         return this._AuthHttp.put('/api/friendlist/', body, headers)
            .map(res => res.json());
    }
}