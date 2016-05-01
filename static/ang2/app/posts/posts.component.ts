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

@Component({
    selector: 'my-posts',
    templateUrl: SrcURL + 'posts/posts.html',
    styleUrls: [SrcURL + 'posts/posts.css'],
    directives: [],
    providers: [PostsService, sb_windowTools],
})

export class PostsComponent implements OnInit {
    posts:Array<Posts> = [];
    gettingPosts:boolean = true;
    pageHeight:number;
    nativePostsPosition:Array<Array<number>>;
    scrollPass:boolean = false;
    currentPost:number;
    keyEventPass:boolean = false;
    routeDate:string;
    outOfPosts:boolean = false;
    // ____CONFIG____
    smoothIntervalPx:number = 50;
    smoothIntervalTime:number = 200;
    getPostsEnd:number = 10;
    getPostsStart:number = 0;
    getPostsDelta:number = 5;
    scrollTimeout:number = 150;
    postsOffsetDelta:number = 0;  // !!!DEPRECATED!!!! concat posts offset for unbreakable change currentPost

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

    getPosts(from:number, to:number, date:string) {
        this._postsService.getPosts(from, to, date)
            .subscribe
            ((posts:Array<Posts>)=> {
                    if (posts.length > 0) {
                        this.addMeta(posts);
                        Array.prototype.push.apply(this.posts, posts);
                        this.gettingPosts = false;
                    } else (this.outOfPosts = true)
                },
                // make sure to reget posts
                error=> {
                    console.error('Error to load Posts: ' + error);
                    setTimeout(()=>this.gettingPosts = false, 500);
                }
            );
    };

    addMeta(posts:Array<Posts>) {
        for (let i = 0; i < posts.length; i++) {
            let curPost = posts[i];
            curPost['Meta'] = {
                'doTrunk': true,
                'saw': false,
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
            this.initPosts();
            if (this._sb_windowTools.scrollPercent() > 0.90 && !this.gettingPosts) {
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
            setTimeout(()=> {
                this.scrollPass = false
            }, this.scrollTimeout);
        }
    };

    setNewPostsPosition() {
        let nativePosts = this.element.nativeElement.getElementsByClassName("_mypost");
        this.nativePostsPosition = [];
        for (let i = 0; i < nativePosts.length; i++) {
            let currentPost = nativePosts[i];
            let currentPostOffset = currentPost.offsetHeight;
            let postPosY:number = this._sb_windowTools.findPosY(currentPost);
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

    onKeyPress(event) {
        //console.log(this.routeDate);
        if (!this.keyEventPass) {
            this.keyEventPass = true;
            this.onScroll();

            if (event.keyCode === 100) {
                if (this.nativePostsPosition[this.currentPost + 1]) {
                    //window.scrollTo(0, this.nativePostsPosition[this.currentPost + 1][0]);
                    let from = this._sb_windowTools.verticalOffset();
                    let to = this.nativePostsPosition[this.currentPost + 1][0];
                    this.smoothYScrollFromTo(from, to + 1, this.smoothIntervalPx);
                }
            }

            if (event.keyCode === 97) {
                if (this.nativePostsPosition[this.currentPost - 1]) {
                    //window.scrollTo(0, this.nativePostsPosition[this.currentPost - 1][0]);
                    let from = this._sb_windowTools.verticalOffset();
                    let to = this.nativePostsPosition[this.currentPost - 1][0];
                    this.smoothYScrollFromTo(to + 1, from, -this.smoothIntervalPx);
                }
            }

            setTimeout(()=> {
                this.keyEventPass = false
            }, 200);
        }
    };

    smoothYScrollFromTo(from:number, to:number, rate:number) {
        let smoothTimeout = Math.abs(this.smoothIntervalTime / ((from - to) / rate));
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

    stringAsDate(dateStr) {
        return new Date(dateStr);
    };

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

    contentStop(ipost:number, icontent:number) {
        this.posts[ipost].contents[icontent]['Meta'] = {
            'play': false,
        }
    }
}