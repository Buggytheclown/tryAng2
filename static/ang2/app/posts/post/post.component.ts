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

@Component({
    selector: 'my-post',
    templateUrl: SrcURL + 'posts/post/post.html',
    styleUrls: [SrcURL + 'posts/post/post.css'],
    directives: [PostContentComponent],
    providers: [],
})

export class PostComponent implements OnInit, AfterViewInit {
    @Input() post:Posts;
    @Output() contentToPlay = new EventEmitter();
    postShow:string = 'content';
    height:number;
    doTrunk:boolean = true;
    contentImgLoadedDo:boolean = true;

    constructor(public element:ElementRef) {
    }

    ngAfterViewInit() {
        this.updatePostHeight();
    }

    ngOnInit() {
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

    friendsViewed():number{
        return this.post.friendsViewed.length
    }

}