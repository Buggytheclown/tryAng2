import {Component} from "angular2/core";
import {SrcURL} from "../../../../../static";
import {Input} from "angular2/core";
import {OnInit} from "angular2/core";
import {DateFromUTCPipe} from "../../../../helpers/dateFromUTC";

@Component({
    selector: 'my-comment',
    //recursive links
    templateUrl: SrcURL + 'posts/post/comments/comment/comment.html',
    styleUrls: [SrcURL + 'posts/post/comments/comment/comment.css'],
    directives: [CommentComponent],
    providers: [],
    pipes: [DateFromUTCPipe]
})

export class CommentComponent implements OnInit{
    @Input() comment;
    @Input() showChild;
    countChildrens:number=0;

    ngOnInit(){
        this.setCountChildrens(this.comment.child);
    }

    setCountChildrens(comments){
        for (let i=0; i < comments.length; i++){
            this.countChildrens++;
            if(comments[i].child.length > 0){
                this.setCountChildrens(comments[i].child)
            }
        }
    }
}
