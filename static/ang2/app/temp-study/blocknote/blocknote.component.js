System.register(["angular2/core", "../../../static"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1;
    var BlocknoteComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            }],
        execute: function() {
            BlocknoteComponent = (function () {
                function BlocknoteComponent() {
                    this.notes = [];
                }
                BlocknoteComponent.prototype.addNext = function (content, remark) {
                    this.notes.push({
                        'number': this.notes.length + 1,
                        'content': content,
                        'remark': remark,
                    });
                };
                BlocknoteComponent = __decorate([
                    core_1.Component({
                        selector: 'my-blocknote',
                        templateUrl: static_1.SrcURL + 'temp-study/blocknote/blocknote.html',
                        styles: ["\n    .readonly{\n        border-width:0px;\n        border:none;\n    }\n\n    .input-number{\n        width:4em;\n    }\n    "],
                        directives: [],
                        providers: [],
                    }), 
                    __metadata('design:paramtypes', [])
                ], BlocknoteComponent);
                return BlocknoteComponent;
            })();
            exports_1("BlocknoteComponent", BlocknoteComponent);
        }
    }
});
//# sourceMappingURL=blocknote.component.js.map