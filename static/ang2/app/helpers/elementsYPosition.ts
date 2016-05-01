export class elementsYPosition {
    constructor() {
    };

    findPosY(obj) {
        var curtop = 0;
        if (obj.offsetParent) {
            while (1) {
                curtop += obj.offsetTop;
                if (!obj.offsetParent) {
                    break;
                }
                obj = obj.offsetParent;
            }
        } else if (obj.y) {
            curtop += obj.y;
        }
        return curtop;
    }

    setNewPostsPosition() {
        let nativePosts = this.element.nativeElement.getElementsByClassName("_mypost");
        this.nativePostsPosition = [];
        for (let i = 0; i < nativePosts.length; i++) {
            let currentPost = nativePosts[i];
            let currentPostOffset = currentPost.offsetHeight;
            let postPosY:number = this.findPosY(currentPost);
            let style = currentPost.currentStyle || window.getComputedStyle(currentPost);
            // style.marginBottom return 'Xpx' and due to margin collapse
            let styleMargin = Math.max(style.marginBottom.slice(0, -2), style.marginTop.slice(0, -2));
            let postInterval:Array<number> = [postPosY - styleMargin, postPosY + currentPostOffset];
            this.nativePostsPosition.push(postInterval);
            //got to know if post was 'doTrunked'
            this.posts[i].Meta['height'] = currentPostOffset;
        }
        this.nativePostsPosition[0][0] = 0; //for 1st post start position
    };

    initPosts() {
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
    }

    isCurrentPost(postIndex:number) {
        try {
            let post:Array<number> = this.nativePostsPosition[postIndex];
            let postY1:number = post[0];
            let postY2:number = post[1];
            if (this._sb_windowTools.verticalOffset() > postY1 && this._sb_windowTools.verticalOffset() < postY2) {
                return true;
            } else {
                return false
            }
        } catch (err) {
            console.log('catched', err)
        }
    }

    findCurrentPost() {
        //console.log('updated');
        for (let i = 1; i < 4; i++) {
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
        for (let i = 0; i < this.nativePostsPosition.length; i++) {
            if (this.isCurrentPost(i)) {
                //this.currentPost=i;
                //this.setCurrentPostPosition(i);
                return i;
            }
        }
    };

    setCurrentPostPosition(newPosition:number) {
        if (this.posts[newPosition]) {
            this.currentPost = newPosition;
            this.posts[this.currentPost].Meta.saw = true;
            console.log('Current Post:', this.posts[newPosition].title);
        }
    }


}