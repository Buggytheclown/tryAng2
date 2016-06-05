import {Injectable} from "angular2/core";
import {Http} from "angular2/http";
import 'rxjs/add/operator/map';
import {Headers} from "angular2/http";
import {AuthHttp} from 'angular2-jwt';

@Injectable()
export class FriendlistService {
    constructor(private _http:Http, private _AuthHttp:AuthHttp) {
    };

    getFriendlist() {
        return this._AuthHttp.get('/api/friendlist/')
            .map(res => res.json());
    }

    deleteFriend(user){}

    addFriend(user){}
}