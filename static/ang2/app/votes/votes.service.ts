import {Injectable} from "angular2/core";
import {Http} from "angular2/http";
import 'rxjs/add/operator/map';

@Injectable()
export class VotesService {
    constructor(private _http:Http) {};

    getVotes() {return this._http.get('/api/polls/')
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

