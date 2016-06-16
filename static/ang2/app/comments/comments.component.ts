import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {CommentsService} from "./comments.service";
import {OnInit} from "angular2/core";
import {Comments} from "./comments.interface";
import {CommentComponent} from "./comment/comment";
import {Input} from "angular2/core";

@Component({
    selector: 'my-comments',
    templateUrl: SrcURL + 'comments/comments.html',
    styleUrls: [SrcURL + 'comments/comments.css'],
    directives: [CommentComponent],
    providers: [CommentsService],
})

export class CommentsComponent implements OnInit {
    comments:Array<Comments>;
    @Input() url;

    constructor(private _CommentsService:CommentsService) {
    }

    ngOnInit() {
        this.getComment(this.url);
        //this._CommentsService.getMockComments().then(comments=>this.comments = comments);
    }

    getComment(url) {
        this._CommentsService.getComments(url).subscribe(comments=> {
            this.comments = comments
        }, err=> {
            console.log(err)
        })
    }
}