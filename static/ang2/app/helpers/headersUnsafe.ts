import {Headers} from "angular2/http";


export class headersUnsafe {
    getHeaders() {
        let headers = new Headers();
        headers.append('X-CSRFToken', this.getCookie('csrftoken'));
        headers.append('Content-Type', 'application/json');
        return {headers: headers}
    }

    getCookie(name) {
        let value = "; " + document.cookie;
        let parts = value.split("; " + name + "=");
        if (parts.length == 2)
            return parts.pop().split(";").shift();
    }
}