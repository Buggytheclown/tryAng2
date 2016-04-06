System.register(['angular2/platform/browser', "./main.component", "angular2/router", "angular2/http", 'angular2/router', 'angular2/core'], function(exports_1) {
    var browser_1, main_component_1, router_1, http_1, router_2, core_1;
    return {
        setters:[
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
            },
            function (router_2_1) {
                router_2 = router_2_1;
            },
            function (core_1_1) {
                core_1 = core_1_1;
            }],
        execute: function() {
            //noinspection TypeScriptValidateTypes
            browser_1.bootstrap(main_component_1.MainComponent, [router_1.ROUTER_PROVIDERS, core_1.provide(router_2.APP_BASE_HREF, { useValue: '/' }), http_1.HTTP_PROVIDERS]);
        }
    }
});
//# sourceMappingURL=boot.js.map