import {SrcURL} from "../../../static";
import {Component} from "angular2/core";
import {OnInit} from "angular2/core";
import {Input} from "angular2/core";
import {Posts} from "../posts.interface";
import {Output} from "angular2/core";
import {EventEmitter} from "angular2/core";
import {ElementRef} from "angular2/core";
import {AfterViewInit} from "angular2/core";
import {PostContentComponent} from "./content/content.component";
import {OnDestroy} from "angular2/core";
import {tokenNotExpired} from "angular2-jwt";
import {CommentsComponent} from "../../comments/comments.component";
import {ViewChild} from "angular2/core";
import {copyToClipboard} from "../../helpers/copyTextToClipboard";
import {ChangeDetectorRef} from "angular2/core";

@Component({
    selector: 'my-post',
    templateUrl: SrcURL + 'posts/post/post.html',
    styleUrls: [SrcURL + 'posts/post/post.css'],
    directives: [PostContentComponent, CommentsComponent],
    providers: [],
})

export class PostComponent implements OnInit, AfterViewInit {
    @Input() post:Posts;
    @Output() contentToPlay = new EventEmitter();
    @Input() windowWidth;
    windowWidthVal:number = 500;
    navCollapse:boolean=false;
    navCollapseHide:boolean=true;
    postShow:string = 'content';
    height:number;
    doTrunk:boolean = true;
    contentImgLoadedDo:boolean = true;
    linkCopyed:boolean = false;

    constructor(public element:ElementRef, private refDetector: ChangeDetectorRef) {
    }

    ngAfterViewInit() {
        this.updatePostHeight();
    }

    ngOnInit() {
        this.navCollapse = window.innerWidth < this.windowWidthVal;
        this.windowWidth.subscribe((val)=> {
            this.navCollapse = val < this.windowWidthVal;
            this.refDetector.detectChanges();
        })
    }

    updatePostHeight() {
        setTimeout(()=> {
            this.height = this.getNativeElement().offsetHeight;
        }, 0);

    }

    //used for parent call!!!
    getNativeElement() {
        //for parent bindings, firstChild is needed (<my-post> is inline element)
        return this.element.nativeElement.firstChild;
    }

    stringAsDate(dateStr) {
        return new Date(dateStr);
    };

    contentPlay(icontent) {
        this.contentToPlay.emit(icontent)
    }

    postShowIt() {
        this.post.viewed = false;
    }

    contentImgLoaded() {
        if (this.contentImgLoadedDo) {
            this.contentImgLoadedDo = false;
            setTimeout(()=> {
                this.contentImgLoadedDo = true;
                this.updatePostHeight();
            }, 200);

        }
    }

    friendsViewed():number {
        if (this.autenticated()) {
            return this.post.friendsViewed.length
        } else {
            return 0
        }
    }

    autenticated() {
        return tokenNotExpired();
    }

    postShowIs(switchState:string):boolean {
        return this.postShow === switchState
    }

    copyTextToClipboard(text:string) {
        let success = copyToClipboard(text);
        if (success) {
            this.linkCopyed = true;
            setTimeout(()=> {
                this.linkCopyed = false
            }, 1500)
        } else {
            console.log('Oops, unable to copy')
        }
    }


}