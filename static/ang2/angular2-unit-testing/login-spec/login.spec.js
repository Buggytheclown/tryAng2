System.register(["../../app/header/login/login.component"], function(exports_1) {
    var login_component_1;
    return {
        setters:[
            function (login_component_1_1) {
                login_component_1 = login_component_1_1;
            }],
        execute: function() {
            describe('Login spec', function () {
                var fakeService;
                var loginComp;
                //___CONFIG___
                var TEST_COUNT = 100;
                var MIN_NAME_LENGTH = 3;
                var MIN_PASS_LENGTH = 4;
                var MAX_CHAR = 20;
                var GOOD_NAME = 'Admin';
                var GOOD_Pass = '12345qwer';
                var GOOD_MAIL = 'admin@isgod.com';
                function rndString(min, max, special) {
                    var text = "";
                    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
                    var safeSpecial = "-_$*!";
                    var unsafeSpecial = ".\-_$@*!";
                    var badSpecial = "#%^()<>'\"\\\/ []|~";
                    var possibleSpecial;
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
                            throw { message: "'special' parameter is incorrect" };
                    }
                    var length = Math.round(min + Math.random() * (max - min));
                    var insertChars;
                    for (var i = 0; i < length; i++) {
                        if (i % 2 === 0) {
                            insertChars = possible;
                        }
                        else {
                            insertChars = possibleSpecial;
                        }
                        text += insertChars.charAt(Math.floor(Math.random() * insertChars.length));
                    }
                    return text;
                }
                function rndMail(min, max, good) {
                    if (good) {
                        var login = rndString(min, max, 'safe');
                        var domain = rndString(min, max, 'None');
                        var zone = rndString(2, 10, 'safeLiteral');
                    }
                    else {
                        var login = rndString(min, max, 'bad');
                        var domain = rndString(min, max, 'bad');
                        var zone = rndString(0, 10, 'bad');
                    }
                    return login + '@' + domain + '.' + zone;
                }
                beforeEach(function () {
                    fakeService = {
                        'loginArgs': [],
                        'regArgs': [],
                        'register': function () {
                            var args = [];
                            for (var _i = 0; _i < arguments.length; _i++) {
                                args[_i - 0] = arguments[_i];
                            }
                            this.regArgs = args;
                            return this;
                        },
                        'login': function () {
                            var args = [];
                            for (var _i = 0; _i < arguments.length; _i++) {
                                args[_i - 0] = arguments[_i];
                            }
                            this.loginArgs = args;
                            return this;
                        },
                        'subscribe': function (cb_success, cb_err) {
                            cb_success({ 'err': true });
                        }
                    };
                    loginComp = new login_component_1.LoginComponent(fakeService);
                    //override due to current token(in browser locStore) corruption
                    login_component_1.LoginComponent.prototype.setToken = function (tokken) { };
                });
                it('login vs rnd strings', function () {
                    for (var i = 0; i < TEST_COUNT; i++) {
                        var rndLog = rndString(MIN_NAME_LENGTH, MAX_CHAR, 'safe');
                        loginComp.logName = rndLog;
                        var rndPass = rndString(MIN_PASS_LENGTH, MAX_CHAR, 'safe');
                        loginComp.logPass = rndPass;
                        loginComp.login();
                        expect(fakeService.loginArgs).toEqual([rndLog, rndPass]);
                        fakeService.loginArgs = [];
                    }
                });
                it('register vs rnd strings', function () {
                    for (var i = 0; i < TEST_COUNT; i++) {
                        var rndLog = rndString(MIN_NAME_LENGTH, MAX_CHAR, 'unsafe');
                        loginComp.regName = rndLog;
                        var rndPass = rndString(MIN_PASS_LENGTH, MAX_CHAR, 'unsafe');
                        loginComp.regPass1 = rndPass;
                        loginComp.regPass2 = rndPass;
                        var randMail = rndMail(MIN_PASS_LENGTH, MAX_CHAR, true);
                        loginComp.regMail = randMail;
                        loginComp.register();
                        expect(fakeService.regArgs).toEqual([rndLog, rndPass, randMail]);
                        fakeService.regArgs = [];
                    }
                });
                it('register vs low length name', function () {
                    for (var i = 0; i < TEST_COUNT; i++) {
                        var rndLog = rndString(0, MIN_NAME_LENGTH - 1, 'unsafe');
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
                it('register vs low length pass', function () {
                    for (var i = 0; i < TEST_COUNT; i++) {
                        loginComp.regName = GOOD_NAME;
                        var rndPass = rndString(0, MIN_PASS_LENGTH - 1, 'unsafe');
                        loginComp.regPass1 = rndPass;
                        loginComp.regPass2 = rndPass;
                        loginComp.regMail = GOOD_MAIL;
                        loginComp.register();
                        expect(loginComp.regPass1Valid()).toBe(false);
                        expect(fakeService.regArgs).toEqual([]);
                        fakeService.regArgs = [];
                    }
                });
                it('register vs bad name', function () {
                    for (var i = 0; i < TEST_COUNT; i++) {
                        var rndLog = rndString(MIN_NAME_LENGTH, MAX_CHAR, 'bad');
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
                it('register vs bad mail', function () {
                    for (var i = 0; i < TEST_COUNT; i++) {
                        loginComp.regName = GOOD_NAME;
                        loginComp.regPass1 = GOOD_Pass;
                        loginComp.regPass2 = GOOD_Pass;
                        var randMail = rndMail(0, 20, false);
                        loginComp.regMail = randMail;
                        loginComp.register();
                        expect(loginComp.regMailValid()).toBe(false);
                        expect(fakeService.regArgs).toEqual([]);
                        fakeService.regArgs = [];
                    }
                });
            });
        }
    }
});
//# sourceMappingURL=login.spec.js.map