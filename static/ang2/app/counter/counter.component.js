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
    var core_1, static_1, core_2, core_3, core_4;
    var CounterComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
                core_2 = core_1_1;
                core_3 = core_1_1;
                core_4 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            }],
        execute: function() {
            CounterComponent = (function () {
                function CounterComponent() {
                    this.updater = new core_2.EventEmitter();
                }
                CounterComponent.prototype.action = function (val) {
                    var delta = (val === 'inc') ? 1 : -1;
                    this.updater.emit(this.count + delta);
                };
                __decorate([
                    core_4.Input(), 
                    __metadata('design:type', Object)
                ], CounterComponent.prototype, "count", void 0);
                __decorate([
                    core_3.Output(), 
                    __metadata('design:type', Object)
                ], CounterComponent.prototype, "updater", void 0);
                CounterComponent = __decorate([
                    core_1.Component({
                        selector: 'my-counter',
                        templateUrl: static_1.SrcURL + 'html/counter.html',
                        styles: [""],
                        directives: [],
                        providers: [],
                    }), 
                    __metadata('design:paramtypes', [])
                ], CounterComponent);
                return CounterComponent;
            })();
            exports_1("CounterComponent", CounterComponent);
        }
    }
});
//# sourceMappingURL=counter.component.js.map