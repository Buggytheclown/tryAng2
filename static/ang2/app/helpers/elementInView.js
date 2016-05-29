System.register([], function(exports_1) {
    var elementInView;
    return {
        setters:[],
        execute: function() {
            elementInView = (function () {
                function elementInView() {
                    this._PostsDimension = [];
                    this._currentPost = 0;
                    this._POSTS_START_POINT = 0;
                }
                elementInView.prototype._findPosY = function (obj) {
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
                elementInView.prototype._findCurrent = function (length, verticalOffset) {
                    for (var i = 0; i < length; i++) {
                        if (this._isCurrent(i, verticalOffset)) {
                            return i;
                        }
                    }
                };
                elementInView.prototype._isCurrent = function (postIndex, verticalOffset) {
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
                };
                //angular2 didnt destroy children after router navigate, so we test it before (it was renderer.listenGlobal, bsd)
                elementInView.prototype.validChildren = function (PostsChildren) {
                    var test = false;
                    try {
                        test = PostsChildren.first.getNativeElement().offsetHeight > 0;
                    }
                    catch (err) {
                        console.log(err);
                    }
                    return test;
                };
                elementInView.prototype.updatePostsDimension = function (PostsChildren) {
                    var _this = this;
                    if (this.validChildren(PostsChildren)) {
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
                    }
                };
                elementInView.prototype.updateCurrent = function (verticalOffset) {
                    //let verticalOffset = this._getVerticalOffset();
                    this._previousPost = this._currentPost;
                    if (!this._isCurrent(this._currentPost, verticalOffset)) {
                        this._currentPost = this._findCurrent(this._PostsDimension.length, verticalOffset);
                    }
                };
                elementInView.prototype.isPostChanged = function () {
                    return this._previousPost !== this._currentPost;
                };
                elementInView.prototype.getCurrent = function () {
                    return this._currentPost;
                };
                elementInView.prototype.getPostStartPosition = function (post) {
                    return this._PostsDimension[post][0];
                };
                return elementInView;
            })();
            exports_1("elementInView", elementInView);
        }
    }
});
//# sourceMappingURL=elementInView.js.map