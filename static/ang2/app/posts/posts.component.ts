import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {PostsService} from "./posts.service";
import {OnInit} from "angular2/core";
import {sb_windowTools} from "../helpers/sb_windowTools";
import {ElementRef} from "angular2/core";

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
    posts:any;
    truncateWord:number;
    scrollPercent:number;
    gettingPosts:boolean;
    getPostsEnd:number;
    getPostsStart:number;
    getPostsDelta:number;
    pageHeight:number;

    constructor(public element:ElementRef,
                private _postsService:PostsService,
                private _sb_windowTools:sb_windowTools) {
        this.truncateWord = 300;
        this.gettingPosts = true;
        this.getPostsEnd = 10;
        this.getPostsStart = 0;
        this.getPostsDelta = 5;
        this.posts = [];
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
                'offset': null,
            }
        }
    };

    onScroll() {
        this._sb_windowTools.updateDimensions();
        this.scrollPercent = (this._sb_windowTools.windowHeight() + this._sb_windowTools.verticalOffset()) / this._sb_windowTools.pageHeight();
        if (this.scrollPercent > 0.90 && !this.gettingPosts) {
            this.getPostsEnd += this.getPostsDelta;
            this.getPosts(this.getPostsEnd - this.getPostsDelta, this.getPostsEnd);
            this.gettingPosts = true;
        }
    };

    stringAsDate(dateStr) {
        return new Date(dateStr);
    };

    getTrunkedContent(post_content) {
        if (post_content.length > this.truncateWord) {
            return post_content.slice(0, this.truncateWord);
        } else {
            return post_content
        }
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

}