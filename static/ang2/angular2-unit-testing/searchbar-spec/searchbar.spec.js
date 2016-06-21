System.register(["../../app/searchbar/searchbar.component"], function(exports_1) {
    var searchbar_component_1;
    return {
        setters:[
            function (searchbar_component_1_1) {
                searchbar_component_1 = searchbar_component_1_1;
            }],
        execute: function() {
            describe('searchbar spec', function () {
                var mockRouter;
                var mockRouteParams;
                var getSerchbar;
                //___CONFIG___
                var TEST_COUNT = 100;
                function rndDate() {
                    var day = Math.ceil(Math.random() * 28);
                    var month = Math.ceil(Math.random() * 12);
                    var year = 2000 + Math.ceil(Math.random() * 15);
                    return day + '-' + month + '-' + year;
                }
                function reverseDate(date) {
                    return date.split('-').reverse().join('-');
                }
                beforeEach(function () {
                    mockRouter = {
                        'navArgs': [],
                        'navigate': function () {
                            var args = [];
                            for (var _i = 0; _i < arguments.length; _i++) {
                                args[_i - 0] = arguments[_i];
                            }
                            this.navArgs = args;
                        }
                    };
                    mockRouteParams = {
                        'date': '',
                        'param': '',
                        'get': function (param) {
                            this.param = param;
                            return this.date;
                        }
                    };
                    getSerchbar = function (date) {
                        mockRouteParams.date = date;
                        return new searchbar_component_1.SearchbarComponent(mockRouter, mockRouteParams);
                    };
                });
                it('date parsers', function () {
                    for (var i = 0; i < TEST_COUNT; i++) {
                        var someDate = rndDate();
                        var sbComp = getSerchbar(someDate);
                        var someDateRev = reverseDate(someDate);
                        sbComp.ngOnInit();
                        expect(sbComp.routeDate).toBe(someDateRev);
                        sbComp.routeIt(someDateRev);
                        expect(mockRouter.navArgs).toEqual([['Posts', { 'date': someDate }]]);
                    }
                });
            });
        }
    }
});
//# sourceMappingURL=searchbar.spec.js.map