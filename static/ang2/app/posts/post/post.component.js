System.register(["../../../static", "angular2/core", "./content/content.component", "angular2-jwt", "./comments/comments.component"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var static_1, core_1, core_2, core_3, core_4, core_5, content_component_1, angular2_jwt_1, comments_component_1;
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
            },
            function (content_component_1_1) {
                content_component_1 = content_component_1_1;
            },
            function (angular2_jwt_1_1) {
                angular2_jwt_1 = angular2_jwt_1_1;
            },
            function (comments_component_1_1) {
                comments_component_1 = comments_component_1_1;
            }],
        execute: function() {
            PostComponent = (function () {
                function PostComponent(element) {
                    this.element = element;
                    this.contentToPlay = new core_4.EventEmitter();
                    this.postShow = 'content';
                    this.doTrunk = true;
                    this.contentImgLoadedDo = true;
                    this.linkCopyed = false;
                }
                PostComponent.prototype.ngAfterViewInit = function () {
                    this.updatePostHeight();
                };
                PostComponent.prototype.ngOnInit = function () {
                };
                PostComponent.prototype.updatePostHeight = function () {
                    var _this = this;
                    setTimeout(function () {
                        _this.height = _this.getNativeElement().offsetHeight;
                    }, 0);
                };
                //used for parent call!!!
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
                PostComponent.prototype.postShowIt = function () {
                    this.post.viewed = false;
                };
                PostComponent.prototype.contentImgLoaded = function () {
                    var _this = this;
                    if (this.contentImgLoadedDo) {
                        this.contentImgLoadedDo = false;
                        setTimeout(function () {
                            _this.contentImgLoadedDo = true;
                            _this.updatePostHeight();
                        }, 200);
                    }
                };
                PostComponent.prototype.friendsViewed = function () {
                    if (this.autenticated()) {
                        return this.post.friendsViewed.length;
                    }
                    else {
                        return 0;
                    }
                };
                PostComponent.prototype.autenticated = function () {
                    return angular2_jwt_1.tokenNotExpired();
                };
                PostComponent.prototype.postShowIs = function (switchState) {
                    return this.postShow === switchState;
                };
                PostComponent.prototype.copyTextToClipboard = function (text) {
                    var _this = this;
                    var textArea = document.createElement("textarea");
                    //
                    // *** This styling is an extra step which is likely not required. ***
                    //
                    // Why is it here? To ensure:
                    // 1. the element is able to have focus and selection.
                    // 2. if element was to flash render it has minimal visual impact.
                    // 3. less flakyness with selection and copying which **might** occur if
                    //    the textarea element is not visible.
                    //
                    // The likelihood is the element won't even render, not even a flash,
                    // so some of these are just precautions. However in IE the element
                    // is visible whilst the popup box asking the user for permission for
                    // the web page to copy to the clipboard.
                    //
                    // Place in top-left corner of screen regardless of scroll position.
                    textArea.style.position = 'fixed';
                    textArea.style.top = 0;
                    textArea.style.left = 0;
                    // Ensure it has a small width and height. Setting to 1px / 1em
                    // doesn't work as this gives a negative w/h on some browsers.
                    textArea.style.width = '2em';
                    textArea.style.height = '2em';
                    // We don't need padding, reducing the size if it does flash render.
                    textArea.style.padding = 0;
                    // Clean up any borders.
                    textArea.style.border = 'none';
                    textArea.style.outline = 'none';
                    textArea.style.boxShadow = 'none';
                    // Avoid flash of white box if rendered for any reason.
                    textArea.style.background = 'transparent';
                    textArea.value = text;
                    document.body.appendChild(textArea);
                    textArea.select();
                    try {
                        var successful = document.execCommand('copy');
                        if (successful) {
                            this.linkCopyed = true;
                            setTimeout(function () { _this.linkCopyed = false; }, 1500);
                        }
                        else {
                            window.prompt("Copy to clipboard: Ctrl+C, Enter", text);
                        }
                        ;
                    }
                    catch (err) {
                        console.log('Oops, unable to copy');
                    }
                    document.body.removeChild(textArea);
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
                        directives: [content_component_1.PostContentComponent, comments_component_1.CommentsComponent],
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