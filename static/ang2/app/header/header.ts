import {SrcURL} from "../../static";
import {Component} from "angular2/core";
import {LoginComponent} from "../login/login.component";
import {tokenNotExpired, JwtHelper} from "angular2-jwt";

@Component({
    selector: 'my-header',
    templateUrl: SrcURL + 'header/header.html',
    styleUrls: [SrcURL + 'header/header.css'],
    directives: [LoginComponent],
    providers: [JwtHelper],
})

export class HeaderComponent {
    showSign:string='';

    constructor(private _JwtHelper: JwtHelper){}

    authenticated() {
        return tokenNotExpired();
    }

    Logout() {
        localStorage.removeItem('id_token');
    }

    decodeToken() {
        try {
            let token = localStorage.getItem('id_token');
            return this._JwtHelper.decodeToken(token);
        } catch (err) {
        }
    }

    getUsername(){
        return this.decodeToken().username
    }
}