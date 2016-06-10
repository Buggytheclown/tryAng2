System.register(["angular2/core", "./mock-comments", 'angular2-jwt', "angular2/http"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, mock_comments_1, angular2_jwt_1, http_1;
    var CommentsService;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (mock_comments_1_1) {
                mock_comments_1 = mock_comments_1_1;
            },
            function (angular2_jwt_1_1) {
                angular2_jwt_1 = angular2_jwt_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
            }],
        execute: function() {
            CommentsService = (function () {
                function CommentsService(_http, _AuthHttp) {
                    this._http = _http;
                    this._AuthHttp = _AuthHttp;
                }
                ;
                CommentsService.prototype.getMockComments = function () {
                    return Promise.resolve(mock_comments_1.COMMENTS);
                };
                CommentsService.prototype.getComments = function (url) {
                    return this._AuthHttp.get('/api/comments/' + '?page=' + url)
                        .map(function (res) { return res.json(); });
                };
                CommentsService = __decorate([
                    core_1.Injectable(), 
                    __metadata('design:paramtypes', [http_1.Http, angular2_jwt_1.AuthHttp])
                ], CommentsService);
                return CommentsService;
            })();
            exports_1("CommentsService", CommentsService);
        }
    }
});
//# sourceMappingURL=comments.service.js.map