import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {LoginService} from "./login.service";
import {tokenNotExpired, JwtHelper} from "angular2-jwt";
import {Input} from "angular2/core";
import {Output} from "angular2/core";
import {EventEmitter} from "angular2/core";


@Component({
    selector: 'my-login',
    templateUrl: SrcURL + 'login/login.html',
    styleUrls: [SrcURL + 'login/login.css'],
    directives: [],
    providers: [LoginService, JwtHelper],
})

export class LoginComponent {
    @Input()showFormContent;
    @Output() closeLogReg = new EventEmitter();
    //jwtHelper: JwtHelper = new JwtHelper();

    //Login
    loginErr:boolean = false;
    logName:string = '';
    logPass:string = '';

    //Register
    regName:string = '';
    regMail:string = '';
    regPass1:string = '';
    regPass2:string = '';
    regErr:string = '';

    passCheckColor:string = '';
    passCheckWidth:number = 0;

    constructor(private _LoginService:LoginService, private _JwtHelper:JwtHelper) {
    }

    closeme() {
        this.closeLogReg.emit(true)
    }

    // *****
    // LOGIN
    //******

    canLogin():boolean {
        if (this.logName.length > 0 && this.logPass.length > 0) {
            return true
        } else {
            return false
        }
    }

    login():void {
        if (this.canLogin()) {
            this._LoginService.login(this.logName, this.logPass).subscribe(
                (res)=> {
                    this.logPass = '';
                    this.logName = '';
                    localStorage.setItem('id_token', res.token)
                },
                (err)=> {
                    console.log('err', err);
                    this.logPass = '';
                    if (!this.loginErr) {
                        this.loginErr = true;
                        setTimeout(()=> {
                            this.loginErr = false;
                        }, 3000)
                    }
                }
            )
        }
    }

    // *****
    // REGISTER
    //******

    //__validators__
    regNameValid():boolean {
        let re = /^[a-zA-Z0-9.\-_$@*!]{3,30}$/;
        return re.test(this.regName);
    }

    regPass1Valid():boolean {
        if (this.regPass1.length > 3) {
            return true
        } else {
            return false
        }
    }

    regMailValid():boolean {
        var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(this.regMail);
    }

    passMatch():boolean {
        if (this.regPass1 && this.regPass1 === this.regPass2) {
            return true
        } else {
            return false
        }
    }

    //__end validators__

    //compare validators
    canRegister():boolean {
        if (this.regPass1Valid() && this.passMatch() && this.regNameValid() && this.regMailValid()) {
            return true
        } else {
            return false
        }
    }

    showRegValidErr() {
        if (!this.regNameValid()) {
            if (!this.regErr) {
                this.regErr = "Error: bad username";
                this.regName = '';
                this.regErrDelayClaer();
            }
        } else if (!this.regMailValid()) {
            if (!this.regErr) {
                this.regErr = "Error: bad e-mail";
                this.regMail = '';
                this.regErrDelayClaer();
            }
        } else if (!this.passMatch()) {
            if (!this.regErr) {
                this.regErr = "Error: password didn't match";
                this.clearRegPass();
                this.regErrDelayClaer();
            }
        } else if (!this.regPass1Valid()) {
            if (!this.regErr) {
                this.regErr = "Error: password too short";
                this.clearRegPass();
                this.regErrDelayClaer();
            }
        }
    }

    register() {
        if (this.canRegister()) {
            this._LoginService.register(this.regName, this.regPass1, this.regMail).subscribe(
                (res)=> {
                    this.clearRegPass();
                    if (!res.err) {
                        localStorage.setItem('id_token', res.token)
                    } else {
                        console.log('err1', res.err);
                        if (!this.regErr) {
                            this.regErr = 'Sorry, that username already exists!';
                            this.regErrDelayClaer();
                        }
                    }
                },
                (err)=> {
                    console.log('err2', err)
                }
            )
        } else (this.showRegValidErr())
    }

    clearRegPass() {
        this.regPass1 = '';
        this.regPass2 = '';
        this.setPasswordAnalizer();
    }

    regErrDelayClaer() {
        setTimeout(()=> {
            this.regErr = '';
        }, 3000)
    }

    setPasswordAnalizer() {
        this.passwordAnalizer.setScore(this.regPass1);
        this.passCheckColor = this.passwordAnalizer.getComplexityColor();
        this.passCheckWidth = this.passwordAnalizer.getComplexity();
        if (this.regPass1.length === 0) {
            this.passCheckWidth = 0;
        } else if (this.regPass1.length > 0 && this.passCheckWidth === 0) {
            this.passCheckWidth = this.regPass1.length;
        }
        //console.log('COLOR:', this.passCheckColor, 'WIDTH:', this.passCheckWidth)
    }

    passwordAnalizer = {
        MIN_PASSWORD_LENGTH: 6,
        BONUS_EXCESS: 2, //was 3
        BONUS_UPPER: 4,
        BONUS_NUMBERS: 5,
        BONUS_SYMBOLS: 5,
        score: undefined,

        setScore(password:string): void {
            let baseScore = 50;

            let numExcess = 0;
            let numUpper = 0;
            let numNumbers = 0;
            let numSybols = 0;

            let bonusCombo = 0;
            let bonusFlatLower = 0;
            let bonusFlatNumber = 0;

            for (let i = 0; i < password.length; i++) {
                if (password[i].match(/[A-Z]/g)) {
                    numUpper++;
                }
                if (password[i].match(/[0-9]/g)) {
                    numNumbers++;
                }
                if (password[i].match(/(.*[!,@,#,$,%,^,&,*,?,_,~])/)) {
                    numSybols++;
                }
            }

            numExcess = password.length - this.MIN_PASSWORD_LENGTH;

            switch (password.length) {
                case 0:
                    baseScore -= 50;
                    break;
                case 1:
                    baseScore -= 40;
                    break;
                case 2:
                    baseScore -= 30;
                    break;
                case 3:
                    baseScore -= 20;
                    break;
                case 4:
                    baseScore -= 10;
                    break;
            }

            if (this.numUpper && this.numNumbers && this.numSybols) {
                bonusCombo = 25;
            }

            else if ((this.numUpper && this.numNumbers) || (this.numUpper && this.numSybols) || (this.numNumbers && this.numSybols)) {
                bonusCombo = 15;
            }

            if (password.match(/^[\sa-z]+$/)) {
                bonusFlatLower = -15;
            }

            if (password.match(/^[\s0-9]+$/)) {
                bonusFlatNumber = -35;
            }

            this.score = baseScore + (numExcess * this.BONUS_EXCESS) + (numUpper * this.BONUS_UPPER) + (numNumbers * this.BONUS_NUMBERS) +
                (numSybols * this.BONUS_SYMBOLS) + bonusCombo + bonusFlatLower + bonusFlatNumber;
            this.score -= 25;
        },

        getComplexity(): number {
            let score = this.score;

            if (score < 0) {
                score = 0
            }
            if (score > 100) {
                score = 100
            }
            return score
        },

        getComplexityColor() {
            if (this.score < 25) {
                //return '#5cb85c';
                return 'progress-bar-danger';
            }
            else if (this.score >= 25 && this.score < 50) {
                //return '#f0ad4e';
                return 'progress-bar-warning';
            }
            else if (this.score >= 50 && this.score < 75) {
                //return '#5bc0de';
                return 'progress-bar-info';
            }
            else if (this.score >= 75) {
                //return '#d9534f';
                return 'progress-bar-success';
            }
        },

    };


    // *****
    // TEST
    //******

    Test() {
        let tok = localStorage.getItem('id_token');
        console.log(tok);
    }

    Logout() {
        localStorage.removeItem('id_token');
    }

    loggedin() {
        return tokenNotExpired();
    }

    expDate() {
        try {
            let token = localStorage.getItem('id_token');
            return this._JwtHelper.getTokenExpirationDate(token);
        } catch (err) {
        }
    }

    decodeToken() {
        try {
            let token = localStorage.getItem('id_token');
            return this._JwtHelper.decodeToken(token);
        } catch (err) {
        }
    }
}