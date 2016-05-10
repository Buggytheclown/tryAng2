import {SrcURL} from "../../../static";
import {Component} from "angular2/core";
import {OnInit} from "angular2/core";
import {Input} from "angular2/core";
import {Posts} from "../posts.interface";
import {Output} from "angular2/core";
import {EventEmitter} from "angular2/core";
import {ElementRef} from "angular2/core";

@Component({
    selector: 'my-post',
    templateUrl: SrcURL + 'posts/post/post.html',
    styleUrls: [SrcURL + 'posts/post/post.css'],
    directives: [],
    providers: [],
})

export class PostComponent implements OnInit {
    @Input() post:Posts;
    @Output() contentToPlay = new EventEmitter();

    constructor(public element:ElementRef){}

    ngOnInit() {}

    getNativeElement(){
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