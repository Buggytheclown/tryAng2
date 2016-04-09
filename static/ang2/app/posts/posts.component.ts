import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {PostsService} from "./posts.service";
import {OnInit} from "angular2/core";
import {sb_windowTools} from "../helpers/sb_windowTools";
import {ElementRef} from "angular2/core";
import {ChangeDetectorRef} from "angular2/core";

@Component({
    selector: 'my-posts',
    templateUrl: SrcURL + 'html/posts.html',
    styles: [`
    pre{
        white-space: pre-line;
    }
    `],
    directives: [],
    providers: [PostsService, sb_windowTools],
})

export class PostsComponent implements OnInit {
    posts:any = [];
    truncateWord:number;
    scrollPercent:number;
    gettingPosts:boolean = true;
    getPostsEnd:number;
    getPostsStart:number;
    getPostsDelta:number;
    pageHeight:number;
    nativePostsPosition:Array<Array<number>>;
    scrollPass:boolean = false;
    currentPost:number;
    postsOffsetDelta:number = 20;  //concat posts offset for unbreakable change currentPost

    constructor(public element:ElementRef,
                private _postsService:PostsService,
                private _sb_windowTools:sb_windowTools,
                private _ChangeDetectorRef:ChangeDetectorRef) {
        this.truncateWord = 300;
        this.getPostsEnd = 10;
        this.getPostsStart = 0;
        this.getPostsDelta = 5;
    };

    ngOnInit() {
        this.getPosts(this.getPostsStart, this.getPostsEnd);
    };


    getPosts(from, to) {
        this._postsService.getPosts(from, to)
            .subscribe
            (posts=> {
                this.addMeta(posts);
                Array.prototype.push.apply(this.posts, posts);
                this.gettingPosts = false;
            });
    };

    addMeta(posts) {
        for (let i = 0; i < posts.length; i++) {
            posts[i]['Meta'] = {
                'doTrunk': true,
                'saw': false,
            }
        }
    };

    onScroll() {
        if(!this.scrollPass) {
            //console.log('onScroll');
            this.scrollPass = true;
            this._sb_windowTools.updateDimensions();
            this.checkLoadNewPosts();
            this.checkPostsPosition();
            this.updateCurrentPost();
            setTimeout(()=>{this.scrollPass = false}, 200);
        }
    };

    setNewPostsPosition(){
        let nativePosts = this.element.nativeElement.getElementsByClassName("_mypost");
        this.nativePostsPosition = [];
        for(let i = 0; i < nativePosts.length; i++){
            let postPosY:number = this._sb_windowTools.findPosY(nativePosts[i]);
            let postInterval:Array<number> = [postPosY - this.postsOffsetDelta, postPosY + nativePosts[i].offsetHeight ];
            this.nativePostsPosition.push(postInterval);
        }
        this.nativePostsPosition[0][0] = 0; //for 1st post start position
    };

    checkLoadNewPosts(){
        this.scrollPercent = (this._sb_windowTools.windowHeight() + this._sb_windowTools.verticalOffset()) / this._sb_windowTools.pageHeight();
        if (this.scrollPercent > 0.90 && !this.gettingPosts) {
            this.getPostsEnd += this.getPostsDelta;
            this.getPosts(this.getPostsEnd - this.getPostsDelta, this.getPostsEnd);
            this.gettingPosts = true;
        }
    }

    checkPostsPosition(){
        //initializing move (dont know how to do else, ngOnViewInit didnt work)
        if(this.currentPost==null){
            this.setCurrentPostPosition(0);
        }
        if (!this.nativePostsPosition) {
                this.setNewPostsPosition();
        }
        if (!this.pageHeight) {
            this.pageHeight = this._sb_windowTools.pageHeight();
        }
        if (this.pageHeight !== this._sb_windowTools.pageHeight()) {
            this.setNewPostsPosition();
            this.pageHeight = this._sb_windowTools.pageHeight();
        }
    }

    updateCurrentPost(){
        //console.log('updated');
        if(this.isCurrentPost(this.currentPost) ){
            return;
        }
        for(let i = 1; i < 4; i++) {
            if (this.nativePostsPosition[this.currentPost + i] && this.isCurrentPost(this.currentPost + i) ) {
                //this.currentPost+=i;
                this.setCurrentPostPosition(this.currentPost + i);
                return;
            }
            if (this.nativePostsPosition[this.currentPost + i] && this.currentPost !== 0 && this.isCurrentPost(this.currentPost - i) ) {
                //this.currentPost-=i;
                this.setCurrentPostPosition(this.currentPost - i);
                return;
            }
        }
        for(let i = 0; i < this.nativePostsPosition.length; i++ ){
            if (this.isCurrentPost(i) ) {
                //this.currentPost=i;
                this.setCurrentPostPosition(i);
                return;
            }
        }
    };

    setCurrentPostPosition(newPosition){
        this.currentPost = newPosition;
        this.posts[this.currentPost].Meta.saw = true;
        console.log('Current Post:',this.posts[newPosition].title);
    }

    onKeyPress(event){
        //console.log(event.keyCode);
        this.onScroll();

        if(event.keyCode === 100){
            if(this.nativePostsPosition[this.currentPost + 1]) {
                //window.scrollTo(0, this.nativePostsPosition[this.currentPost + 1][0]);
                let from = this._sb_windowTools.verticalOffset();
                let to = this.nativePostsPosition[this.currentPost + 1][0];
                this.smoothYScrollFromTo(from, to + 1, 50 );
            }
        }
        if(event.keyCode === 97) {
            if(this.nativePostsPosition[this.currentPost - 1]) {
                //window.scrollTo(0, this.nativePostsPosition[this.currentPost - 1][0]);
                let from = this._sb_windowTools.verticalOffset();
                let to = this.nativePostsPosition[this.currentPost - 1][0];
                this.smoothYScrollFromTo(to + 1, from, -50 );
            }
        }
    }

    smoothYScrollFromTo(from, to, rate){
        if(Math.abs(to - from) < Math.abs(rate)){
            if(rate > 0) {
                this.setCurrentPostPosition(this.currentPost + 1);
                window.scrollBy(0, to - from);
                //console.log('set +1');
                return;
            }else{
                //this.setCurrentPostPosition(this.currentPost - 1);  //couse we move from bot to top and steped on our posr multiple timses
                window.scrollBy(0, from - to);
                //console.log('set -1');
                return;
            }
        }else{
            window.scrollBy(0, rate);
            setTimeout(()=>{this.smoothYScrollFromTo(from, to - Math.abs(rate), rate);}, 25);
        }
    }

    isCurrentPost(postIndex){
        try {
            let post:Array<number> = this.nativePostsPosition[postIndex];
            let postY1:number = post[0];
            let postY2:number = post[1];
            if (this._sb_windowTools.verticalOffset() > postY1 && this._sb_windowTools.verticalOffset() < postY2) {
                return true;
            } else {
                return false
            }
        }catch (err){console.log('catched', err)}
    }

    stringAsDate(dateStr) {
        return new Date(dateStr);
    };

    getTrunkedContent(post_content) {
        if (post_content.length > this.truncateWord) {
            return post_content.slice(0, this.truncateWord);
        } else {
            return post_content;
        }
    };



}