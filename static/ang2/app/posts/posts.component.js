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
                    this.SMOOTH_INTERVAL_PX = 50;
                    this.SMOOTH_INTERVAL_TIME = 200;
                    this.getPostsEnd = 10;
                    this.getPostsStart = 0;
                    this.GET_POSTS_DELTA = 5;
                    this.SCROLL_TIMEOUT = 150;
                    this.SCROLL_PERCENT_LOAD = 0.85;
                    this.POSTS_OFFSET_DELTA = 30; // concat posts offset for unbreakable change currentPost
                    this.postInView = {
                        '_PostsChildren': this.PostsChildren,
                        '_nativePostsPosition': [],
                        '_currentPost': undefined,
                        '_verticalOffset': undefined,
                        '_POSTS_OFFSET_DELTA': this.POSTS_OFFSET_DELTA,
                        setVerticalOffset: function () {
                            var verticalOffset;
                            if (self.pageYOffset) {
                                verticalOffset = self.pageYOffset;
                            }
                            else if (document.documentElement && document.documentElement.scrollTop) {
                                // Explorer 6 Strict
                                verticalOffset = document.documentElement.scrollTop;
                            }
                            else if (document.body) {
                                // all other Explorers
                                verticalOffset = document.body.scrollTop;
                            }
                            this._verticalOffset = verticalOffset;
                        },
                        findPosY: function (obj) {
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
                        findCurrent: function (length) {
                            for (var i = 0; i < length; i++) {
                                if (this.isCurrent(i)) {
                                    return i;
                                }
                                else {
                                    console.log('error to findCurrentPosts');
                                }
                            }
                        },
                        isCurrent: function (postIndex) {
                            try {
                                var post = this._nativePostsPosition[postIndex];
                                var postY1 = post[0];
                                var postY2 = post[1];
                                if (this._verticalOffset >= postY1 && this._verticalOffset <= postY2) {
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
                        updateNativePostsPosition: function () {
                            var _this = this;
                            this._nativePostsPosition = [];
                            this._PostsChildren.forEach(function (post, i) {
                                var currentPost = post.getNativeElement();
                                var currentPostOffset = currentPost.offsetHeight;
                                var postPosY = _this.findPosY(currentPost);
                                var postInterval = [postPosY - _this._POSTS_OFFSET_DELTA, postPosY + currentPostOffset];
                                _this._nativePostsPosition.push(postInterval);
                            });
                            this._nativePostsPosition[0][0] = 0; //for 1st post start position
                        },
                        getCurent: function () {
                            this.setVerticalOffset();
                            if (this.isCurrent(this._currentPost)) {
                                return this._currentPost;
                            }
                            else {
                                this._currentPost = this.findCurrent(this._nativePostsPosition.length);
                                return this._currentPost;
                            }
                        },
                    };
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
                        setTimeout(function () { return _this.gettingPosts = false; }, 1000);
                    });
                };
                ;
                PostsComponent.prototype.getNewPosts = function () {
                    this.getPostsEnd += this.GET_POSTS_DELTA;
                    this.getPosts(this.getPostsEnd - this.GET_POSTS_DELTA, this.getPostsEnd, this.routeDate);
                    this.gettingPosts = true;
                };
                PostsComponent.prototype.grabViewedPostsID = function (posts) {
                    for (var i = 0; i < posts.length; i++) {
                        var curPost = posts[i];
                        if (curPost['viewed']) {
                            this.viewedPosts.push(curPost['id']);
                        }
                    }
                };
                PostsComponent.prototype.addMeta = function (posts) {
                    for (var i = 0; i < posts.length; i++) {
                        var curPost = posts[i];
                        curPost['Meta'] = {
                            'doTrunk': true,
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
                        if (this._sb_windowTools.scrollPercent() > this.SCROLL_PERCENT_LOAD && !this.gettingPosts) {
                            this.getNewPosts();
                        }
                        if (this.pageHeight !== this._sb_windowTools.pageHeight()) {
                            this.updateNativePostsPosition();
                            this.pageHeight = this._sb_windowTools.pageHeight();
                        }
                        if (!this.isCurrentPost(this.currentPost)) {
                            this.setCurrentPostPosition(this.findCurrentPost(this.nativePostsPosition.length));
                        }
                        setTimeout(function () {
                            _this.scrollPass = false;
                        }, this.SCROLL_TIMEOUT);
                    }
                };
                ;
                PostsComponent.prototype.updateNativePostsPosition = function () {
                    var _this = this;
                    this.nativePostsPosition = [];
                    this.PostsChildren.forEach(function (post, i) {
                        var currentPost = post.getNativeElement();
                        var currentPostOffset = currentPost.offsetHeight;
                        var postPosY = _this._sb_windowTools.findPosY(currentPost);
                        //let style = currentPost.currentStyle || window.getComputedStyle(currentPost);
                        //// style.marginBottom return 'Xpx' and due to margin collapse
                        //let styleMargin = Math.max(style.marginBottom.slice(0, -2), style.marginTop.slice(0, -2));
                        var postInterval = [postPosY - _this.POSTS_OFFSET_DELTA, postPosY + currentPostOffset];
                        _this.nativePostsPosition.push(postInterval);
                        //got to know if post was 'doTrunked'
                        //this.posts[i].Meta['height'] = currentPostOffset;
                    });
                    this.nativePostsPosition[0][0] = 0; //for 1st post start position
                    console.log(this.nativePostsPosition);
                };
                PostsComponent.prototype.initPosts = function () {
                    this._sb_windowTools.updateDimensions();
                    // __init__ move
                    if (this.currentPost == null) {
                        this.setCurrentPostPosition(0);
                    }
                    if (!this.nativePostsPosition) {
                        this.updateNativePostsPosition();
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
                        var currentOffset = this._sb_windowTools.verticalOffset();
                        if (currentOffset >= postY1 && currentOffset <= postY2) {
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
                PostsComponent.prototype.findCurrentPost = function (length) {
                    //console.log('updated');
                    //for (let i = 1; i < 4; i++) {
                    //    if (this.nativePostsPosition[this.currentPost + i] && this.isCurrentPost(this.currentPost + i)) {
                    //        //this.currentPost+=i;
                    //        //this.setCurrentPostPosition(this.currentPost + i);
                    //        return (this.currentPost + i);
                    //    }
                    //    if (this.nativePostsPosition[this.currentPost + i] && this.currentPost !== 0 && this.isCurrentPost(this.currentPost - i)) {
                    //        //this.currentPost-=i;
                    //        //this.setCurrentPostPosition(this.currentPost - i);
                    //        return (this.currentPost - i);
                    //    }
                    //}
                    for (var i = 0; i < length; i++) {
                        if (this.isCurrentPost(i)) {
                            return i;
                        }
                    }
                };
                PostsComponent.prototype.setCurrentPostPosition = function (newPosition) {
                    var _this = this;
                    if (this.posts[newPosition]) {
                        this.currentPost = newPosition;
                        console.log('Current Post:', this.posts[newPosition].title);
                        var currentID = this.posts[this.currentPost]['id'];
                        if (angular2_jwt_1.tokenNotExpired() && !this.viewedPosts.find(function (x) { return x === currentID; })) {
                            this.viewedPosts.push(currentID);
                            this.newViewedPosts.push(currentID);
                            //TODO make timeout to send viewed
                            if (this.newViewedPosts.length > 5) {
                                //newViewedPosts to server
                                this._postsService.saveViewed(this.newViewedPosts).subscribe(function (suc) {
                                    console.log("Succ to load newViewed:", suc);
                                    _this.newViewedPosts = [];
                                }, function (err) {
                                    console.log("Err to load newViewed:", err);
                                });
                            }
                        }
                    }
                };
                PostsComponent.prototype.onKeyPress = function (event) {
                    var _this = this;
                    //console.log(event.keyCode);
                    if (!this.keyEventPass) {
                        this.keyEventPass = true;
                        this.onScroll();
                        if (event.keyCode === 100) {
                            if (this.nativePostsPosition[this.currentPost + 1]) {
                                //window.scrollTo(0, this.nativePostsPosition[this.currentPost + 1][0]);
                                var from = this._sb_windowTools.verticalOffset();
                                var to = this.nativePostsPosition[this.currentPost + 1][0];
                                this.smoothYScrollFromTo(from, to + 1, this.SMOOTH_INTERVAL_PX);
                            }
                        }
                        if (event.keyCode === 97) {
                            if (this.nativePostsPosition[this.currentPost - 1]) {
                                //window.scrollTo(0, this.nativePostsPosition[this.currentPost - 1][0]);
                                var from = this._sb_windowTools.verticalOffset();
                                var to = this.nativePostsPosition[this.currentPost - 1][0];
                                this.smoothYScrollFromTo(to + 1, from, -this.SMOOTH_INTERVAL_PX);
                            }
                        }
                        // hide viewed posts and scroll to first unviewed
                        if (event.keyCode === 102) {
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
                                    _this.onScroll();
                                    // to scrollTo and set as current
                                    window.scrollTo(0, _this.nativePostsPosition[firstUnViewed][0] + 1);
                                    //    wait for cd onscroll()
                                }, this.SCROLL_TIMEOUT + 1);
                            }
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