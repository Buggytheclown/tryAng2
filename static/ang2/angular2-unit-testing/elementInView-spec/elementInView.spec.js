System.register(["../../app/helpers/elementInView", "./mock-PostsChildren"], function(exports_1) {
    var elementInView_1, mock_PostsChildren_1;
    return {
        setters:[
            function (elementInView_1_1) {
                elementInView_1 = elementInView_1_1;
            },
            function (mock_PostsChildren_1_1) {
                mock_PostsChildren_1 = mock_PostsChildren_1_1;
            }],
        execute: function() {
            describe('elementInView spec', function () {
                var ev;
                beforeEach(function () {
                    var mockPostChildrens = [new mock_PostsChildren_1.mockPostChildren(0, 200), new mock_PostsChildren_1.mockPostChildren(200, 300), new mock_PostsChildren_1.mockPostChildren(500, 300)];
                    // first property for QueryList.first
                    mockPostChildrens.first = mockPostChildrens[0];
                    ev = new elementInView_1.elementInView();
                    ev.updatePostsDimension(mockPostChildrens);
                });
                it('is post changed', function () {
                    ev.updateCurrent(0);
                    expect(ev.isPostChanged()).toBe(false);
                    for (var position = 0; position < 201; position++) {
                        ev.updateCurrent(position);
                        expect(ev.isPostChanged()).toBe(false);
                    }
                    ev.updateCurrent(499);
                    expect(ev.isPostChanged()).toBe(true);
                    for (var position = 200; position < 501; position++) {
                        ev.updateCurrent(position);
                        expect(ev.isPostChanged()).toBe(false);
                    }
                    ev.updateCurrent(650);
                    expect(ev.isPostChanged()).toBe(true);
                    for (var position = 500; position < 801; position++) {
                        ev.updateCurrent(position);
                        expect(ev.isPostChanged()).toBe(false);
                    }
                });
                it('get current', function () {
                    for (var position = 0; position < 201; position++) {
                        ev.updateCurrent(position);
                        expect(ev.getCurrent()).toBe(0);
                    }
                    for (var position = 201; position < 501; position++) {
                        ev.updateCurrent(position);
                        expect(ev.getCurrent()).toBe(1);
                    }
                    for (var position = 501; position < 801; position++) {
                        ev.updateCurrent(position);
                        expect(ev.getCurrent()).toBe(2);
                    }
                });
            });
        }
    }
});
//# sourceMappingURL=elementInView.spec.js.map