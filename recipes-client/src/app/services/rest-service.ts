import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Recipe } from '../model/Recipe';
import { Observable } from 'rxjs/Observable';


@Injectable()
export class RestService
{
    // endpoint = 'http://localhost:5000/';
    endpoint = 'http://192.168.178.25:5000/';

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
        console.log(JSON.stringify(recepe));
        return this.postRequest<Recipe>('recepes/new', JSON.stringify(recepe));
    }

    private getRequest<T>(path: string, headers: HttpHeaders = null, params: HttpParams = null)
    {
        if (headers === null)
        {
            headers = new HttpHeaders({'Content-Type': 'application/json; charset=utf-8'});
            headers.append('Content-Type', 'application/json; charset=utf-8');       // not working -> bug in angular
        }

        return this.http.get<T>(this.endpoint.concat(path), { 'headers': headers, 'params': params});
    }

    private postRequest<T>(path: string, body: string, headers: HttpHeaders = null, params: HttpParams = null)
    {
        if (headers === null)
        {
            headers = new HttpHeaders().set('Content-Type', 'application/json; charset=utf-8');
        }

        return this.http.post<T>(this.endpoint.concat(path), body, { 'headers': headers, 'params': params});
    }
}
