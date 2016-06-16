import {Injectable} from "angular2/core";
import {Http} from "angular2/http";
import 'rxjs/add/operator/map';
import {AuthHttp} from 'angular2-jwt';
import {Headers} from "angular2/http";

@Injectable()
export class VotesService {
    constructor(private _http:Http, private _AuthHttp:AuthHttp) {};

    getVotes() {
            let myHeader = new Headers();
            myHeader.append('Content-Type', 'application/json');
            return this._AuthHttp.get('/api/polls/', { headers: myHeader})
            // Call map on the response observable to get the parsed people object
            .map(res => res.json());
            // Subscribe to the observable to get the parsed people object and attach it to the
            // component
    }
    doVotes(vote_id, choice_id){
        return this._http.get('/api/polls/' + vote_id + '/' + choice_id)
        .map(res => res.json());
    }
}

