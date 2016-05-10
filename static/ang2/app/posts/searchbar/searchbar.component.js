System.register(["angular2/core", "../../../static", "angular2/router"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, router_1, router_2;
    var SearchbarComponent;
    return {
        setters:[
            function (core_1_1) {
                core_1 = core_1_1;
            },
            function (static_1_1) {
                static_1 = static_1_1;
            },
            function (router_1_1) {
                router_1 = router_1_1;
                router_2 = router_1_1;
            }],
        execute: function() {
            SearchbarComponent = (function () {
                function SearchbarComponent(_router, _routeParams) {
                    this._router = _router;
                    this._routeParams = _routeParams;
                }
                SearchbarComponent.prototype.ngOnInit = function () {
                    var someDate = this._routeParams.get('date');
                    if (someDate) {
                        this.routeDate = this.getReversedDate(someDate);
                    }
                    else {
                        this.routeDate = this.getDateNow();
                    }
                };
                SearchbarComponent.prototype.routeIt = function (date) {
                    //date need to be "dd-mm-yyyy"
                    var dateNow = new Date();
                    var dateIn = new Date(date);
                    var routeDate = '';
                    var revrouteDate = '';
                    if (dateIn && dateIn - dateNow <= 0) {
                        revrouteDate = this.getReversedDate(date);
                    }
                    else {
                        routeDate = this.getDateNow();
                        //TODO calendar date dont change
                        //this.routeDate = routeDate;
                        revrouteDate = this.getReversedDate(routeDate);
                    }
                    this._router.navigate(['Posts', { date: revrouteDate }]);
                };
                SearchbarComponent.prototype.getReversedDate = function (date) {
                    return date.split('-').reverse().join('-');
                };
                SearchbarComponent.prototype.getDateNow = function () {
                    //let dateNow = new Date().toISOString().slice(0, 10);
                    var currentDate = new Date();
                    var day = ("0" + currentDate.getDate()).slice(-2);
                    var month = ("0" + (currentDate.getMonth() + 1)).slice(-2);
                    var year = currentDate.getFullYear();
                    return [year, month, day].join('-');
                };
                SearchbarComponent = __decorate([
                    core_1.Component({
                        selector: 'my-searchbar',
                        templateUrl: static_1.SrcURL + 'posts/searchbar/searchbar.html',
                        styleUrls: [static_1.SrcURL + 'posts/searchbar/searchbar.css'],
                        directives: [],
                        providers: [],
                    }), 
                    __metadata('design:paramtypes', [router_1.Router, router_2.RouteParams])
                ], SearchbarComponent);
                return SearchbarComponent;
            })();
            exports_1("SearchbarComponent", SearchbarComponent);
        }
    }
});
//# sourceMappingURL=searchbar.component.js.map