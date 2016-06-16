System.register(['angular2/core', "../static", 'angular2/router', "./posts/posts.component", "./logger/logger.component", "./helpers/headersUnsafe", "./temp-study/blocknote/blocknote.component", "./temp-study/votes/votes.component"], function(exports_1) {
    var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
        var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
        if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
        else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
        return c > 3 && r && Object.defineProperty(target, key, r), r;
    };
    var __metadata = (this && this.__metadata) || function (k, v) {
        if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
    };
    var core_1, static_1, router_1, posts_component_1, logger_component_1, headersUnsafe_1, blocknote_component_1, votes_component_1;
    var MainComponent;
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
            },
            function (posts_component_1_1) {
                posts_component_1 = posts_component_1_1;
            },
            function (logger_component_1_1) {
                logger_component_1 = logger_component_1_1;
            },
            function (headersUnsafe_1_1) {
                headersUnsafe_1 = headersUnsafe_1_1;
            },
            function (blocknote_component_1_1) {
                blocknote_component_1 = blocknote_component_1_1;
            },
            function (votes_component_1_1) {
                votes_component_1 = votes_component_1_1;
            }],
        execute: function() {
            MainComponent = (function () {
                function MainComponent() {
                }
                MainComponent = __decorate([
                    core_1.Component({
                        selector: 'my-main',
                        templateUrl: static_1.SrcURL + 'myMain.html',
                        styleUrls: [static_1.SrcURL + 'myMain.css'],
                        directives: [router_1.ROUTER_DIRECTIVES, posts_component_1.PostsComponent, logger_component_1.LoggerComponent, votes_component_1.VotesComponent, blocknote_component_1.BlocknoteComponent],
                        providers: [router_1.ROUTER_PROVIDERS, headersUnsafe_1.headersUnsafe]
                    }),
                    router_1.RouteConfig([
                        {
                            path: '/posts',
                            name: 'Posts',
                            component: posts_component_1.PostsComponent,
                            useAsDefault: true
                        },
                        {
                            path: '/votes',
                            name: 'Votes',
                            component: votes_component_1.VotesComponent,
                        },
                        {
                            path: '/blocknote',
                            name: 'Blocknote',
                            component: blocknote_component_1.BlocknoteComponent
                        },
                        {
                            path: '/logger',
                            name: 'Logger',
                            component: logger_component_1.LoggerComponent
                        },
                    ]), 
                    __metadata('design:paramtypes', [])
                ], MainComponent);
                return MainComponent;
            })();
            exports_1("MainComponent", MainComponent);
        }
    }
});
//# sourceMappingURL=main.component.js.map