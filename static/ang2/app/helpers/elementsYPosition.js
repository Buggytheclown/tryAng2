System.register([], function(exports_1) {
    var elementsYPosition;
    return {
        setters:[],
        execute: function() {
            elementsYPosition = (function () {
                function elementsYPosition() {
                }
                ;
                elementsYPosition.prototype.findPosY = function (obj) {
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
                elementsYPosition.prototype.setNewPostsPosition = function () {
                    var nativePosts = this.element.nativeElement.getElementsByClassName("_mypost");
                    this.nativePostsPosition = [];
                    for (var i = 0; i < nativePosts.length; i++) {
                        var currentPost = nativePosts[i];
                        var currentPostOffset = currentPost.offsetHeight;
                        var postPosY = this.findPosY(currentPost);
                        var style = currentPost.currentStyle || window.getComputedStyle(currentPost);
                        // style.marginBottom return 'Xpx' and due to margin collapse
                        var styleMargin = Math.max(style.marginBottom.slice(0, -2), style.marginTop.slice(0, -2));
                        var postInterval = [postPosY - styleMargin, postPosY + currentPostOffset];
                        this.nativePostsPosition.push(postInterval);
                        //got to know if post was 'doTrunked'
                        this.posts[i].Meta['height'] = currentPostOffset;
                    }
                    this.nativePostsPosition[0][0] = 0; //for 1st post start position
                };
                ;
                elementsYPosition.prototype.initPosts = function () {
                    // __init__ move (dont know how to do else, ngOnViewInit didn't work for that)
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
                elementsYPosition.prototype.isCurrentPost = function (postIndex) {
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
                elementsYPosition.prototype.findCurrentPost = function () {
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
                ;
                elementsYPosition.prototype.setCurrentPostPosition = function (newPosition) {
                    if (this.posts[newPosition]) {
                        this.currentPost = newPosition;
                        this.posts[this.currentPost].Meta.saw = true;
                        console.log('Current Post:', this.posts[newPosition].title);
                    }
                };
                return elementsYPosition;
            })();
            exports_1("elementsYPosition", elementsYPosition);
        }
    }
});
//# sourceMappingURL=elementsYPosition.js.map