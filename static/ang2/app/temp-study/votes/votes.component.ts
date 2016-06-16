import {Component} from "angular2/core";
import {SrcURL} from "../../../static";
import {OnInit} from "angular2/core";
import {VotesService} from "./votes.service";
import {NgSwitch} from "angular2/common";
import {NgSwitchWhen} from "angular2/common";
import {NgSwitchDefault} from "angular2/common";

@Component({
    selector: 'my-votes',
    templateUrl: SrcURL + 'temp-study/votes/votes.html',
    styles:[`
    .wrapper{
    }

    .first  {
    list-style: none;
    padding: 0;
    }

    .first li {
    text-align: center;
    border-radius: 15px;
    padding: 10px 30px;
    background: linear-gradient(to left, #f8ab8d 0%, white, #f8ab8d);
    border-bottom: 1px solid grey;
    color: #506a6b;
    box-shadow: 0 5px 5px 0 rgba(0,0,0, .2);
    margin-bottom: 5px;
    }

    .first li:last-child {
    border-bottom: none;
    }

    .choices {
    cursor: pointer;
    }

    .choices:hover {
    color: blue;
    border-left: 3px solid green;
    border-right: 3px solid green;
    }
    `],
    directives: [NgSwitch, NgSwitchWhen, NgSwitchDefault],
    providers:[VotesService],
})

export class VotesComponent implements OnInit {
    switchValue:any;
    votes:any;
    SelectedVote:any;

    constructor(private _votesService:VotesService){};
    ngOnInit(){
        this.getVotes()
    };

    getVotes(){
        this._votesService.getVotes().subscribe(votes=>this.votes = votes)
    };

    onSelectVote(vote){
        this.SelectedVote = vote;
        this.switchValue = 'voteSelected';
    };

    doVotes(vote_id, choice_id){
        this._votesService.doVotes(vote_id, choice_id).subscribe();
        this.switchValue = 'voted';
    }

    onBack(){
        this.SelectedVote = null;
        this.switchValue = null;
    }

    getChoicePercent(SelectedVote, choice_votes){
        let arrayLength = SelectedVote.choices.length;
        let choicesSumm = 0;
        for (let i = 0; i < arrayLength; i++) {
           choicesSumm += SelectedVote.choices[i].votes;
        }
        return choice_votes/choicesSumm*100;
    }
}