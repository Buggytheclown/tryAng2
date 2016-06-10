System.register(["angular2/http"], function(exports_1) {
    var http_1;
    var headersUnsafe;
    return {
        setters:[
            function (http_1_1) {
                http_1 = http_1_1;
            }],
        execute: function() {
            headersUnsafe = (function () {
                function headersUnsafe() {
                }
                headersUnsafe.prototype.getHeaders = function () {
                    var headers = new http_1.Headers();
                    headers.append('X-CSRFToken', this.getCookie('csrftoken'));
                    headers.append('Content-Type', 'application/json');
                    return { headers: headers };
                };
                headersUnsafe.prototype.getCookie = function (name) {
                    var value = "; " + document.cookie;
                    var parts = value.split("; " + name + "=");
                    if (parts.length == 2)
                        return parts.pop().split(";").shift();
                };
                return headersUnsafe;
            })();
            exports_1("headersUnsafe", headersUnsafe);
        }
    }
});
//# sourceMappingURL=headersUnsafe.js.map