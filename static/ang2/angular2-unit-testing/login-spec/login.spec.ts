import {LoginComponent} from "../../app/header/login/login.component";

describe('Login spec', () => {
    let fakeService:any;
    let loginComp:any;

    //___CONFIG___
    let TEST_COUNT:number = 100;
    let MIN_NAME_LENGTH:number = 3;
    let MIN_PASS_LENGTH:number = 4;
    let MAX_CHAR:number = 20;
    let GOOD_NAME = 'Admin';
    let GOOD_Pass = '12345qwer';
    let GOOD_MAIL = 'admin@isgod.com';

    function rndString(min:number, max:number, special:string):string {
        var text = "";
        var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
        var safeSpecial = "-_$*!";
        var unsafeSpecial = ".\-_$@*!";
        var badSpecial = "#%^()<>'\"\\\/ []|~";

        var possibleSpecial:string;
        switch (special) {
            case 'safe':
                possibleSpecial = safeSpecial;
                break;
            case 'unsafe':
                possibleSpecial = unsafeSpecial;
                break;
            case 'bad':
                possibleSpecial = badSpecial;
                break;
            case 'None':
                possibleSpecial = possible;
                break;
            case 'safeLiteral':
                possible = possible.slice(0, -10);
                possibleSpecial = possible;
                break;
            default:
                throw {message: "'special' parameter is incorrect"}
        }

        var length = Math.round(min + Math.random() * (max - min));
        var insertChars:string;

        for (var i = 0; i < length; i++) {
            if (i % 2 === 0) {
                insertChars = possible;
            } else {
                insertChars = possibleSpecial
            }
            text += insertChars.charAt(Math.floor(Math.random() * insertChars.length));
        }
        return text;
    }

    function rndMail(min:number, max:number, good:boolean):string {
        if(good) {
            var login = rndString(min, max, 'safe');
            var domain = rndString(min, max, 'None');
            var zone = rndString(2, 10, 'safeLiteral');
        } else {
            var login = rndString(min, max, 'bad');
            var domain = rndString(min, max, 'bad');
            var zone = rndString(0, 10, 'bad');
        }
        return login + '@' + domain + '.' + zone;
    }

    beforeEach(() => {
        fakeService = {
            'loginArgs': [],
            'regArgs': [],
            'register': function (...args) {
                this.regArgs = args;
                return this;
            },
            'login': function (...args) {
                this.loginArgs = args;
                return this;
            },
            'subscribe': function (cb_success:any, cb_err:any) {
                cb_success({'err': true});
            }
        };
        loginComp = new LoginComponent(fakeService);
        //override due to current token(in browser locStore) corruption
        LoginComponent.prototype.setToken = function(tokken){};
    });

    it('login vs rnd strings', () => {
        for (let i = 0; i < TEST_COUNT; i++) {
            let rndLog = rndString(MIN_NAME_LENGTH, MAX_CHAR, 'safe');
            loginComp.logName = rndLog;

            let rndPass = rndString(MIN_PASS_LENGTH, MAX_CHAR, 'safe');
            loginComp.logPass = rndPass;

            loginComp.login();
            expect(fakeService.loginArgs).toEqual([rndLog, rndPass]);
            fakeService.loginArgs = [];
        }
    });

    it('register vs rnd strings', () => {
        for (let i = 0; i < TEST_COUNT; i++) {
            let rndLog = rndString(MIN_NAME_LENGTH, MAX_CHAR, 'unsafe');
            loginComp.regName = rndLog;

            let rndPass = rndString(MIN_PASS_LENGTH, MAX_CHAR, 'unsafe');
            loginComp.regPass1 = rndPass;
            loginComp.regPass2 = rndPass;

            let randMail = rndMail(MIN_PASS_LENGTH, MAX_CHAR, true);
            loginComp.regMail = randMail;

            loginComp.register();
            expect(fakeService.regArgs).toEqual([rndLog, rndPass, randMail]);
            fakeService.regArgs = [];
            //expect(loginComp.regErr).toEqual('Sorry, that username already exists!');
        }
    });

    it('register vs low length name', () => {
        for (let i = 0; i < TEST_COUNT; i++) {
            let rndLog = rndString(0, MIN_NAME_LENGTH - 1, 'unsafe');
            loginComp.regName = rndLog;

            loginComp.regPass1 = GOOD_Pass;
            loginComp.regPass2 = GOOD_Pass;

            loginComp.regMail = GOOD_MAIL;

            loginComp.register();
            expect(loginComp.regNameValid()).toBe(false);
            expect(fakeService.regArgs).toEqual([]);
            fakeService.regArgs = [];
        }
    });

    it('register vs low length pass', () => {
        for (let i = 0; i < TEST_COUNT; i++) {
            loginComp.regName = GOOD_NAME;

            let rndPass = rndString(0, MIN_PASS_LENGTH - 1, 'unsafe');
            loginComp.regPass1 = rndPass;
            loginComp.regPass2 = rndPass;

            loginComp.regMail = GOOD_MAIL;

            loginComp.register();
            expect(loginComp.regPass1Valid()).toBe(false);
            expect(fakeService.regArgs).toEqual([]);
            fakeService.regArgs = [];
        }
    });

    it('register vs bad name', () => {
        for (let i = 0; i < TEST_COUNT; i++) {
            let rndLog = rndString(MIN_NAME_LENGTH, MAX_CHAR, 'bad');
            loginComp.regName = rndLog;

            loginComp.regPass1 = GOOD_Pass;
            loginComp.regPass2 = GOOD_Pass;

            loginComp.regMail = GOOD_MAIL;

            loginComp.register();
            expect(loginComp.regNameValid()).toBe(false);
            expect(fakeService.regArgs).toEqual([]);
            fakeService.regArgs = [];
        }
    });

    it('register vs bad mail', () => {
        for (let i = 0; i < TEST_COUNT; i++) {
            loginComp.regName = GOOD_NAME;

            loginComp.regPass1 = GOOD_Pass;
            loginComp.regPass2 = GOOD_Pass;

            let randMail = rndMail(0, 20, false);
            loginComp.regMail = randMail;

            loginComp.register();
            expect(loginComp.regMailValid()).toBe(false);
            expect(fakeService.regArgs).toEqual([]);
            fakeService.regArgs = [];
        }
    });

});
