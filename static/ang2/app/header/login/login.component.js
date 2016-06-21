System.register(["angular2/core", "../../../static", "./login.service"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, login_service_1, core_2, core_3, core_4;
    var LoginComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
                core_2 = core_1_1;
                core_3 = core_1_1;
                core_4 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (login_service_1_1) {
                login_service_1 = login_service_1_1;
            }],
        execute: function() {
            LoginComponent = (function () {
                function LoginComponent(_LoginService) {
                    this._LoginService = _LoginService;
                    this.closeLogReg = new core_4.EventEmitter();
                    //jwtHelper: JwtHelper = new JwtHelper();
                    //Login
                    this.loginErr = false;
                    this.logName = '';
                    this.logPass = '';
                    //Register
                    this.regName = '';
                    this.regMail = '';
                    this.regPass1 = '';
                    this.regPass2 = '';
                    this.regErr = '';
                    this.passCheckColor = '';
                    this.passCheckWidth = 0;
                    //TODO remove to helpers
                    this.passwordAnalizer = {
                        MIN_PASSWORD_LENGTH: 6,
                        BONUS_EXCESS: 2,
                        BONUS_UPPER: 4,
                        BONUS_NUMBERS: 5,
                        BONUS_SYMBOLS: 5,
                        score: undefined,
                        setScore: function (password) {
                            var baseScore = 50;
                            var numExcess = 0;
                            var numUpper = 0;
                            var numNumbers = 0;
                            var numSybols = 0;
                            var bonusCombo = 0;
                            var bonusFlatLower = 0;
                            var bonusFlatNumber = 0;
                            for (var i = 0; i < password.length; i++) {
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
                        getComplexity: function () {
                            var score = this.score;
                            if (score < 0) {
                                score = 0;
                            }
                            if (score > 100) {
                                score = 100;
                            }
                            return score;
                        },
                        getComplexityColor: function () {
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
                }
                LoginComponent.prototype.closeme = function () {
                    this.closeLogReg.emit(true);
                };
                LoginComponent.prototype.setToken = function (token) {
                    localStorage.setItem('id_token', token);
                };
                // *****
                // LOGIN
                // *****
                LoginComponent.prototype.canLogin = function () {
                    if (this.logName.length > 0 && this.logPass.length > 0) {
                        return true;
                    }
                    else {
                        return false;
                    }
                };
                LoginComponent.prototype.login = function () {
                    var _this = this;
                    if (this.canLogin()) {
                        this._LoginService.login(this.logName, this.logPass).subscribe(function (res) {
                            _this.logPass = '';
                            _this.logName = '';
                            _this.setToken(res.token);
                            _this.closeme();
                        }, function (err) {
                            console.log('err', err);
                            _this.logPass = '';
                            if (!_this.loginErr) {
                                _this.loginErr = true;
                                setTimeout(function () {
                                    _this.loginErr = false;
                                }, 3000);
                            }
                        });
                    }
                };
                // *****
                // REGISTER
                // *****
                //__validators__
                LoginComponent.prototype.regNameValid = function () {
                    var re = /^[a-zA-Z0-9.\-_$@*!]{3,30}$/;
                    return re.test(this.regName);
                };
                LoginComponent.prototype.regPass1Valid = function () {
                    if (this.regPass1.length > 3) {
                        return true;
                    }
                    else {
                        return false;
                    }
                };
                LoginComponent.prototype.regMailValid = function () {
                    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                    return re.test(this.regMail);
                };
                LoginComponent.prototype.passMatch = function () {
                    if (this.regPass1 && this.regPass1 === this.regPass2) {
                        return true;
                    }
                    else {
                        return false;
                    }
                };
                //__end validators__
                //compare validators
                LoginComponent.prototype.canRegister = function () {
                    if (this.regPass1Valid() && this.passMatch() && this.regNameValid() && this.regMailValid()) {
                        return true;
                    }
                    else {
                        return false;
                    }
                };
                LoginComponent.prototype.showRegValidErr = function () {
                    if (!this.regNameValid()) {
                        if (!this.regErr) {
                            this.regErr = "Error: bad username";
                            this.regName = '';
                        }
                    }
                    else if (!this.regMailValid()) {
                        if (!this.regErr) {
                            this.regErr = "Error: bad e-mail";
                            this.regMail = '';
                        }
                    }
                    else if (!this.passMatch()) {
                        if (!this.regErr) {
                            this.regErr = "Error: password didn't match";
                            this.clearRegPass();
                        }
                    }
                    else if (!this.regPass1Valid()) {
                        if (!this.regErr) {
                            this.regErr = "Error: password too short";
                            this.clearRegPass();
                        }
                    }
                    this.regErrDelayClaer();
                };
                LoginComponent.prototype.register = function () {
                    var _this = this;
                    if (this.canRegister()) {
                        this._LoginService.register(this.regName, this.regPass1, this.regMail).subscribe(function (res) {
                            _this.clearRegPass();
                            if (!res.err) {
                                _this.setToken(res.token);
                                _this.closeme();
                            }
                            else {
                                console.log('err1', res.err);
                                if (!_this.regErr) {
                                    _this.regErr = 'Sorry, that username already exists!';
                                    _this.regErrDelayClaer();
                                }
                            }
                        }, function (err) {
                            console.log('err2', err);
                        });
                    }
                    else
                        (this.showRegValidErr());
                };
                LoginComponent.prototype.clearRegPass = function () {
                    this.regPass1 = '';
                    this.regPass2 = '';
                    this.setPasswordAnalizer();
                };
                LoginComponent.prototype.regErrDelayClaer = function () {
                    var _this = this;
                    setTimeout(function () {
                        _this.regErr = '';
                    }, 3000);
                };
                LoginComponent.prototype.setPasswordAnalizer = function () {
                    this.passwordAnalizer.setScore(this.regPass1);
                    this.passCheckColor = this.passwordAnalizer.getComplexityColor();
                    this.passCheckWidth = this.passwordAnalizer.getComplexity();
                    if (this.regPass1.length === 0) {
                        this.passCheckWidth = 0;
                    }
                    else if (this.regPass1.length > 0 && this.passCheckWidth === 0) {
                        this.passCheckWidth = this.regPass1.length;
                    }
                    //console.log('COLOR:', this.passCheckColor, 'WIDTH:', this.passCheckWidth)
                };
                __decorate([
                    core_2.Input(), 
                    __metadata('design:type', Object)
                ], LoginComponent.prototype, "showFormContent", void 0);
                __decorate([
                    core_3.Output(), 
                    __metadata('design:type', Object)
                ], LoginComponent.prototype, "closeLogReg", void 0);
                LoginComponent = __decorate([
                    core_1.Component({
                        selector: 'my-login',
                        templateUrl: static_1.SrcURL + 'header/login/login.html',
                        styleUrls: [static_1.SrcURL + 'header/login/login.css'],
                        directives: [],
                        providers: [login_service_1.LoginService],
                    }), 
                    __metadata('design:paramtypes', [login_service_1.LoginService])
                ], LoginComponent);
                return LoginComponent;
            })();
            exports_1("LoginComponent", LoginComponent);
        }
    }
});
//# sourceMappingURL=login.component.js.map