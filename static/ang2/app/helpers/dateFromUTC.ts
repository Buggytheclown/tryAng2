import {Pipe} from "angular2/core";
import {PipeTransform} from "angular2/core";


@Pipe({name: 'dateFromUTC'})
export class DateFromUTCPipe implements PipeTransform {
  transform(utcSeconds: number): any {
    var d = new Date(0); // The 0 there is the key, which sets the date to the epoch
    return d.setUTCSeconds(utcSeconds);
  }
}