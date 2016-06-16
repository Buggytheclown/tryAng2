System.register(["angular2/core", "./counter.component"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, counter_component_1;
    var CounterMainComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (counter_component_1_1) {
                counter_component_1 = counter_component_1_1;
            }],
        execute: function() {
            CounterMainComponent = (function () {
                function CounterMainComponent() {
                    this.model = [];
                }
                CounterMainComponent.prototype.addCounter = function () {
                    this.model.push(0);
                };
                CounterMainComponent.prototype.pupdate = function (modelIndex) {
                    var _this = this;
                    return (function (newVal) { return _this.model[modelIndex] = newVal; });
                };
                CounterMainComponent = __decorate([
                    core_1.Component({
                        selector: 'my-mainCounter',
                        template: "<button (click)=\"addCounter()\">Add counter</button>\n    <my-counter\n        *ngFor=\"#val of model; #i=index\"\n        [count]=\"val\"\n        (updater)=\"pupdate(i)($event)\">\n    </my-counter>\n    ",
                        styles: [""],
                        directives: [counter_component_1.CounterComponent],
                        providers: [],
                    }), 
                    __metadata('design:paramtypes', [])
                ], CounterMainComponent);
                return CounterMainComponent;
            })();
            exports_1("CounterMainComponent", CounterMainComponent);
        }
    }
});
//# sourceMappingURL=main-counter.component.js.map