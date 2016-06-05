import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {PostsService} from "./posts.service";
import {OnInit} from "angular2/core";
import {sb_windowToolsY} from "../helpers/sb_windowToolsY";
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
import {OnDestroy} from "angular2/core";
import {Renderer} from "angular2/core";
import {elementInView} from "../helpers/elementInView";
import {HeaderComponent} from "../header/header";
import {FriendlistComponent} from "./friendlist/friendlist.component";

@Component({
    selector: 'my-posts',
    templateUrl: SrcURL + 'posts/posts.html',
    styleUrls: [SrcURL + 'posts/posts.css'],
    directives: [PostComponent, SearchbarComponent, HeaderComponent, FriendlistComponent],
    providers: [PostsService, sb_windowToolsY, elementInView],
})

export class PostsComponent implements OnInit, AfterViewInit, OnDestroy {
    // can process onKeyPress
    pressKeyFree:boolean = true;
    posts:Array<Posts> = [];
    gettingPosts:boolean = true;
    scrollPass:boolean = false;
    keyEventPass:boolean = false;
    routeDate:string;
    outOfPosts:boolean = false;
    viewedPosts:Array<number> = [];
    newViewedPosts:Array<number> = [];

    // ____CONFIG____
    SMOOTH_INTERVAL_PX:number = 50;
    SMOOTH_INTERVAL_TIME:number = 200;
    getPostsEnd:number = 5;
    getPostsStart:number = 0;
    GET_POSTS_DELTA:number = 5;
    SCROLL_TIMEOUT:number = 150;
    SCROLL_PERCENT_LOAD:number = 0.85;
    //POSTS_OFFSET_DELTA:number = 30;  // concat posts offset for unbreakable change currentPost
    POSTS_START_POINT:number = 0;
    KEY_NEXT:number = 100;
    KEY_PREVIOUS:number = 97;
    KEY_HIDE_VIEWED:number = 102;

    constructor(private element:ElementRef,
                private _postsService:PostsService,
                private _sb_windowToolsY:sb_windowToolsY,
                private _ChangeDetectorRef:ChangeDetectorRef,
                params:RouteParams,
                private renderer:Renderer,
                private postsInView: elementInView) {
        this.routeDate = params.get('date');

    };

    ngOnInit() {
        this.getPosts(this.getPostsStart, this.getPostsEnd, this.routeDate);
        //on refresh and close save viewed posts
        window.onbeforeunload = ()=> closingCode(this);
        function closingCode(_mythis) {
            _mythis.saveViewedPostsID();
            return null;
        }
        //window.addEventListener("beforeunload", this.saveViewedPostsID);
        //FULL OF BUGGS - dont use it!!!!
        //this.renderer.listenGlobal('window', 'keypress', (event) => {
        //    this.onKeyPress(event)
        //});
        //this.renderer.listenGlobal('window', 'beforeunload', () => {
        //    this.saveViewedPostsID();
        //    return null;
        //});
        //this.renderer.listenGlobal('window', 'scroll', () => {
        //    this.onScroll();
        //});
    };

    @ViewChildren(PostComponent) PostsChildren:QueryList<PostComponent>;

    ngAfterViewInit() {
        this.initMove();
    }

    ngOnDestroy() {
        this.saveViewedPostsID();
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
                        //this.addMeta(posts);
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
        if (!this.gettingPosts) {
            this.getPostsEnd += this.GET_POSTS_DELTA;
            this.getPosts(this.getPostsEnd - this.GET_POSTS_DELTA, this.getPostsEnd, this.routeDate);
            this.gettingPosts = true;
        }
    }

    saveViewedPostsID() {
        if (this.newViewedPosts.length > 0) {
            this._postsService.saveViewed(this.newViewedPosts).subscribe(suc => {
                this.newViewedPosts = [];
                console.log('Saved')
            }, err => {
                console.log(err)
            })
        }
    }

    grabViewedPostsID(posts) {
        for (let i = 0; i < posts.length; i++) {
            let curPost = posts[i];
            if (curPost['viewed']) {
                this.viewedPosts.push(curPost['id'])
            }
        }
    }

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

    onScroll() {
        if (!this.scrollPass) {
            //console.log(this._sb_windowTools.scrollPercent());
            //console.log(this.posts);
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

            setTimeout(()=> {
                this.scrollPass = false
            }, this.SCROLL_TIMEOUT);
        }
    };

    initPosts() {
        this._sb_windowToolsY.updateDimensions();
        this.setCurrentPostPosition(0);
        this.postsInView.updatePostsDimension(this.PostsChildren);
    }

    setCurrentPostPosition(newPosition:number) {
        if (this.posts[newPosition]) {
            console.log('Current Post:', this.posts[newPosition].title);
            let currentID = this.posts[newPosition]['id'];

            if (tokenNotExpired() && !this.viewedPosts.find((x)=>x === currentID)) {
                this.viewedPosts.push(currentID);
                this.newViewedPosts.push(currentID);

                if (this.newViewedPosts.length > 5) {
                    //newViewedPosts to server
                    this.saveViewedPostsID();
                }
            }
        } else {
            console.log('!!!We dont have that post position - ', newPosition)
        }
    }

    onKeyPress(event) {
        //TODO if switch not on content?
        //console.log(event.keyCode);
        if (!this.keyEventPass && this.pressKeyFree) {
            this.keyEventPass = true;
            this.allContentStop();
            this.onScroll();

            switch (event.keyCode) {
                case this.KEY_NEXT:
                    if (this.postsInView.getCurrent() + 1 <= this.posts.length) {
                        let from = this._sb_windowToolsY.verticalOffset();
                        let to = this.postsInView.getPostStartPosition(this.postsInView.getCurrent() + 1);
                        this.smoothYScrollFromTo(from, to + 1, this.SMOOTH_INTERVAL_PX);
                    }
                    break;

                case this.KEY_PREVIOUS:
                    //TODO scroll to top current or previous
                    if (this.postsInView.getCurrent() - 1 >= 0) {
                        let from = this._sb_windowToolsY.verticalOffset();
                        let to = this.postsInView.getPostStartPosition(this.postsInView.getCurrent() - 1);
                        this.smoothYScrollFromTo(to + 1, from, -this.SMOOTH_INTERVAL_PX);
                    }
                    break;

                // hide viewed posts and scroll to first unviewed
                case this.KEY_HIDE_VIEWED:
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
                            // post was truncated => post Dimension was changed
                            this.onScroll();
                            // to scrollTo and set as current
                            window.scrollTo(0, this.postsInView.getPostStartPosition(firstUnViewed) + 1);
                            //    wait for cd onscroll()
                        }, this.SCROLL_TIMEOUT + 1)
                    }
                    break;

            }

            setTimeout(()=> {
                this.keyEventPass = false
            }, this.SCROLL_TIMEOUT + 1);
        }
    }

    //TODO test it (const time to scroll)
    smoothYScrollFromTo(from:number, to:number, rate:number):void {
        let smoothTimeout = Math.abs(this.SMOOTH_INTERVAL_TIME / ((from - to) / rate));
        if (to - from < Math.abs(rate)) {
            if (rate > 0) {
                window.scrollBy(0, to - from);
                //console.log('set +1');
                return;
            } else {
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

    contentPlay(ipost:number, icontent:number):void {
        this.allContentStop();
        this.posts[ipost].contents[icontent]['Meta'] = {
            'play': true,
        }
    }

    allContentStop():void {
        for (let i = 0; i < this.posts.length; i++) {
            let curPost = this.posts[i];
            for (let i2 = 0; i2 < curPost.contents.length; i2++) {
                curPost.contents[i2]['Meta'] = {
                    'play': false,
                }
            }
        }
    }

    //postsInView = {
    //    _PostsDimension: [],
    //    _previousPost: undefined,
    //    _currentPost: 0,
    //    _POSTS_START_POINT: this.POSTS_START_POINT,
    //
    //    _findPosY(obj): number {
    //        var curtop = 0;
    //        if (obj.offsetParent) {
    //            while (1) {
    //                curtop += obj.offsetTop;
    //                if (!obj.offsetParent) {
    //                    break;
    //                }
    //                obj = obj.offsetParent;
    //            }
    //        } else if (obj.y) {
    //            curtop += obj.y;
    //        }
    //        return curtop;
    //    },
    //
    //    _findCurrent(length:number, verticalOffset:number): number {
    //        for (let i = 0; i < length; i++) {
    //            if (this._isCurrent(i, verticalOffset)) {
    //                return i;
    //            }
    //        }
    //    },
    //
    //    _isCurrent(postIndex:number, verticalOffset:number): boolean {
    //        try {
    //            let post:Array<number> = this._PostsDimension[postIndex];
    //            let postY1:number = post[0];
    //            let postY2:number = post[1];
    //            if (verticalOffset >= postY1 && verticalOffset <= postY2) {
    //                return true;
    //            } else {
    //                return false
    //            }
    //        } catch (err) {
    //            console.log('catched', err)
    //        }
    //    },
    //
    //    updatePostsDimension(PostsChildren): void {
    //        this._PostsDimension = [];
    //        //cancat post position for unbreakable scroll
    //        let postStart:number = this._POSTS_START_POINT;
    //        PostsChildren.forEach((post, i)=> {
    //            let currentPost = post.getNativeElement();
    //            let currentPostOffset = currentPost.offsetHeight;
    //            let postPosY:number = this._findPosY(currentPost);
    //            let postEnd = postPosY + currentPostOffset;
    //            let postInterval:Array<number> = [postStart, postEnd];
    //            this._PostsDimension.push(postInterval);
    //            postStart = postEnd;
    //        });
    //    },
    //
    //    updateCurrent(verticalOffset): void {
    //        //let verticalOffset = this._getVerticalOffset();
    //        this._previousPost = this._currentPost;
    //        if (!this._isCurrent(this._currentPost, verticalOffset)) {
    //            this._currentPost = this._findCurrent(this._PostsDimension.length, verticalOffset);
    //        }
    //    },
    //
    //    isPostChanged(): boolean{
    //        return this._previousPost !== this._currentPost
    //    },
    //
    //    getCurrent(): number{
    //        return this._currentPost
    //    },
    //
    //    getPostStartPosition(post:number): number{
    //        return this._PostsDimension[post][0];
    //    }
    //
    //};

    authenticated() {
        return tokenNotExpired();
    }

}