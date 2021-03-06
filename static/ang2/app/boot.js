System.register(['zone.js', 'reflect-metadata', 'es6-shim', 'angular2/platform/browser', "./main.component", "angular2/router", "angular2/http", 'angular2/router', 'angular2/core', 'angular2-jwt'], function(exports_1) {
    var browser_1, main_component_1, router_1, http_1, router_2, core_1, http_2, angular2_jwt_1, core_2;
    return {
        setters:[
            function (_1) {},
            function (_2) {},
            function (_3) {},
            function (browser_1_1) {
                browser_1 = browser_1_1;
            },
            function (main_component_1_1) {
                main_component_1 = main_component_1_1;
            },
            function (router_1_1) {
                router_1 = router_1_1;
            },
            function (http_1_1) {
                http_1 = http_1_1;
                http_2 = http_1_1;
            },
            function (router_2_1) {
                router_2 = router_2_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
                core_2 = core_1_1;
            },
            function (angular2_jwt_1_1) {
                angular2_jwt_1 = angular2_jwt_1_1;
            }],
        execute: function() {
            core_2.enableProdMode();
            //noinspection TypeScriptValidateTypes
            browser_1.bootstrap(main_component_1.MainComponent, [router_1.ROUTER_PROVIDERS, core_1.provide(router_2.APP_BASE_HREF, { useValue: '/' }), http_1.HTTP_PROVIDERS,
                core_1.provide(angular2_jwt_1.AuthHttp, {
                    useFactory: function (http) {
                        return new angular2_jwt_1.AuthHttp(new angular2_jwt_1.AuthConfig({
                            noJwtError: true,
                            headerPrefix: "JWT ",
                        }), http);
                    },
                    deps: [http_2.Http]
                })
            ]);
        }
    }
});
//# sourceMappingURL=boot.js.map