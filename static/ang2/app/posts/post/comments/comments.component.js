System.register(["angular2/core", "../../../../static", "./comments.service", "./comment/comment"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, comments_service_1, comment_1, core_2;
    var CommentsComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
                core_2 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (comments_service_1_1) {
                comments_service_1 = comments_service_1_1;
            },
            function (comment_1_1) {
                comment_1 = comment_1_1;
            }],
        execute: function() {
            CommentsComponent = (function () {
                function CommentsComponent(_CommentsService) {
                    this._CommentsService = _CommentsService;
                }
                CommentsComponent.prototype.ngOnInit = function () {
                    this.getComment(this.url);
                    //this._CommentsService.getMockComments().then(comments=>this.comments = comments);
                };
                CommentsComponent.prototype.getComment = function (url) {
                    var _this = this;
                    this._CommentsService.getComments(url).subscribe(function (comments) {
                        _this.comments = comments;
                    }, function (err) {
                        console.log(err);
                    });
                };
                __decorate([
                    core_2.Input(), 
                    __metadata('design:type', Object)
                ], CommentsComponent.prototype, "url", void 0);
                CommentsComponent = __decorate([
                    core_1.Component({
                        selector: 'my-comments',
                        templateUrl: static_1.SrcURL + 'posts/post/comments/comments.html',
                        styleUrls: [static_1.SrcURL + 'posts/post/comments/comments.css'],
                        directives: [comment_1.CommentComponent],
                        providers: [comments_service_1.CommentsService],
                    }), 
                    __metadata('design:paramtypes', [comments_service_1.CommentsService])
                ], CommentsComponent);
                return CommentsComponent;
            })();
            exports_1("CommentsComponent", CommentsComponent);
        }
    }
});
//# sourceMappingURL=comments.component.js.map