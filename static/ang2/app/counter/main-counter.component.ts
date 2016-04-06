import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {CounterComponent} from "./counter.component";


@Component({
    selector: 'my-mainCounter',
    template: `<button (click)="addCounter()">Add counter</button>
    <my-counter
        *ngFor="#val of model; #i=index"
        [count]="val"
        (updater)="pupdate(i)($event)">
    </my-counter>
    `,
    styles: [``],
    directives: [CounterComponent],
    providers: [],
})

export class CounterMainComponent {
    model:Array<Number>;

    constructor() {
        this.model = [];
    }

    addCounter() {
        this.model.push(0);
    }

    pupdate(modelIndex) {
        return (newVal=>this.model[modelIndex] = newVal);
    }
}