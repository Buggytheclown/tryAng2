System.register(["../../../../static", "angular2/core"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var static_1, core_1, core_2, core_3, core_4;
    var PostContentComponent;
    return {
        setters:[
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
                core_2 = core_1_1;
                core_3 = core_1_1;
                core_4 = core_1_1;
            }],
        execute: function() {
            PostContentComponent = (function () {
                function PostContentComponent() {
                    this.contentToPlay = new core_4.EventEmitter();
                    this.contentImgLoaded = new core_4.EventEmitter();
                }
                PostContentComponent.prototype.ngOnInit = function () {
                    this.content['Meta'] = {
                        'play': false,
                    };
                };
                PostContentComponent.prototype.contentPlay = function () {
                    this.contentToPlay.emit(true);
                };
                PostContentComponent.prototype.imgLoaded = function () {
                    this.contentImgLoaded.emit(true);
                };
                __decorate([
                    core_2.Input(), 
                    __metadata('design:type', Object)
                ], PostContentComponent.prototype, "content", void 0);
                __decorate([
                    core_3.Output(), 
                    __metadata('design:type', Object)
                ], PostContentComponent.prototype, "contentToPlay", void 0);
                __decorate([
                    core_3.Output(), 
                    __metadata('design:type', Object)
                ], PostContentComponent.prototype, "contentImgLoaded", void 0);
                PostContentComponent = __decorate([
                    core_1.Component({
                        selector: 'my-post-content',
                        templateUrl: static_1.SrcURL + 'posts/post/content/content.html',
                        styleUrls: [static_1.SrcURL + 'posts/post/content/content.css'],
                        directives: [],
                        providers: [],
                    }), 
                    __metadata('design:paramtypes', [])
                ], PostContentComponent);
                return PostContentComponent;
            })();
            exports_1("PostContentComponent", PostContentComponent);
        }
    }
});
//# sourceMappingURL=content.component.js.map