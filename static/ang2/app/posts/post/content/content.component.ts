import { SrcURL } from "../../../../static";
import { Component } from "angular2/core";
import { OnInit } from "angular2/core";
import { Input } from "angular2/core";
import { Output } from "angular2/core";
import { EventEmitter } from "angular2/core";
import { ElementRef } from "angular2/core";
import { AfterViewInit } from "angular2/core";
import {OnDestroy} from "angular2/core";
import {AfterContentInit} from "angular2/core";

@Component({
    selector: 'my-post-content',
    templateUrl: SrcURL + 'posts/post/content/content.html',
    styleUrls: [SrcURL + 'posts/post/content/content.css'],
    directives: [],
    providers: [],
})

export class PostContentComponent implements OnInit {

    @Input() content;
    @Output() contentToPlay = new EventEmitter();
    @Output() contentImgLoaded = new EventEmitter();

    constructor() {
    }

    ngOnInit() {
        this.content['Meta'] = {
            'play': false,
        }
    }


    contentPlay(){
        this.contentToPlay.emit(true)
    }

    imgLoaded(){
        this.contentImgLoaded.emit(true)
    }

}