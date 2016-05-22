System.register(["angular2/core", "../../static", "./posts.service", "../helpers/sb_windowToolsY", "angular2/router", "./post/post.component", "./searchbar/searchbar.component", "angular2-jwt"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, posts_service_1, sb_windowToolsY_1, core_2, core_3, router_1, post_component_1, core_4, core_5, searchbar_component_1, angular2_jwt_1;
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
            function (sb_windowToolsY_1_1) {
                sb_windowToolsY_1 = sb_windowToolsY_1_1;
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
                function PostsComponent(element, _postsService, _sb_windowToolsY, _ChangeDetectorRef, params) {
                    this.element = element;
                    this._postsService = _postsService;
                    this._sb_windowToolsY = _sb_windowToolsY;
                    this._ChangeDetectorRef = _ChangeDetectorRef;
                    this.posts = [];
                    this.gettingPosts = true;
                    this.scrollPass = false;
                    this.keyEventPass = false;
                    this.outOfPosts = false;
                    this.viewedPosts = [];
                    this.newViewedPosts = [];
                    // ____CONFIG____
                    this.SMOOTH_INTERVAL_PX = 50;
                    this.SMOOTH_INTERVAL_TIME = 200;
                    this.getPostsEnd = 10;
                    this.getPostsStart = 0;
                    this.GET_POSTS_DELTA = 5;
                    this.SCROLL_TIMEOUT = 150;
                    this.SCROLL_PERCENT_LOAD = 0.85;
                    //POSTS_OFFSET_DELTA:number = 30;  // concat posts offset for unbreakable change currentPost
                    this.POSTS_START_POINT = 0;
                    this.KEY_NEXT = 100;
                    this.KEY_PREVIOUS = 97;
                    this.KEY_HIDE_VIEWED = 102;
                    this.postsInView = {
                        _PostsDimension: [],
                        _previousPost: undefined,
                        _currentPost: 0,
                        _POSTS_START_POINT: this.POSTS_START_POINT,
                        //_getVerticalOffset(): number {
                        //    if (self.pageYOffset) {
                        //        return self.pageYOffset;
                        //    } else if (document.documentElement && document.documentElement.scrollTop) {
                        //        // Explorer 6 Strict
                        //        return document.documentElement.scrollTop;
                        //    } else if (document.body) {
                        //        // all other Explorers
                        //        return document.body.scrollTop;
                        //    }
                        //},
                        _findPosY: function (obj) {
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
                        },
                        _findCurrent: function (length, verticalOffset) {
                            for (var i = 0; i < length; i++) {
                                if (this._isCurrent(i, verticalOffset)) {
                                    return i;
                                }
                            }
                        },
                        _isCurrent: function (postIndex, verticalOffset) {
                            try {
                                var post = this._PostsDimension[postIndex];
                                var postY1 = post[0];
                                var postY2 = post[1];
                                if (verticalOffset >= postY1 && verticalOffset <= postY2) {
                                    return true;
                                }
                                else {
                                    return false;
                                }
                            }
                            catch (err) {
                                console.log('catched', err);
                            }
                        },
                        updatePostsDimension: function (PostsChildren) {
                            var _this = this;
                            this._PostsDimension = [];
                            //cancat post position for unbreakable scroll
                            var postStart = this._POSTS_START_POINT;
                            PostsChildren.forEach(function (post, i) {
                                var currentPost = post.getNativeElement();
                                var currentPostOffset = currentPost.offsetHeight;
                                var postPosY = _this._findPosY(currentPost);
                                var postEnd = postPosY + currentPostOffset;
                                var postInterval = [postStart, postEnd];
                                _this._PostsDimension.push(postInterval);
                                postStart = postEnd;
                            });
                        },
                        updateCurrent: function (verticalOffset) {
                            //let verticalOffset = this._getVerticalOffset();
                            this._previousPost = this._currentPost;
                            if (!this._isCurrent(this._currentPost, verticalOffset)) {
                                this._currentPost = this._findCurrent(this._PostsDimension.length, verticalOffset);
                            }
                        },
                        isPostChanged: function () {
                            return this._previousPost !== this._currentPost;
                        },
                        getCurrent: function () {
                            return this._currentPost;
                        },
                        getPostStartPosition: function (post) {
                            return this._PostsDimension[post][0];
                        }
                    };
                    this.routeDate = params.get('date');
                }
                ;
                PostsComponent.prototype.ngOnInit = function () {
                    var _this = this;
                    this.getPosts(this.getPostsStart, this.getPostsEnd, this.routeDate);
                    //on refresh and close save viewed posts
                    window.onbeforeunload = function () { return closingCode(_this); };
                    function closingCode(_mythis) {
                        _mythis.saveViewedPostsID();
                        return null;
                    }
                };
                ;
                PostsComponent.prototype.ngAfterViewInit = function () {
                    this.initMove();
                };
                PostsComponent.prototype.initMove = function () {
                    var _this = this;
                    if (this.PostsChildren.length > 0) {
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
                            _this.grabViewedPostsID(posts);
                            //this.addMeta(posts);
                            Array.prototype.push.apply(_this.posts, posts);
                            _this.gettingPosts = false;
                        }
                        else
                            (_this.outOfPosts = true);
                    }, 
                    // make sure to reget posts
                    function (error) {
                        console.error('Error to load Posts: ' + error);
                        setTimeout(function () { return _this.gettingPosts = false; }, 1000);
                    });
                };
                ;
                PostsComponent.prototype.getNewPosts = function () {
                    if (!this.gettingPosts) {
                        this.getPostsEnd += this.GET_POSTS_DELTA;
                        this.getPosts(this.getPostsEnd - this.GET_POSTS_DELTA, this.getPostsEnd, this.routeDate);
                        this.gettingPosts = true;
                    }
                };
                PostsComponent.prototype.saveViewedPostsID = function () {
                    var _this = this;
                    this._postsService.saveViewed(this.newViewedPosts).subscribe(function (suc) {
                        _this.newViewedPosts = [];
                        console.log('Saved');
                    }, function (err) {
                    });
                };
                PostsComponent.prototype.grabViewedPostsID = function (posts) {
                    for (var i = 0; i < posts.length; i++) {
                        var curPost = posts[i];
                        if (curPost['viewed']) {
                            this.viewedPosts.push(curPost['id']);
                        }
                    }
                };
                //addMeta(posts:Array<Posts>) {
                //    for (let i = 0; i < posts.length; i++) {
                //        let curPost = posts[i];
                //        //curPost['Meta'] = {
                //        //    'doTrunk': true,
                //        //};
                //        //console.log(curPost.contents[0]);
                //        for (let i2 = 0; i2 < curPost.contents.length; i2++) {
                //            curPost.contents[i2]['Meta'] = {
                //                'play': false,
                //            }
                //        }
                //    }
                //};
                PostsComponent.prototype.onScroll = function () {
                    var _this = this;
                    if (!this.scrollPass) {
                        //console.log(this._sb_windowTools.scrollPercent());
                        this.scrollPass = true;
                        this._sb_windowToolsY.updateDimensions();
                        if (this._sb_windowToolsY.isPageHeightChanged()) {
                            this.postsInView.updatePostsDimension(this.PostsChildren);
                        }
                        this.postsInView.updateCurrent(this._sb_windowToolsY.verticalOffset());
                        if (this.postsInView.isPostChanged()) {
                            this.setCurrentPostPosition(this.postsInView.getCurrent());
                        }
                        if (this._sb_windowToolsY.scrollPercent() > this.SCROLL_PERCENT_LOAD) {
                            this.getNewPosts();
                        }
                        setTimeout(function () {
                            _this.scrollPass = false;
                        }, this.SCROLL_TIMEOUT);
                    }
                };
                ;
                PostsComponent.prototype.initPosts = function () {
                    this._sb_windowToolsY.updateDimensions();
                    this.setCurrentPostPosition(0);
                    this.postsInView.updatePostsDimension(this.PostsChildren);
                };
                PostsComponent.prototype.setCurrentPostPosition = function (newPosition) {
                    //TODO remove 'if'
                    if (this.posts[newPosition]) {
                        console.log('Current Post:', this.posts[newPosition].title);
                        var currentID = this.posts[newPosition]['id'];
                        if (angular2_jwt_1.tokenNotExpired() && !this.viewedPosts.find(function (x) { return x === currentID; })) {
                            this.viewedPosts.push(currentID);
                            this.newViewedPosts.push(currentID);
                            if (this.newViewedPosts.length > 5) {
                                //newViewedPosts to server
                                this.saveViewedPostsID();
                            }
                        }
                    }
                    else {
                        console.log('!!!We dont have that post position');
                    }
                };
                PostsComponent.prototype.onKeyPress = function (event) {
                    var _this = this;
                    //console.log(event.keyCode);
                    if (!this.keyEventPass) {
                        this.keyEventPass = true;
                        this.onScroll();
                        switch (event.keyCode) {
                            case this.KEY_NEXT:
                                if (this.postsInView.getCurrent() + 1 <= this.posts.length) {
                                    this._sb_windowToolsY.updateDimensions();
                                    var from = this._sb_windowToolsY.verticalOffset();
                                    var to = this.postsInView.getPostStartPosition(this.postsInView.getCurrent() + 1);
                                    this.smoothYScrollFromTo(from, to + 1, this.SMOOTH_INTERVAL_PX);
                                }
                                break;
                            case this.KEY_PREVIOUS:
                                if (this.postsInView.getCurrent() - 1 >= 0) {
                                    this._sb_windowToolsY.updateDimensions();
                                    var from = this._sb_windowToolsY.verticalOffset();
                                    var to = this.postsInView.getPostStartPosition(this.postsInView.getCurrent() - 1);
                                    this.smoothYScrollFromTo(to + 1, from, -this.SMOOTH_INTERVAL_PX);
                                }
                                break;
                            // hide viewed posts and scroll to first unviewed
                            case this.KEY_HIDE_VIEWED:
                                var firstUnViewed;
                                for (var i = 0; i < this.posts.length; i++) {
                                    var currentPost = this.posts[i];
                                    if (this.viewedPosts.find(function (x) { return x === currentPost.id; })) {
                                        currentPost.viewed = true;
                                    }
                                    else {
                                        if (firstUnViewed === undefined) {
                                            firstUnViewed = i;
                                        }
                                    }
                                }
                                if (firstUnViewed !== undefined) {
                                    setTimeout(function () {
                                        // post was truncated => post Dimension was changed
                                        _this.onScroll();
                                        // to scrollTo and set as current
                                        window.scrollTo(0, _this.postsInView.getPostStartPosition(firstUnViewed) + 1);
                                        //    wait for cd onscroll()
                                    }, this.SCROLL_TIMEOUT + 1);
                                }
                                break;
                        }
                        setTimeout(function () {
                            _this.keyEventPass = false;
                        }, this.SCROLL_TIMEOUT + 1);
                    }
                };
                PostsComponent.prototype.smoothYScrollFromTo = function (from, to, rate) {
                    var _this = this;
                    var smoothTimeout = Math.abs(this.SMOOTH_INTERVAL_TIME / ((from - to) / rate));
                    if (to - from < Math.abs(rate)) {
                        if (rate > 0) {
                            window.scrollBy(0, to - from);
                            //console.log('set +1');
                            return;
                        }
                        else {
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
                        providers: [posts_service_1.PostsService, sb_windowToolsY_1.sb_windowToolsY],
                    }), 
                    __metadata('design:paramtypes', [core_2.ElementRef, posts_service_1.PostsService, sb_windowToolsY_1.sb_windowToolsY, core_3.ChangeDetectorRef, router_1.RouteParams])
                ], PostsComponent);
                return PostsComponent;
            })();
            exports_1("PostsComponent", PostsComponent);
        }
    }
});
//# sourceMappingURL=posts.component.js.map