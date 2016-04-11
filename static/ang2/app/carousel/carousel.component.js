System.register(["angular2/core", "../../static"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, core_2;
    var CarouselComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
                core_2 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            }],
        execute: function() {
            CarouselComponent = (function () {
                function CarouselComponent(elementRef) {
                    this.elementRef = elementRef;
                }
                CarouselComponent.prototype.ngOnInit = function () {
                    jQuery(this.elementRef.nativeElement).find('.owl-carousel').owlCarousel();
                };
                ;
                CarouselComponent = __decorate([
                    core_1.Component({
                        selector: 'my-carousel',
                        templateUrl: static_1.SrcURL + 'carousel/carousel.html',
                        styles: ["\n    "],
                        directives: [],
                        providers: [],
                    }), 
                    __metadata('design:paramtypes', [core_2.ElementRef])
                ], CarouselComponent);
                return CarouselComponent;
            })();
            exports_1("CarouselComponent", CarouselComponent);
        }
    }
});
//# sourceMappingURL=carousel.component.js.map