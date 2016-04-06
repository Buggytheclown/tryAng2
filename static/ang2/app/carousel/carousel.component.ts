import {Component} from "angular2/core";
import {SrcURL} from "../../static";
import {OnInit} from "angular2/core";
import {ElementRef} from "angular2/core";
import {Inject} from "angular2/core";

declare var jQuery:any;

@Component({
    selector: 'my-carousel',
    templateUrl: SrcURL + 'html/carousel.html',
    styles: [`
    `],
    directives: [],
    providers: [],
})

export class CarouselComponent implements OnInit {
    elementRef: ElementRef;

   constructor(elementRef: ElementRef) {
        this.elementRef = elementRef;
    }

    ngOnInit() {
        jQuery(this.elementRef.nativeElement).find('.owl-carousel').owlCarousel();
    };

}
