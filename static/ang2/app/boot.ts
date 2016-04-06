import {bootstrap} from 'angular2/platform/browser';
import {MainComponent} from "./main.component";
import {ROUTER_PROVIDERS} from "angular2/router";
import {HTTP_PROVIDERS} from "angular2/http";
import {APP_BASE_HREF} from 'angular2/router';
import {provide} from 'angular2/core';

//noinspection TypeScriptValidateTypes
bootstrap(MainComponent, [ROUTER_PROVIDERS, provide(APP_BASE_HREF, {useValue : '/'}), HTTP_PROVIDERS]);