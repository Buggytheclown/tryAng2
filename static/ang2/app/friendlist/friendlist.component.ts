import {SrcURL} from "../../static";
import {Component} from "angular2/core";
import {OnInit} from "angular2/core";
import {FriendlistService} from "./friendlist.service";


@Component({
    selector: 'my-friendlist',
    templateUrl: SrcURL + 'friendlist/friendlist.html',
    styleUrls: [SrcURL + 'friendlist/friendlist.css'],
    directives: [],
    providers: [FriendlistService],
})

export class FriendlistComponent implements OnInit {
    hidden:boolean = true;
    showAddFriend:boolean = false;
    userOnDelete:string = '';
    showDeleteConfirm:boolean = false;
    friendslist:Array<string> = [];
    addFriendMessage:string = '';
    addFriendWaiting:boolean = false;

    constructor(private _FriendlistService:FriendlistService) {
    }

    ngOnInit() {
        this.getFriends();
    }

    toggleHide() {
        this.hidden = !this.hidden
    }

    getFriends() {
        this._FriendlistService.getFriendlist().subscribe((friends)=> {
                this.friendslist = friends
            }, (ex)=> {
                console.log(ex)
            }
        )
    }

    updateFriends() {
        setTimeout(()=> {
            this.getFriends()
        }, 100)
    }


    addFriend(friend) {
        if (!this.addFriendWaiting) {
            this.addFriendWaiting = true;
            this._FriendlistService.addFriend(friend).subscribe((response)=> {
                    if (response.created[0]) {
                        this.addFriendMessage = 'Friendship creadet! ;)';
                        this.addFriendWaiting = false;
                        this.updateFriends();
                    } else {
                        this.addFriendMessage = friend + ' is already your friend!';
                        this.addFriendWaiting = false;
                    }
                }, (ex)=> {
                    this.addFriendMessage = friend + ' - no such user to be friend with! :(';
                    this.addFriendWaiting = false;
                }
            );
        }
    }


    deleteFriend(friend) {
        this.userOnDelete = '';
        this._FriendlistService.deleteFriend(friend).subscribe((response)=> {
            }, (ex)=> {
                console.log(ex);
            }
        );
        this.updateFriends();
    }

}
