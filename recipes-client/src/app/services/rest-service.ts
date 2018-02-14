import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Recipe } from '../model/Recipe';
import { Observable } from 'rxjs/Observable';


@Injectable()
export class RestService
{
    endpoint = 'http://localhost:5000/';

    constructor( private http: HttpClient)
    { }

    getRecepes(): Observable<Recipe[]>
    {
        return this.getRequest<Recipe[]>('recepes/list');
    }

    getRecepe(id: number): Observable<Recipe>
    {
        return this.getRequest<Recipe>('recepes/' + id);
    }

    createRecepe(recepe: Recipe)
    {
        return this.postRequest<Recipe>('recepes/new', JSON.stringify(recepe));
    }

    private getRequest<T>(path: string, headers: HttpHeaders = null, params: HttpParams = null)
    {
        if (headers === null)
        {
            headers = new HttpHeaders({'Content-Type': 'application/json; charset=utf-8'});
            headers.append('Content-Type', 'application/json; charset=utf-8');       // not working -> bug in angular
        }

        // run get request
        return this.http.get<T>(this.endpoint.concat(path), { 'headers': headers, 'params': params});
    }

    private postRequest<T>(path: string, body: string, headers: HttpHeaders = null, params: HttpParams = null)
    {
        if (headers === null)
        {
            console.log(headers);
            headers = new HttpHeaders().set('Content-Type', 'application/json; charset=utf-8');
            console.log(headers);
        }

        return this.http.post<T>(this.endpoint.concat(path), body, { 'headers': headers, 'params': params});
    }
}
