import {SearchbarComponent} from "../../app/searchbar/searchbar.component";

describe('searchbar spec', () => {
    let mockRouter:any;
    let mockRouteParams:any;
    let getSerchbar:any;

    //___CONFIG___
    let TEST_COUNT:number = 100;

    function rndDate():string {
        let day = Math.ceil(Math.random() * 28);
        let month = Math.ceil(Math.random() * 12);
        let year = 2000 + Math.ceil(Math.random() * 15);
        return day + '-' + month + '-' + year
    }

    function reverseDate(date:string):string {
        return date.split('-').reverse().join('-')
    }

    beforeEach(() => {
        mockRouter = {
            'navArgs': [],
            'navigate': function (...args:Array<any>) {
                this.navArgs = args;
            }
        };

        mockRouteParams = {
            'date': '',
            'param': '',
            'get': function (param:string) {
                this.param = param;
                return this.date;
            }
        };

        getSerchbar = function (date:string) {
            mockRouteParams.date = date;
            return new SearchbarComponent(mockRouter, mockRouteParams)
        }
    });

    it('date parsers', () => {
        for (let i = 0; i < TEST_COUNT; i++) {
            let someDate = rndDate();
            let sbComp = getSerchbar(someDate);
            let someDateRev = reverseDate(someDate);

            sbComp.ngOnInit();
            expect(sbComp.routeDate).toBe(someDateRev);

            sbComp.routeIt(someDateRev);
            expect(mockRouter.navArgs).toEqual([['Posts', {'date': someDate}]])
        }
    });

});