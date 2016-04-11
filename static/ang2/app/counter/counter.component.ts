import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {EventEmitter} from "angular2/core";
import {Output} from "angular2/core";
import {Input} from "angular2/core";


@Component({
    selector: 'my-counter',
    templateUrl: SrcURL + 'counter/counter.html',
    styles: [``],
    directives: [],
    providers: [],
})

export class CounterComponent {
    @Input() count;
    @Output() updater = new EventEmitter();

    constructor() {
    }

    action(val) {
        let delta:Number = (val === 'inc') ? 1 : -1;
        this.updater.emit(this.count + delta);
    }
}