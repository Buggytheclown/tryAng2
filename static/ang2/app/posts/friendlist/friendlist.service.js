System.register(["angular2/core", "angular2/http", 'rxjs/add/operator/map', 'angular2-jwt', "../../helpers/headersUnsafe"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, http_1, angular2_jwt_1, headersUnsafe_1;
    var FriendlistService;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            },
            function (_1) {},
            function (angular2_jwt_1_1) {
                angular2_jwt_1 = angular2_jwt_1_1;
            },
            function (headersUnsafe_1_1) {
                headersUnsafe_1 = headersUnsafe_1_1;
            }],
        execute: function() {
            FriendlistService = (function () {
                function FriendlistService(_http, _AuthHttp, _headersUnsafe) {
                    this._http = _http;
                    this._AuthHttp = _AuthHttp;
                    this._headersUnsafe = _headersUnsafe;
                }
                ;
                FriendlistService.prototype.getFriendlist = function () {
                    return this._AuthHttp.get('/api/friendlist/')
                        .map(function (res) { return res.json(); });
                };
                FriendlistService.prototype.deleteFriend = function (user) {
                    var headers = this._headersUnsafe.getHeaders();
                    var body = JSON.stringify({ 'friend': user });
                    return this._AuthHttp.patch('/api/friendlist/', body, headers)
                        .map(function (res) { return res.json(); });
                };
                FriendlistService.prototype.addFriend = function (user) {
                    var headers = this._headersUnsafe.getHeaders();
                    var body = JSON.stringify({ 'friend': user });
                    return this._AuthHttp.put('/api/friendlist/', body, headers)
                        .map(function (res) { return res.json(); });
                };
                FriendlistService = __decorate([
                    core_1.Injectable(), 
                    __metadata('design:paramtypes', [http_1.Http, angular2_jwt_1.AuthHttp, headersUnsafe_1.headersUnsafe])
                ], FriendlistService);
                return FriendlistService;
            })();
            exports_1("FriendlistService", FriendlistService);
        }
    }
});
//# sourceMappingURL=friendlist.service.js.map