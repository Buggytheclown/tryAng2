System.register(["angular2/core", "angular2/http", 'rxjs/add/operator/map', 'rxjs/add/operator/delay'], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, http_1, http_2;
    var LoginService;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
                http_2 = http_1_1;
            },
            function (_1) {},
            function (_2) {}],
        execute: function() {
            LoginService = (function () {
                function LoginService(_http) {
                    this._http = _http;
                }
                ;
                LoginService.prototype.login = function (name, pass) {
                    var body = JSON.stringify({ 'username': name, 'password': pass });
                    var headers = new http_2.Headers();
                    headers.append('Content-Type', 'application/json');
                    return this._http.post('/api-token-auth/', body, { headers: headers })
                        .map(function (res) { return res.json(); });
                };
                LoginService.prototype.register = function (name, pass, email) {
                    var headers = new http_2.Headers();
                    headers.append('X-CSRFToken', this.getCookie('csrftoken'));
                    headers.append('Content-Type', 'application/json');
                    var body = JSON.stringify({ 'username': name, 'password': pass, 'email': email });
                    return this._http.post('/api-register/', body, { headers: headers })
                        .map(function (res) { return res.json(); });
                };
                LoginService.prototype.getCookie = function (name) {
                    var value = "; " + document.cookie;
                    var parts = value.split("; " + name + "=");
                    if (parts.length == 2)
                        return parts.pop().split(";").shift();
                };
                LoginService = __decorate([
                    core_1.Injectable(), 
                    __metadata('design:paramtypes', [http_1.Http])
                ], LoginService);
                return LoginService;
            })();
            exports_1("LoginService", LoginService);
        }
    }
});
//# sourceMappingURL=login.service.js.map