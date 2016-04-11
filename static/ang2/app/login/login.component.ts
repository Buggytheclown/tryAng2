import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {LoginService} from "./login.service";
import {tokenNotExpired, JwtHelper} from "angular2-jwt";

@Component({
    selector: 'my-login',
    templateUrl:SrcURL+'login/login.html',
    styleUrls: [SrcURL+'login/login.css'],
    directives: [],
    providers: [LoginService],
})

export class LoginComponent {
    showFormContent:number = 0;
    jwtHelper: JwtHelper = new JwtHelper();
    pass1Check:string;
    pass2Check:string;
    pass2CleanColor:string = 'black';
    loginErr:boolean = false;
    canRegister:boolean = false;
    registerErr:string;

    constructor(private _LoginService:LoginService){}

    pass1(value){
        this.pass1Check=value;
        if(this.pass2Check && this.pass1Check !== this.pass2Check){
            this.pass2CleanColor = 'red';
        }
    }

    pass2(value){
        this.pass2Check=value;
        this.pass2CleanColor = 'red';
        if(this.pass1Check===value){
            this.pass2CleanColor = 'green';
            this.canRegister = true;
        }
    }

    login(name, pass){
        this._LoginService.login(name, pass).subscribe(
            (res)=>{
                console.log('logged in');
                localStorage.setItem('id_token', res.token )
            },
            (err)=>{
                console.log('err', err);
                this.loginErr = true;
            }
        )
    }

    register(name, pass1, pass2, email){
        this.registerErr = "";
        if(pass1===pass2) {
            this._LoginService.register(name, pass1, email).subscribe(
                (res)=> {
                    if(!res.err){
                        localStorage.setItem('id_token', res.token )
                    }else {
                        console.log('err1', res.err);
                        this.registerErr = res.err;
                    }
                },
                (err)=> {
                    console.log('err2', err)
                }
            )
        }else {
            this.pass2CleanColor = 'red';
            this.registerErr = 'Sorry, password dont match!';
        }
    }

    Test(){
        let tok = localStorage.getItem('id_token');
        console.log(tok);
    }

    Logout(){
        localStorage.removeItem('id_token');
    }

    loggedin(){
        return tokenNotExpired();
    }

    expDate(){
        try{
            let token = localStorage.getItem('id_token');
            return this.jwtHelper.getTokenExpirationDate(token);
        }catch (err){}
    }

    decodeToken(){
         try{
            let token = localStorage.getItem('id_token');
            return this.jwtHelper.decodeToken(token);
        }catch (err){}
    }
}