System.register(["../../../static", "angular2/core", "./friendlist.service"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var static_1, core_1, friendlist_service_1;
    var FriendlistComponent;
    return {
        setters:[
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (friendlist_service_1_1) {
                friendlist_service_1 = friendlist_service_1_1;
            }],
        execute: function() {
            FriendlistComponent = (function () {
                function FriendlistComponent(_FriendlistService) {
                    this._FriendlistService = _FriendlistService;
                    this.hidden = true;
                    this.showAddFriend = false;
                    this.userOnDelete = '';
                    this.showDeleteConfirm = false;
                    this.friendslist = [];
                    this.addFriendMessage = '';
                    this.addFriendWaiting = false;
                }
                FriendlistComponent.prototype.ngOnInit = function () {
                    this.getFriends();
                };
                FriendlistComponent.prototype.toggleHide = function () {
                    this.hidden = !this.hidden;
                };
                FriendlistComponent.prototype.getFriends = function () {
                    var _this = this;
                    this._FriendlistService.getFriendlist().subscribe(function (friends) {
                        _this.friendslist = friends;
                    }, function (ex) {
                        console.log(ex);
                    });
                };
                FriendlistComponent.prototype.updateFriends = function () {
                    var _this = this;
                    setTimeout(function () {
                        _this.getFriends();
                    }, 100);
                };
                FriendlistComponent.prototype.addFriend = function (friend) {
                    var _this = this;
                    if (!this.addFriendWaiting) {
                        this.addFriendWaiting = true;
                        this._FriendlistService.addFriend(friend).subscribe(function (response) {
                            if (response.created[0]) {
                                _this.addFriendMessage = 'Friendship creadet! ;)';
                                _this.addFriendWaiting = false;
                                _this.updateFriends();
                            }
                            else {
                                _this.addFriendMessage = friend + ' is already your friend!';
                                _this.addFriendWaiting = false;
                            }
                        }, function (ex) {
                            _this.addFriendMessage = friend + ' - no such user to be friend with! :(';
                            _this.addFriendWaiting = false;
                        });
                    }
                };
                FriendlistComponent.prototype.deleteFriend = function (friend) {
                    this.userOnDelete = '';
                    this._FriendlistService.deleteFriend(friend).subscribe(function (response) {
                    }, function (ex) {
                        console.log(ex);
                    });
                    this.updateFriends();
                };
                FriendlistComponent = __decorate([
                    core_1.Component({
                        selector: 'my-friendlist',
                        templateUrl: static_1.SrcURL + 'posts/friendlist/friendlist.html',
                        styleUrls: [static_1.SrcURL + 'posts/friendlist/friendlist.css'],
                        directives: [],
                        providers: [friendlist_service_1.FriendlistService],
                    }), 
                    __metadata('design:paramtypes', [friendlist_service_1.FriendlistService])
                ], FriendlistComponent);
                return FriendlistComponent;
            })();
            exports_1("FriendlistComponent", FriendlistComponent);
        }
    }
});
//# sourceMappingURL=friendlist.component.js.map