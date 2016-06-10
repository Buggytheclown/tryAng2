import {Component} from 'angular2/core';
import {SrcURL} from "../static";
import { RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from 'angular2/router';

import {PostsComponent} from "./posts/posts.component";
import {VotesComponent} from "./votes/votes.component";
import {BlocknoteComponent} from "./blocknote/blocknote.component";
import {LoggerComponent} from "./logger/logger.component";
import {FriendlistComponent} from "./posts/friendlist/friendlist.component";
import {headersUnsafe} from "./helpers/headersUnsafe";


@Component({
    selector: 'my-main',
    templateUrl: SrcURL + 'myMain.html',
    styleUrls: [SrcURL + 'myMain.css'],
    directives: [ROUTER_DIRECTIVES, PostsComponent, LoggerComponent, VotesComponent, BlocknoteComponent],
    providers: [ROUTER_PROVIDERS, headersUnsafe]
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
    {
        path: '/logger',
        name: 'Logger',
        component: LoggerComponent
    },
    {
        path: '/friendlist',
        name: 'Friendlist',
        component: FriendlistComponent
    },

])


export class MainComponent {
}