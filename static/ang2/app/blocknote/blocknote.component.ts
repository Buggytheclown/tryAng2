import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {NgForm} from "angular2/common";


@Component({
    selector: 'my-blocknote',
    templateUrl:SrcURL+'blocknote/blocknote.html',
    styles: [`
    .readonly{
        border-width:0px;
        border:none;
    }

    .input-number{
        width:4em;
    }
    `],
    directives: [],
    providers: [],
})

export class BlocknoteComponent {
    notes:Array<Object> = [];

    constructor() { }

    addNext(content, remark){
        this.notes.push({
            'number':this.notes.length + 1,
            'content': content,
            'remark':remark,
        });
    }

}