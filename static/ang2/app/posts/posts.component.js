System.register(["angular2/core", "../../static", "./posts.service", "../helpers/sb_windowTools", "angular2/router", "./post/post.component", "./searchbar/searchbar.component", "angular2-jwt"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, posts_service_1, sb_windowTools_1, core_2, core_3, router_1, post_component_1, core_4, core_5, searchbar_component_1, angular2_jwt_1;
    var PostsComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
                core_2 = core_1_1;
                core_3 = core_1_1;
                core_4 = core_1_1;
                core_5 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (posts_service_1_1) {
                posts_service_1 = posts_service_1_1;
            },
            function (sb_windowTools_1_1) {
                sb_windowTools_1 = sb_windowTools_1_1;
            },
            function (router_1_1) {
                router_1 = router_1_1;
            },
            function (post_component_1_1) {
                post_component_1 = post_component_1_1;
            },
            function (searchbar_component_1_1) {
                searchbar_component_1 = searchbar_component_1_1;
            },
            function (angular2_jwt_1_1) {
                angular2_jwt_1 = angular2_jwt_1_1;
            }],
        execute: function() {
            PostsComponent = (function () {
                function PostsComponent(element, _postsService, _sb_windowTools, _ChangeDetectorRef, params) {
                    this.element = element;
                    this._postsService = _postsService;
                    this._sb_windowTools = _sb_windowTools;
                    this._ChangeDetectorRef = _ChangeDetectorRef;
                    this.posts = [];
                    this.gettingPosts = true;
                    this.scrollPass = false;
                    this.keyEventPass = false;
                    this.outOfPosts = false;
                    this.viewedPosts = [];
                    this.newViewedPosts = [];
                    // ____CONFIG____
                    this.smoothIntervalPx = 50;
                    this.smoothIntervalTime = 200;
                    this.getPostsEnd = 10;
                    this.getPostsStart = 0;
                    this.getPostsDelta = 5;
                    this.scrollTimeout = 150;
                    this.postsOffsetDelta = 0; // !!!DEPRECATED!!!! concat posts offset for unbreakable change currentPost
                    this.routeDate = params.get('date');
                }
                ;
                PostsComponent.prototype.ngOnInit = function () {
                    this.getPosts(this.getPostsStart, this.getPostsEnd, this.routeDate);
                };
                ;
                PostsComponent.prototype.ngAfterViewInit = function () {
                    this.initMove();
                };
                PostsComponent.prototype.initMove = function () {
                    var _this = this;
                    if (this.PostsChildren.length > 0) {
                        this._sb_windowTools.updateDimensions();
                        this.initPosts();
                    }
                    else {
                        setTimeout(function () { return _this.initMove(); }, 50);
                    }
                };
                PostsComponent.prototype.getPosts = function (from, to, date) {
                    var _this = this;
                    this._postsService.getPosts(from, to, date)
                        .subscribe(function (posts) {
                        if (posts.length > 0) {
                            _this.addMeta(posts);
                            Array.prototype.push.apply(_this.posts, posts);
                            _this.gettingPosts = false;
                        }
                        else
                            (_this.outOfPosts = true);
                    }, 
                    // make sure to reget posts
                    function (error) {
                        console.error('Error to load Posts: ' + error);
                        setTimeout(function () { return _this.gettingPosts = false; }, 500);
                    });
                };
                ;
                PostsComponent.prototype.addMeta = function (posts) {
                    for (var i = 0; i < posts.length; i++) {
                        var curPost = posts[i];
                        curPost['Meta'] = {
                            'doTrunk': true,
                            'saw': false,
                        };
                        //console.log(curPost.contents[0]);
                        for (var i2 = 0; i2 < curPost.contents.length; i2++) {
                            curPost.contents[i2]['Meta'] = {
                                'play': false,
                            };
                        }
                    }
                };
                ;
                PostsComponent.prototype.onScroll = function () {
                    var _this = this;
                    if (!this.scrollPass) {
                        //console.log(this._sb_windowTools.scrollPercent());
                        this.scrollPass = true;
                        this._sb_windowTools.updateDimensions();
                        if (this._sb_windowTools.scrollPercent() > 0.85 && !this.gettingPosts) {
                            this.getPostsEnd += this.getPostsDelta;
                            this.getPosts(this.getPostsEnd - this.getPostsDelta, this.getPostsEnd, this.routeDate);
                            this.gettingPosts = true;
                        }
                        if (this.pageHeight !== this._sb_windowTools.pageHeight()) {
                            this.setNewPostsPosition();
                            this.pageHeight = this._sb_windowTools.pageHeight();
                        }
                        if (!this.isCurrentPost(this.currentPost)) {
                            this.setCurrentPostPosition(this.findCurrentPost());
                        }
                        setTimeout(function () {
                            _this.scrollPass = false;
                        }, this.scrollTimeout);
                    }
                };
                ;
                PostsComponent.prototype.setNewPostsPosition = function () {
                    var _this = this;
                    //let nativePosts = this.element.nativeElement.getElementsByClassName("_mypost");
                    //let nativePosts = this.PostsChildren.forEach(post=>post.getNativeElement());
                    //nativePosts.forEach(post=>{console.log(post.getNativeElement())});
                    this.nativePostsPosition = [];
                    //for (let i = 0; i < nativePosts.length; i++) {
                    this.PostsChildren.forEach(function (post, i) {
                        var currentPost = post.getNativeElement();
                        var currentPostOffset = currentPost.offsetHeight;
                        var postPosY = _this._sb_windowTools.findPosY(currentPost);
                        var style = currentPost.currentStyle || window.getComputedStyle(currentPost);
                        // style.marginBottom return 'Xpx' and due to margin collapse
                        var styleMargin = Math.max(style.marginBottom.slice(0, -2), style.marginTop.slice(0, -2));
                        var postInterval = [postPosY - styleMargin, postPosY + currentPostOffset];
                        _this.nativePostsPosition.push(postInterval);
                        //got to know if post was 'doTrunked'
                        _this.posts[i].Meta['height'] = currentPostOffset;
                    });
                    this.nativePostsPosition[0][0] = 0; //for 1st post start position
                };
                PostsComponent.prototype.initPosts = function () {
                    // __init__ move
                    if (this.currentPost == null) {
                        this.setCurrentPostPosition(0);
                    }
                    if (!this.nativePostsPosition) {
                        this.setNewPostsPosition();
                    }
                    if (!this.pageHeight) {
                        this.pageHeight = this._sb_windowTools.pageHeight();
                    }
                };
                PostsComponent.prototype.isCurrentPost = function (postIndex) {
                    try {
                        var post = this.nativePostsPosition[postIndex];
                        var postY1 = post[0];
                        var postY2 = post[1];
                        if (this._sb_windowTools.verticalOffset() > postY1 && this._sb_windowTools.verticalOffset() < postY2) {
                            return true;
                        }
                        else {
                            return false;
                        }
                    }
                    catch (err) {
                        console.log('catched', err);
                    }
                };
                PostsComponent.prototype.findCurrentPost = function () {
                    //console.log('updated');
                    for (var i = 1; i < 4; i++) {
                        if (this.nativePostsPosition[this.currentPost + i] && this.isCurrentPost(this.currentPost + i)) {
                            //this.currentPost+=i;
                            //this.setCurrentPostPosition(this.currentPost + i);
                            return (this.currentPost + i);
                        }
                        if (this.nativePostsPosition[this.currentPost + i] && this.currentPost !== 0 && this.isCurrentPost(this.currentPost - i)) {
                            //this.currentPost-=i;
                            //this.setCurrentPostPosition(this.currentPost - i);
                            return (this.currentPost - i);
                        }
                    }
                    for (var i = 0; i < this.nativePostsPosition.length; i++) {
                        if (this.isCurrentPost(i)) {
                            //this.currentPost=i;
                            //this.setCurrentPostPosition(i);
                            return i;
                        }
                    }
                };
                PostsComponent.prototype.setCurrentPostPosition = function (newPosition) {
                    if (this.posts[newPosition]) {
                        this.currentPost = newPosition;
                        this.posts[this.currentPost].Meta.saw = true;
                        console.log('Current Post:', this.posts[newPosition].title);
                        var currentPID = this.posts[this.currentPost]['p_id'];
                        if (angular2_jwt_1.tokenNotExpired() && !this.viewedPosts.find(function (x) { return x === currentPID; })) {
                            this.viewedPosts.push(currentPID);
                            this.newViewedPosts.push(currentPID);
                            if (this.newViewedPosts.length > 5) {
                                //newViewedPosts to server
                                this._postsService.saveViewed(this.newViewedPosts).subscribe(function (suc) {
                                    console.log(suc);
                                }, function (err) {
                                    console.log(err);
                                });
                                this.newViewedPosts = [];
                            }
                        }
                    }
                };
                PostsComponent.prototype.onKeyPress = function (event) {
                    var _this = this;
                    //console.log(this.routeDate);
                    if (!this.keyEventPass) {
                        this.keyEventPass = true;
                        this.onScroll();
                        if (event.keyCode === 100) {
                            if (this.nativePostsPosition[this.currentPost + 1]) {
                                //window.scrollTo(0, this.nativePostsPosition[this.currentPost + 1][0]);
                                var from = this._sb_windowTools.verticalOffset();
                                var to = this.nativePostsPosition[this.currentPost + 1][0];
                                this.smoothYScrollFromTo(from, to + 1, this.smoothIntervalPx);
                            }
                        }
                        if (event.keyCode === 97) {
                            if (this.nativePostsPosition[this.currentPost - 1]) {
                                //window.scrollTo(0, this.nativePostsPosition[this.currentPost - 1][0]);
                                var from = this._sb_windowTools.verticalOffset();
                                var to = this.nativePostsPosition[this.currentPost - 1][0];
                                this.smoothYScrollFromTo(to + 1, from, -this.smoothIntervalPx);
                            }
                        }
                        setTimeout(function () {
                            _this.keyEventPass = false;
                        }, 200);
                    }
                };
                PostsComponent.prototype.smoothYScrollFromTo = function (from, to, rate) {
                    var _this = this;
                    var smoothTimeout = Math.abs(this.smoothIntervalTime / ((from - to) / rate));
                    if (to - from < Math.abs(rate)) {
                        if (rate > 0) {
                            this.setCurrentPostPosition(this.currentPost + 1);
                            window.scrollBy(0, to - from);
                            //console.log('set +1');
                            return;
                        }
                        else {
                            this.setCurrentPostPosition(this.currentPost - 1);
                            window.scrollBy(0, from - to);
                            //console.log('set -1');
                            return;
                        }
                    }
                    else {
                        window.scrollBy(0, rate);
                        setTimeout(function () {
                            _this.smoothYScrollFromTo(from, to - Math.abs(rate), rate);
                        }, smoothTimeout);
                    }
                };
                PostsComponent.prototype.contentPlay = function (ipost, icontent) {
                    for (var i = 0; i < this.posts.length; i++) {
                        var curPost = this.posts[i];
                        for (var i2 = 0; i2 < curPost.contents.length; i2++) {
                            curPost.contents[i2]['Meta'] = {
                                'play': false,
                            };
                        }
                    }
                    this.posts[ipost].contents[icontent]['Meta'] = {
                        'play': true,
                    };
                };
                __decorate([
                    core_4.ViewChildren(post_component_1.PostComponent), 
                    __metadata('design:type', core_5.QueryList)
                ], PostsComponent.prototype, "PostsChildren", void 0);
                PostsComponent = __decorate([
                    core_1.Component({
                        selector: 'my-posts',
                        templateUrl: static_1.SrcURL + 'posts/posts.html',
                        styleUrls: [static_1.SrcURL + 'posts/posts.css'],
                        directives: [post_component_1.PostComponent, searchbar_component_1.SearchbarComponent],
                        providers: [posts_service_1.PostsService, sb_windowTools_1.sb_windowTools],
                    }), 
                    __metadata('design:paramtypes', [core_2.ElementRef, posts_service_1.PostsService, sb_windowTools_1.sb_windowTools, core_3.ChangeDetectorRef, router_1.RouteParams])
                ], PostsComponent);
                return PostsComponent;
            })();
            exports_1("PostsComponent", PostsComponent);
        }
    }
});
//# sourceMappingURL=posts.component.js.map