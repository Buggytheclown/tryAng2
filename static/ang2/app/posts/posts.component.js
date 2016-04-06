System.register(["angular2/core", "../../static", "./posts.service", "../helpers/sb_windowTools"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, posts_service_1, sb_windowTools_1, core_2;
    var PostsComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
                core_2 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (posts_service_1_1) {
                posts_service_1 = posts_service_1_1;
            },
            function (sb_windowTools_1_1) {
                sb_windowTools_1 = sb_windowTools_1_1;
            }],
        execute: function() {
            PostsComponent = (function () {
                function PostsComponent(element, _postsService, _sb_windowTools) {
                    this.element = element;
                    this._postsService = _postsService;
                    this._sb_windowTools = _sb_windowTools;
                    this.truncateWord = 300;
                    this.gettingPosts = true;
                    this.getPostsEnd = 10;
                    this.getPostsStart = 0;
                    this.getPostsDelta = 5;
                    this.posts = [];
                }
                ;
                PostsComponent.prototype.ngOnInit = function () {
                    this.getPosts(this.getPostsStart, this.getPostsEnd);
                };
                ;
                PostsComponent.prototype.getPosts = function (from, to) {
                    var _this = this;
                    this._postsService.getPosts(from, to)
                        .subscribe(function (posts) {
                        _this.addMeta(posts);
                        Array.prototype.push.apply(_this.posts, posts);
                        _this.gettingPosts = false;
                    });
                };
                ;
                PostsComponent.prototype.addMeta = function (posts) {
                    for (var i = 0; i < posts.length; i++) {
                        posts[i]['Meta'] = {
                            'doTrunk': true,
                            'offset': null,
                        };
                    }
                };
                ;
                PostsComponent.prototype.onScroll = function () {
                    this._sb_windowTools.updateDimensions();
                    this.scrollPercent = (this._sb_windowTools.windowHeight() + this._sb_windowTools.verticalOffset()) / this._sb_windowTools.pageHeight();
                    if (this.scrollPercent > 0.90 && !this.gettingPosts) {
                        this.getPostsEnd += this.getPostsDelta;
                        this.getPosts(this.getPostsEnd - this.getPostsDelta, this.getPostsEnd);
                        this.gettingPosts = true;
                    }
                };
                ;
                PostsComponent.prototype.stringAsDate = function (dateStr) {
                    return new Date(dateStr);
                };
                ;
                PostsComponent.prototype.getTrunkedContent = function (post_content) {
                    if (post_content.length > this.truncateWord) {
                        return post_content.slice(0, this.truncateWord);
                    }
                    else {
                        return post_content;
                    }
                };
                ;
                PostsComponent.prototype.findPosY = function (obj) {
                    var curtop = 0;
                    if (obj.offsetParent) {
                        while (1) {
                            curtop += obj.offsetTop;
                            if (!obj.offsetParent) {
                                break;
                            }
                            obj = obj.offsetParent;
                        }
                    }
                    else if (obj.y) {
                        curtop += obj.y;
                    }
                    return curtop;
                };
                PostsComponent = __decorate([
                    core_1.Component({
                        selector: 'my-posts',
                        templateUrl: static_1.SrcURL + 'html/posts.html',
                        styles: ["\n    pre{\n        white-space: pre-line;\n    }\n    "],
                        directives: [],
                        providers: [posts_service_1.PostsService, sb_windowTools_1.sb_windowTools],
                    }), 
                    __metadata('design:paramtypes', [core_2.ElementRef, posts_service_1.PostsService, sb_windowTools_1.sb_windowTools])
                ], PostsComponent);
                return PostsComponent;
            })();
            exports_1("PostsComponent", PostsComponent);
        }
    }
});
//# sourceMappingURL=posts.component.js.map