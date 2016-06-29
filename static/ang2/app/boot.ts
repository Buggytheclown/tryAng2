import 'zone.js';
import 'reflect-metadata';
import 'es6-shim';

import {bootstrap} from 'angular2/platform/browser';
import {MainComponent} from "./main.component";
import {ROUTER_PROVIDERS} from "angular2/router";
import {HTTP_PROVIDERS} from "angular2/http";
import {APP_BASE_HREF} from 'angular2/router';
import {provide} from 'angular2/core';
import {Http} from "angular2/http";
import {AuthHttp, AuthConfig} from 'angular2-jwt';
import {enableProdMode} from 'angular2/core';

enableProdMode();

//noinspection TypeScriptValidateTypes
bootstrap(MainComponent,
    [ROUTER_PROVIDERS, provide(APP_BASE_HREF, {useValue : '/'}), HTTP_PROVIDERS,
        provide(AuthHttp, {
            useFactory: (http) => {
                return new AuthHttp(new AuthConfig({
                    noJwtError: true,
                    headerPrefix: "JWT ",
                }), http);
            },
        deps: [Http]
        })
    ]);