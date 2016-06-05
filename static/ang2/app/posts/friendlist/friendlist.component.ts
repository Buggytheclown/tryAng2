import {SrcURL} from "../../../static";
import {Component} from "angular2/core";
import {OnInit} from "angular2/core";
import {FriendlistService} from "./friendlist.service";


@Component({
    selector: 'my-friendlist',
    templateUrl: SrcURL + 'posts/friendlist/friendlist.html',
    styleUrls: [SrcURL + 'posts/friendlist/friendlist.css'],
    directives: [],
    providers: [FriendlistService],
})

export class FriendlistComponent implements OnInit{
    hidden:boolean = true;
    showAddFriend:boolean = false;
    userOnDelete:string = '';
    showDeleteConfirm:boolean = false;
    friendslist:Array<string> = [];

    constructor(private _FriendlistService:FriendlistService){}

    ngOnInit(){this._FriendlistService.getFriendlist().subscribe(friends=>this.friendslist = friends, ex=>console.log(ex))}

    toggleHide(){
        this.hidden = !this.hidden
    }

    addFriend(value){
        console.log('add', value);
    }

    deleteFriend(friend){
        this.userOnDelete = '';
        console.log('delete', friend);
    }

}
