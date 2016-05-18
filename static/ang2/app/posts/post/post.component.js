System.register(["../../../static", "angular2/core"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var static_1, core_1, core_2, core_3, core_4, core_5;
    var PostComponent;
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
                core_5 = core_1_1;
            }],
        execute: function() {
            PostComponent = (function () {
                function PostComponent(element) {
                    this.element = element;
                    this.contentToPlay = new core_4.EventEmitter();
                    this.postShow = 'content';
                }
                PostComponent.prototype.ngAfterViewInit = function () {
                    var _this = this;
                    //this.initMove();
                    setTimeout(function () { return _this.height = _this.getNativeElement().offsetHeight; }, 0);
                };
                //initMove() {
                //    this.height = this.getNativeElement().offsetHeight;
                //    console.log( this.height);
                //    if (this.height === undefined) {
                //        setTimeout(()=>this.initMove(), 50)
                //    }
                //}
                PostComponent.prototype.ngOnInit = function () { };
                PostComponent.prototype.getNativeElement = function () {
                    //for parent bindings, firstChild is needed (<my-post> is inline element)
                    return this.element.nativeElement.firstChild;
                };
                PostComponent.prototype.stringAsDate = function (dateStr) {
                    return new Date(dateStr);
                };
                ;
                PostComponent.prototype.contentPlay = function (icontent) {
                    this.contentToPlay.emit(icontent);
                };
                PostComponent.prototype.contentStop = function (icontent) {
                    this.post.contents[icontent]['Meta'] = {
                        'play': false,
                    };
                };
                __decorate([
                    core_2.Input(), 
                    __metadata('design:type', Object)
                ], PostComponent.prototype, "post", void 0);
                __decorate([
                    core_3.Output(), 
                    __metadata('design:type', Object)
                ], PostComponent.prototype, "contentToPlay", void 0);
                PostComponent = __decorate([
                    core_1.Component({
                        selector: 'my-post',
                        templateUrl: static_1.SrcURL + 'posts/post/post.html',
                        styleUrls: [static_1.SrcURL + 'posts/post/post.css'],
                        directives: [],
                        providers: [],
                    }), 
                    __metadata('design:paramtypes', [core_5.ElementRef])
                ], PostComponent);
                return PostComponent;
            })();
            exports_1("PostComponent", PostComponent);
        }
    }
});
//# sourceMappingURL=post.component.js.map