import {SrcURL} from "../../../static";
import {Component} from "angular2/core";
import {OnInit} from "angular2/core";
import {Input} from "angular2/core";
import {Posts} from "../posts.interface";
import {Output} from "angular2/core";
import {EventEmitter} from "angular2/core";
import {ElementRef} from "angular2/core";
import {AfterViewInit} from "angular2/core";

@Component({
    selector: 'my-post',
    templateUrl: SrcURL + 'posts/post/post.html',
    styleUrls: [SrcURL + 'posts/post/post.css'],
    directives: [],
    providers: [],
})

export class PostComponent implements OnInit, AfterViewInit {
    @Input() post:Posts;
    @Output() contentToPlay = new EventEmitter();
    postShow:string = 'content';
    height:number;

    constructor(public element:ElementRef) {
    }

    ngAfterViewInit() {
        //this.initMove();
         setTimeout(()=>this.height = this.getNativeElement().offsetHeight, 0)
    }

    //initMove() {
    //    this.height = this.getNativeElement().offsetHeight;
    //    console.log( this.height);
    //    if (this.height === undefined) {
    //        setTimeout(()=>this.initMove(), 50)
    //    }
    //}

    ngOnInit() {}

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

    contentStop(icontent:number) {
        this.post.contents[icontent]['Meta'] = {
            'play': false,
        }
    }
}