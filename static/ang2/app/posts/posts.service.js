System.register(["angular2/core", "angular2/http", 'rxjs/add/operator/map', 'rxjs/add/operator/delay', 'angular2-jwt'], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, http_1, http_2, angular2_jwt_1;
    var PostsService;
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
            function (_2) {},
            function (angular2_jwt_1_1) {
                angular2_jwt_1 = angular2_jwt_1_1;
            }],
        execute: function() {
            PostsService = (function () {
                function PostsService(_http, _AuthHttp) {
                    this._http = _http;
                    this._AuthHttp = _AuthHttp;
                }
                ;
                //getPosts(from, to) {return this._http.get('/api/posts/'+'?postFrom=' + from + '&postTo=' + to).delay(500)
                //        // Call map on the response observable to get the parsed people object
                //        .map(res => res.json());
                //        // Subscribe to the observable to get the parsed people object and attach it to the
                //        // component
                //}
                PostsService.prototype.getPosts = function (from, to, date) {
                    return this._AuthHttp.get('/api/PiParse/' + '?postFrom=' + from + '&postTo=' + to + '&date=' + date)
                        .map(function (res) { return res.json(); });
                    // Subscribe to the observable to get the parsed people object and attach it to the
                    // component
                };
                PostsService.prototype.saveViewed = function (viewed) {
                    var headers = new http_2.Headers();
                    headers.append('X-CSRFToken', this.getCookie('csrftoken'));
                    headers.append('Content-Type', 'application/json');
                    var body = JSON.stringify({ 'viewed': viewed });
                    return this._AuthHttp.post('/api/viewed/', body, { headers: headers })
                        .map(function (res) { return res.json(); });
                };
                PostsService.prototype.getCookie = function (name) {
                    var value = "; " + document.cookie;
                    var parts = value.split("; " + name + "=");
                    if (parts.length == 2)
                        return parts.pop().split(";").shift();
                };
                PostsService = __decorate([
                    core_1.Injectable(), 
                    __metadata('design:paramtypes', [http_1.Http, angular2_jwt_1.AuthHttp])
                ], PostsService);
                return PostsService;
            })();
            exports_1("PostsService", PostsService);
        }
    }
});
//# sourceMappingURL=posts.service.js.map