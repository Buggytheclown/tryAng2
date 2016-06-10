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
import {CommentsComponent} from "./comments/comments.component";
import {ViewChild} from "angular2/core";

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
    postShow:string = 'content';
    height:number;
    doTrunk:boolean = true;
    contentImgLoadedDo:boolean = true;
    linkCopyed: boolean = false;

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

    copyTextToClipboard(text) {
        var textArea = document.createElement("textarea");

        //
        // *** This styling is an extra step which is likely not required. ***
        //
        // Why is it here? To ensure:
        // 1. the element is able to have focus and selection.
        // 2. if element was to flash render it has minimal visual impact.
        // 3. less flakyness with selection and copying which **might** occur if
        //    the textarea element is not visible.
        //
        // The likelihood is the element won't even render, not even a flash,
        // so some of these are just precautions. However in IE the element
        // is visible whilst the popup box asking the user for permission for
        // the web page to copy to the clipboard.
        //

        // Place in top-left corner of screen regardless of scroll position.
        textArea.style.position = 'fixed';
        textArea.style.top = 0;
        textArea.style.left = 0;

        // Ensure it has a small width and height. Setting to 1px / 1em
        // doesn't work as this gives a negative w/h on some browsers.
        textArea.style.width = '2em';
        textArea.style.height = '2em';

        // We don't need padding, reducing the size if it does flash render.
        textArea.style.padding = 0;

        // Clean up any borders.
        textArea.style.border = 'none';
        textArea.style.outline = 'none';
        textArea.style.boxShadow = 'none';

        // Avoid flash of white box if rendered for any reason.
        textArea.style.background = 'transparent';


        textArea.value = text;

        document.body.appendChild(textArea);

        textArea.select();

        try {
            var successful = document.execCommand('copy');
            if(successful){this.linkCopyed = true; setTimeout(()=>{this.linkCopyed = false}, 1500)}
            else {window.prompt("Copy to clipboard: Ctrl+C, Enter", text);};
        } catch (err) {
            console.log('Oops, unable to copy');
        }

        document.body.removeChild(textArea);
    }

}