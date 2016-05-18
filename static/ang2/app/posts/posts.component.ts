import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {PostsService} from "./posts.service";
import {OnInit} from "angular2/core";
import {sb_windowTools} from "../helpers/sb_windowTools";
import {ElementRef} from "angular2/core";
import {ChangeDetectorRef} from "angular2/core";
import {AfterViewInit} from "angular2/core";
import {RouteParams} from "angular2/router";
import {AfterViewChecked} from "angular2/core";
import {AfterContentInit} from "angular2/core";
import {Posts} from "./posts.interface";
import {PostComponent} from "./post/post.component";
import {ViewChildren} from "angular2/core";
import {QueryList} from "angular2/core";
import {SearchbarComponent} from "./searchbar/searchbar.component";
import {tokenNotExpired, JwtHelper} from "angular2-jwt";

@Component({
    selector: 'my-posts',
    templateUrl: SrcURL + 'posts/posts.html',
    styleUrls: [SrcURL + 'posts/posts.css'],
    directives: [PostComponent, SearchbarComponent],
    providers: [PostsService, sb_windowTools],
})

export class PostsComponent implements OnInit, AfterViewInit {
    posts:Array<Posts> = [];
    gettingPosts:boolean = true;
    pageHeight:number;
    nativePostsPosition:Array<Array<number>>;
    scrollPass:boolean = false;
    currentPost:number;
    keyEventPass:boolean = false;
    routeDate:string;
    outOfPosts:boolean = false;
    viewedPosts:Array<number> = [];
    newViewedPosts:Array<number> = [];
    // ____CONFIG____
    SMOOTH_INTERVAL_PX:number = 50;
    SMOOTH_INTERVAL_TIME:number = 200;
    getPostsEnd:number = 10;
    getPostsStart:number = 0;
    GET_POSTS_DELTA:number = 5;
    SCROLL_TIMEOUT:number = 150;
    SCROLL_PERCENT_LOAD:number = 0.85;
    POSTS_OFFSET_DELTA:number = 30;  // concat posts offset for unbreakable change currentPost

    constructor(public element:ElementRef,
                private _postsService:PostsService,
                private _sb_windowTools:sb_windowTools,
                private _ChangeDetectorRef:ChangeDetectorRef,
                params:RouteParams) {
        this.routeDate = params.get('date');

    };

    ngOnInit() {
        this.getPosts(this.getPostsStart, this.getPostsEnd, this.routeDate);
    };

    @ViewChildren(PostComponent) PostsChildren:QueryList<PostComponent>;

    ngAfterViewInit() {
        this.initMove();
    }

    initMove() {
        if (this.PostsChildren.length > 0) {
            this.initPosts();
        } else {
            setTimeout(()=>this.initMove(), 50)
        }
    }

    getPosts(from:number, to:number, date:string) {
        this._postsService.getPosts(from, to, date)
            .subscribe
            ((posts:Array<Posts>)=> {
                    if (posts.length > 0) {
                        this.grabViewedPostsID(posts);
                        this.addMeta(posts);
                        Array.prototype.push.apply(this.posts, posts);
                        this.gettingPosts = false;
                    } else (this.outOfPosts = true)
                },
                // make sure to reget posts
                error=> {
                    console.error('Error to load Posts: ' + error);
                    setTimeout(()=>this.gettingPosts = false, 1000);
                }
            );
    };

    getNewPosts() {
        this.getPostsEnd += this.GET_POSTS_DELTA;
        this.getPosts(this.getPostsEnd - this.GET_POSTS_DELTA, this.getPostsEnd, this.routeDate);
        this.gettingPosts = true;
    }

    grabViewedPostsID(posts) {
        for (let i = 0; i < posts.length; i++) {
            let curPost = posts[i];
            if (curPost['viewed']) {
                this.viewedPosts.push(curPost['id'])
            }
        }
    }

    addMeta(posts:Array<Posts>) {
        for (let i = 0; i < posts.length; i++) {
            let curPost = posts[i];
            curPost['Meta'] = {
                'doTrunk': true,
            };
            //console.log(curPost.contents[0]);
            for (let i2 = 0; i2 < curPost.contents.length; i2++) {
                curPost.contents[i2]['Meta'] = {
                    'play': false,
                }
            }
        }
    };

    onScroll() {
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
            setTimeout(()=> {
                this.scrollPass = false
            }, this.SCROLL_TIMEOUT);
        }
    };

    updateNativePostsPosition() {
        this.nativePostsPosition = [];
        this.PostsChildren.forEach((post, i)=> {
            let currentPost = post.getNativeElement();
            let currentPostOffset = currentPost.offsetHeight;
            let postPosY:number = this._sb_windowTools.findPosY(currentPost);
            //let style = currentPost.currentStyle || window.getComputedStyle(currentPost);
            //// style.marginBottom return 'Xpx' and due to margin collapse
            //let styleMargin = Math.max(style.marginBottom.slice(0, -2), style.marginTop.slice(0, -2));
            let postInterval:Array<number> = [postPosY - this.POSTS_OFFSET_DELTA, postPosY + currentPostOffset];
            this.nativePostsPosition.push(postInterval);
            //got to know if post was 'doTrunked'
            //this.posts[i].Meta['height'] = currentPostOffset;
        });
        this.nativePostsPosition[0][0] = 0; //for 1st post start position
        console.log(this.nativePostsPosition);
    }

    initPosts() {
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
    }

    isCurrentPost(postIndex:number) {
        try {
            let post:Array<number> = this.nativePostsPosition[postIndex];
            let postY1:number = post[0];
            let postY2:number = post[1];
            let currentOffset = this._sb_windowTools.verticalOffset();
            if (currentOffset >= postY1 && currentOffset <= postY2) {
                return true;
            } else {
                return false;
            }
        } catch (err) {
            console.log('catched', err)
        }
    }

    findCurrentPost(length:number) {
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
        for (let i = 0; i < length; i++) {
            if (this.isCurrentPost(i)) {
                return i;
            }
        }
    }

    setCurrentPostPosition(newPosition:number) {
        if (this.posts[newPosition]) {
            this.currentPost = newPosition;
            console.log('Current Post:', this.posts[newPosition].title);
            let currentID = this.posts[this.currentPost]['id'];

            if (tokenNotExpired() && !this.viewedPosts.find((x)=>x === currentID)) {
                this.viewedPosts.push(currentID);
                this.newViewedPosts.push(currentID);

                //TODO make timeout to send viewed
                if (this.newViewedPosts.length > 5) {
                    //newViewedPosts to server
                    this._postsService.saveViewed(this.newViewedPosts).subscribe(suc => {
                        console.log("Succ to load newViewed:", suc);
                        this.newViewedPosts = [];
                    }, err => {
                        console.log("Err to load newViewed:", err);
                    });
                }
            }
        }
    }

    onKeyPress(event) {
        //console.log(event.keyCode);
        if (!this.keyEventPass) {
            this.keyEventPass = true;
            this.onScroll();

            if (event.keyCode === 100) {
                if (this.nativePostsPosition[this.currentPost + 1]) {
                    //window.scrollTo(0, this.nativePostsPosition[this.currentPost + 1][0]);
                    let from = this._sb_windowTools.verticalOffset();
                    let to = this.nativePostsPosition[this.currentPost + 1][0];
                    this.smoothYScrollFromTo(from, to + 1, this.SMOOTH_INTERVAL_PX);
                }
            }

            if (event.keyCode === 97) {
                if (this.nativePostsPosition[this.currentPost - 1]) {
                    //window.scrollTo(0, this.nativePostsPosition[this.currentPost - 1][0]);
                    let from = this._sb_windowTools.verticalOffset();
                    let to = this.nativePostsPosition[this.currentPost - 1][0];
                    this.smoothYScrollFromTo(to + 1, from, -this.SMOOTH_INTERVAL_PX);
                }
            }

            // hide viewed posts and scroll to first unviewed
            if (event.keyCode === 102) {
                let firstUnViewed;
                for (let i = 0; i < this.posts.length; i++) {
                    var currentPost = this.posts[i];
                    if (this.viewedPosts.find((x)=>x === currentPost.id)) {
                        currentPost.viewed = true;
                    } else {
                        if (firstUnViewed === undefined) {
                            firstUnViewed = i;
                        }
                    }
                }
                if (firstUnViewed !== undefined) {
                    setTimeout(()=> {
                        this.onScroll();
                        // to scrollTo and set as current
                        window.scrollTo(0, this.nativePostsPosition[firstUnViewed][0] + 1);
                        //    wait for cd onscroll()
                    }, this.SCROLL_TIMEOUT + 1)
                }
            }

            setTimeout(()=> {
                this.keyEventPass = false
            }, this.SCROLL_TIMEOUT + 1);
        }
    }

    smoothYScrollFromTo(from:number, to:number, rate:number) {
        let smoothTimeout = Math.abs(this.SMOOTH_INTERVAL_TIME / ((from - to) / rate));
        if (to - from < Math.abs(rate)) {
            if (rate > 0) {
                this.setCurrentPostPosition(this.currentPost + 1);
                window.scrollBy(0, to - from);
                //console.log('set +1');
                return;
            } else {
                this.setCurrentPostPosition(this.currentPost - 1);
                window.scrollBy(0, from - to);
                //console.log('set -1');
                return;
            }
        } else {
            window.scrollBy(0, rate);
            setTimeout(()=> {
                this.smoothYScrollFromTo(from, to - Math.abs(rate), rate);
            }, smoothTimeout);
        }
    }

    contentPlay(ipost:number, icontent:number) {
        for (let i = 0; i < this.posts.length; i++) {
            let curPost = this.posts[i];
            for (let i2 = 0; i2 < curPost.contents.length; i2++) {
                curPost.contents[i2]['Meta'] = {
                    'play': false,
                }
            }
        }
        this.posts[ipost].contents[icontent]['Meta'] = {
            'play': true,
        }
    }


    postInView = {
        '_PostsChildren': this.PostsChildren,
        '_nativePostsPosition': [],
        '_currentPost': undefined,
        '_verticalOffset': undefined,
        '_POSTS_OFFSET_DELTA': this.POSTS_OFFSET_DELTA,
        setVerticalOffset(){
            let verticalOffset;
            if (self.pageYOffset) {
                verticalOffset = self.pageYOffset;
            } else if (document.documentElement && document.documentElement.scrollTop) {
                // Explorer 6 Strict
                verticalOffset = document.documentElement.scrollTop;
            } else if (document.body) {
                // all other Explorers
                verticalOffset = document.body.scrollTop;
            }
            this._verticalOffset = verticalOffset
        },
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
        },
        findCurrent(length:number) {
            for (let i = 0; i < length; i++) {
                if (this.isCurrent(i)) {
                    return i;
                } else {
                    console.log('error to findCurrentPosts')
                }
            }
        },
        isCurrent(postIndex:number) {
            try {
                let post:Array<number> = this._nativePostsPosition[postIndex];
                let postY1:number = post[0];
                let postY2:number = post[1];
                if (this._verticalOffset >= postY1 && this._verticalOffset <= postY2) {
                    return true;
                } else {
                    return false
                }
            } catch (err) {
                console.log('catched', err)
            }
        },
        updateNativePostsPosition() {
            this._nativePostsPosition = [];
            this._PostsChildren.forEach((post, i)=> {
                let currentPost = post.getNativeElement();
                let currentPostOffset = currentPost.offsetHeight;
                let postPosY:number = this.findPosY(currentPost);
                let postInterval:Array<number> = [postPosY - this._POSTS_OFFSET_DELTA, postPosY + currentPostOffset];
                this._nativePostsPosition.push(postInterval);
            });
            this._nativePostsPosition[0][0] = 0; //for 1st post start position
        },
        getCurent(){
            this.setVerticalOffset();
            if (this.isCurrent(this._currentPost)) {
                return this._currentPost;
            }
            else {
                this._currentPost = this.findCurrent(this._nativePostsPosition.length);
                return this._currentPost;
            }
        },

    }


}