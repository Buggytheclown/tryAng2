System.register(["../../static", "angular2/core", "../login/login.component", "angular2-jwt"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var static_1, core_1, login_component_1, angular2_jwt_1;
    var HeaderComponent;
    return {
        setters:[
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (login_component_1_1) {
                login_component_1 = login_component_1_1;
            },
            function (angular2_jwt_1_1) {
                angular2_jwt_1 = angular2_jwt_1_1;
            }],
        execute: function() {
            HeaderComponent = (function () {
                function HeaderComponent(_JwtHelper) {
                    this._JwtHelper = _JwtHelper;
                    this.showSign = '';
                }
                HeaderComponent.prototype.authenticated = function () {
                    return angular2_jwt_1.tokenNotExpired();
                };
                HeaderComponent.prototype.Logout = function () {
                    localStorage.removeItem('id_token');
                };
                HeaderComponent.prototype.decodeToken = function () {
                    try {
                        var token = localStorage.getItem('id_token');
                        return this._JwtHelper.decodeToken(token);
                    }
                    catch (err) {
                    }
                };
                HeaderComponent.prototype.getUsername = function () {
                    return this.decodeToken().username;
                };
                HeaderComponent = __decorate([
                    core_1.Component({
                        selector: 'my-header',
                        templateUrl: static_1.SrcURL + 'header/header.html',
                        styleUrls: [static_1.SrcURL + 'header/header.css'],
                        directives: [login_component_1.LoginComponent],
                        providers: [angular2_jwt_1.JwtHelper],
                    }), 
                    __metadata('design:paramtypes', [angular2_jwt_1.JwtHelper])
                ], HeaderComponent);
                return HeaderComponent;
            })();
            exports_1("HeaderComponent", HeaderComponent);
        }
    }
});
//# sourceMappingURL=header.js.map