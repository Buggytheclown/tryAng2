import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {OnInit} from "angular2/core";
import {Router} from "angular2/router";
import {RouteParams} from "angular2/router";

@Component({
    selector: 'my-searchbar',
    templateUrl: SrcURL + 'searchbar/searchbar.html',
    styleUrls: [SrcURL + 'searchbar/searchbar.css'],
    directives: [],
    providers: [],
})

export class SearchbarComponent implements OnInit {

    routeDate:string;

    constructor(private _router:Router, private _routeParams:RouteParams) {
    }

    ngOnInit() {
        let someDate = this._routeParams.get('date');
        if (someDate) {
            this.routeDate = this.getReversedDate(someDate);
        } else {
            this.routeDate = this.getDateNow()
        }
    }

    routeIt(date:string):void {
        //date need to be "dd-mm-yyyy"
        let dateNow = new Date();
        let dateIn = new Date(date);
        let routeDate = '';
        let revrouteDate = '';
        if (dateIn && dateIn - dateNow <= 0) {
            revrouteDate = this.getReversedDate(date);
        } else {
            routeDate = this.getDateNow();
            revrouteDate = this.getReversedDate(routeDate);
        }
        this._router.navigate(['Posts', {date: revrouteDate}]);
    }

    getReversedDate(date:string):string {
        return date.split('-').reverse().join('-');
    }

    getDateNow():string {
        //let dateNow = new Date().toISOString().slice(0, 10);
        let currentDate = new Date();
        let day = ("0" + currentDate.getDate()).slice(-2);
        let month = ("0" + (currentDate.getMonth() + 1)).slice(-2);
        let year = currentDate.getFullYear();
        return [year, month, day].join('-');
    }
}