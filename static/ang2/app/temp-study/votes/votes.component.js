System.register(["angular2/core", "../../../static", "./votes.service", "angular2/common"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, votes_service_1, common_1, common_2, common_3;
    var VotesComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (votes_service_1_1) {
                votes_service_1 = votes_service_1_1;
            },
            function (common_1_1) {
                common_1 = common_1_1;
                common_2 = common_1_1;
                common_3 = common_1_1;
            }],
        execute: function() {
            VotesComponent = (function () {
                function VotesComponent(_votesService) {
                    this._votesService = _votesService;
                }
                ;
                VotesComponent.prototype.ngOnInit = function () {
                    this.getVotes();
                };
                ;
                VotesComponent.prototype.getVotes = function () {
                    var _this = this;
                    this._votesService.getVotes().subscribe(function (votes) { return _this.votes = votes; });
                };
                ;
                VotesComponent.prototype.onSelectVote = function (vote) {
                    this.SelectedVote = vote;
                    this.switchValue = 'voteSelected';
                };
                ;
                VotesComponent.prototype.doVotes = function (vote_id, choice_id) {
                    this._votesService.doVotes(vote_id, choice_id).subscribe();
                    this.switchValue = 'voted';
                };
                VotesComponent.prototype.onBack = function () {
                    this.SelectedVote = null;
                    this.switchValue = null;
                };
                VotesComponent.prototype.getChoicePercent = function (SelectedVote, choice_votes) {
                    var arrayLength = SelectedVote.choices.length;
                    var choicesSumm = 0;
                    for (var i = 0; i < arrayLength; i++) {
                        choicesSumm += SelectedVote.choices[i].votes;
                    }
                    return choice_votes / choicesSumm * 100;
                };
                VotesComponent = __decorate([
                    core_1.Component({
                        selector: 'my-votes',
                        templateUrl: static_1.SrcURL + 'temp-study/votes/votes.html',
                        styles: ["\n    .wrapper{\n    }\n\n    .first  {\n    list-style: none;\n    padding: 0;\n    }\n\n    .first li {\n    text-align: center;\n    border-radius: 15px;\n    padding: 10px 30px;\n    background: linear-gradient(to left, #f8ab8d 0%, white, #f8ab8d);\n    border-bottom: 1px solid grey;\n    color: #506a6b;\n    box-shadow: 0 5px 5px 0 rgba(0,0,0, .2);\n    margin-bottom: 5px;\n    }\n\n    .first li:last-child {\n    border-bottom: none;\n    }\n\n    .choices {\n    cursor: pointer;\n    }\n\n    .choices:hover {\n    color: blue;\n    border-left: 3px solid green;\n    border-right: 3px solid green;\n    }\n    "],
                        directives: [common_1.NgSwitch, common_2.NgSwitchWhen, common_3.NgSwitchDefault],
                        providers: [votes_service_1.VotesService],
                    }), 
                    __metadata('design:paramtypes', [votes_service_1.VotesService])
                ], VotesComponent);
                return VotesComponent;
            })();
            exports_1("VotesComponent", VotesComponent);
        }
    }
});
//# sourceMappingURL=votes.component.js.map