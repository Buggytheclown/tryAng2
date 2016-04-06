import {Component} from 'angular2/core';
import {SrcURL} from "../static";
import { RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from 'angular2/router';

import {PostsComponent} from "./posts/posts.component";
import {VotesComponent} from "./votes/votes.component";
import {CarouselComponent} from "./carousel/carousel.component";
import {CounterMainComponent} from "./counter/main-counter.component";
import {BlocknoteComponent} from "./blocknote/blocknote.component";



@Component({
    selector: 'my-main',
    templateUrl: SrcURL+'html/myMain.html',
    directives: [ROUTER_DIRECTIVES, PostsComponent, VotesComponent, BlocknoteComponent],
    providers: [ROUTER_PROVIDERS,]
})


@RouteConfig([
    {
        path: '/posts',
        name: 'Posts',
        component: PostsComponent,
        useAsDefault: true
    },
    {
        path: '/votes',
        name: 'Votes',
        component: VotesComponent,

    },
    {
      path: '/blocknote',
      name: 'Blocknote',
      component: BlocknoteComponent
    },

])


export class MainComponent {}