export class elementInView {
    _PostsDimension:Array<Array<number>> = [];
    _previousPost:number;
    _currentPost:number = 0;
    _POSTS_START_POINT:number = 0;

    _findPosY(obj):number {
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

    _findCurrent(length:number, verticalOffset:number):number {
        for (let i = 0; i < length; i++) {
            if (this._isCurrent(i, verticalOffset)) {
                return i;
            }
        }
    }

    _isCurrent(postIndex:number, verticalOffset:number):boolean {
        try {
            let post:Array<number> = this._PostsDimension[postIndex];
            let postY1:number = post[0];
            let postY2:number = post[1];
            if (verticalOffset >= postY1 && verticalOffset <= postY2) {
                return true;
            } else {
                return false
            }
        } catch (err) {
            console.log('catched', err)
        }
    }

    //angular2 didnt destroy children after router navigate, so we test it before (it was renderer.listenGlobal, bsd)
    validChildren(PostsChildren):boolean {
        let test = false;
        try {
            test = PostsChildren.first.getNativeElement().offsetHeight > 0;
        } catch (err) {
            console.log(err);
        }
        return test;
    }

    updatePostsDimension(PostsChildren):void {
        if (this.validChildren(PostsChildren)) {
            this._PostsDimension = [];
            //cancat post position for unbreakable scroll
            let postStart:number = this._POSTS_START_POINT;
            PostsChildren.forEach((post, i)=> {
                let currentPost = post.getNativeElement();
                let currentPostOffset = currentPost.offsetHeight;
                let postPosY:number = this._findPosY(currentPost);
                let postEnd = postPosY + currentPostOffset;
                let postInterval:Array<number> = [postStart, postEnd];
                this._PostsDimension.push(postInterval);
                postStart = postEnd;
            });
            //console.log(this._PostsDimension)
        }
    }

    updateCurrent(verticalOffset):void {
        //let verticalOffset = this._getVerticalOffset();
        this._previousPost = this._currentPost;
        if (!this._isCurrent(this._currentPost, verticalOffset)) {
            this._currentPost = this._findCurrent(this._PostsDimension.length, verticalOffset);
        }
    }

    isPostChanged():boolean {
        return this._previousPost !== this._currentPost;
    }

    getCurrent():number {
        return this._currentPost
    }

    getPostStartPosition(post:number):number {
        return this._PostsDimension[post][0];
    }

}
