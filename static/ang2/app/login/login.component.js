System.register(["angular2/core", "../../static", "./login.service", "angular2-jwt"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, login_service_1, angular2_jwt_1;
    var LoginComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (login_service_1_1) {
                login_service_1 = login_service_1_1;
            },
            function (angular2_jwt_1_1) {
                angular2_jwt_1 = angular2_jwt_1_1;
            }],
        execute: function() {
            LoginComponent = (function () {
                function LoginComponent(_LoginService) {
                    this._LoginService = _LoginService;
                    this.showFormContent = 0;
                    this.jwtHelper = new angular2_jwt_1.JwtHelper();
                    this.pass2CleanColor = 'black';
                    this.loginErr = false;
                    this.canRegister = false;
                }
                LoginComponent.prototype.pass1 = function (value) {
                    this.pass1Check = value;
                    if (this.pass2Check && this.pass1Check !== this.pass2Check) {
                        this.pass2CleanColor = 'red';
                    }
                };
                LoginComponent.prototype.pass2 = function (value) {
                    this.pass2Check = value;
                    this.pass2CleanColor = 'red';
                    if (this.pass1Check === value) {
                        this.pass2CleanColor = 'green';
                        this.canRegister = true;
                    }
                };
                LoginComponent.prototype.login = function (name, pass) {
                    var _this = this;
                    this._LoginService.login(name, pass).subscribe(function (res) {
                        console.log('logged in');
                        localStorage.setItem('id_token', res.token);
                    }, function (err) {
                        console.log('err', err);
                        _this.loginErr = true;
                    });
                };
                LoginComponent.prototype.register = function (name, pass1, pass2, email) {
                    var _this = this;
                    this.registerErr = "";
                    if (pass1 === pass2) {
                        this._LoginService.register(name, pass1, email).subscribe(function (res) {
                            if (!res.err) {
                                localStorage.setItem('id_token', res.token);
                            }
                            else {
                                console.log('err1', res.err);
                                _this.registerErr = res.err;
                            }
                        }, function (err) {
                            console.log('err2', err);
                        });
                    }
                    else {
                        this.pass2CleanColor = 'red';
                        this.registerErr = 'Sorry, password dont match!';
                    }
                };
                LoginComponent.prototype.Test = function () {
                    var tok = localStorage.getItem('id_token');
                    console.log(tok);
                };
                LoginComponent.prototype.Logout = function () {
                    localStorage.removeItem('id_token');
                };
                LoginComponent.prototype.loggedin = function () {
                    return angular2_jwt_1.tokenNotExpired();
                };
                LoginComponent.prototype.expDate = function () {
                    try {
                        var token = localStorage.getItem('id_token');
                        return this.jwtHelper.getTokenExpirationDate(token);
                    }
                    catch (err) { }
                };
                LoginComponent.prototype.decodeToken = function () {
                    try {
                        var token = localStorage.getItem('id_token');
                        return this.jwtHelper.decodeToken(token);
                    }
                    catch (err) { }
                };
                LoginComponent = __decorate([
                    core_1.Component({
                        selector: 'my-login',
                        templateUrl: static_1.SrcURL + 'login/login.html',
                        styleUrls: [static_1.SrcURL + 'login/login.css'],
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