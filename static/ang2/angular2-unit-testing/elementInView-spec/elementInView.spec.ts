import {elementInView} from "../../app/helpers/elementInView";
import {mockPostChildren} from "./mock-PostsChildren";

describe('elementInView spec', () => {
    let ev:any;

    beforeEach(() => {
        let mockPostChildrens = [new mockPostChildren(0, 200), new mockPostChildren(200, 300), new mockPostChildren(500, 300)];

        // first property for QueryList.first
        mockPostChildrens.first = mockPostChildrens[0];
        ev = new elementInView();
        ev.updatePostsDimension(mockPostChildrens);

    });
    it('is post changed', () => {
        ev.updateCurrent(0);
        expect(ev.isPostChanged()).toBe(false);

        for (let position = 0; position < 201; position++) {
            ev.updateCurrent(position);
            expect(ev.isPostChanged()).toBe(false);
        }

        ev.updateCurrent(499);
        expect(ev.isPostChanged()).toBe(true);

        for (let position = 200; position < 501; position++) {
            ev.updateCurrent(position);
            expect(ev.isPostChanged()).toBe(false);
        }

        ev.updateCurrent(650);
        expect(ev.isPostChanged()).toBe(true);

        for (let position = 500; position < 801; position++) {
            ev.updateCurrent(position);
            expect(ev.isPostChanged()).toBe(false);
        }

    });

    it('get current', () => {
        for (let position = 0; position < 201; position++) {
            ev.updateCurrent(position);
            expect(ev.getCurrent()).toBe(0);
        }

        for (let position = 201; position < 501; position++) {
            ev.updateCurrent(position);
            expect(ev.getCurrent()).toBe(1);
        }

        for (let position = 501; position < 801; position++) {
            ev.updateCurrent(position);
            expect(ev.getCurrent()).toBe(2);
        }

    });

});

