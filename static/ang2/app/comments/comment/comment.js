System.register(["angular2/core", "../../../static", "../../helpers/dateFromUTC"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, core_2, dateFromUTC_1;
    var CommentComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
                core_2 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (dateFromUTC_1_1) {
                dateFromUTC_1 = dateFromUTC_1_1;
            }],
        execute: function() {
            CommentComponent = (function () {
                function CommentComponent() {
                    this.countChildrens = 0;
                }
                CommentComponent.prototype.ngOnInit = function () {
                    this.setCountChildrens(this.comment.child);
                };
                CommentComponent.prototype.setCountChildrens = function (comments) {
                    for (var i = 0; i < comments.length; i++) {
                        this.countChildrens++;
                        if (comments[i].child.length > 0) {
                            this.setCountChildrens(comments[i].child);
                        }
                    }
                };
                __decorate([
                    core_2.Input(), 
                    __metadata('design:type', Object)
                ], CommentComponent.prototype, "comment", void 0);
                __decorate([
                    core_2.Input(), 
                    __metadata('design:type', Object)
                ], CommentComponent.prototype, "showChild", void 0);
                CommentComponent = __decorate([
                    core_1.Component({
                        selector: 'my-comment',
                        //recursive links
                        templateUrl: static_1.SrcURL + 'comments/comment/comment.html',
                        styleUrls: [static_1.SrcURL + 'comments/comment/comment.css'],
                        directives: [CommentComponent],
                        providers: [],
                        pipes: [dateFromUTC_1.DateFromUTCPipe]
                    }), 
                    __metadata('design:paramtypes', [])
                ], CommentComponent);
                return CommentComponent;
            })();
            exports_1("CommentComponent", CommentComponent);
        }
    }
});
//# sourceMappingURL=comment.js.map