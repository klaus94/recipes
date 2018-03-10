import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Recipe } from '../model/Recipe';
import { Observable } from 'rxjs/Observable';
import { backendURL } from '../utils/const';
import { RequestOptions, RequestOptionsArgs, Http } from '@angular/http';


@Injectable()
export class RestService
{
    constructor( private http: HttpClient, private imgHTTP: Http)
    { }

    getRecepes(): Observable<Recipe[]>
    {
        return this.getRequest<Recipe[]>('recepes/list');
    }

    getRecepe(id: number): Observable<Recipe>
    {
        return this.getRequest<Recipe>('recepes/' + id);
    }

    createRecepe(recepe: Recipe): any
    {
        console.log(JSON.stringify(recepe));
        return this.postRequest<Recipe>('recepes/new', JSON.stringify(recepe));
    }

    addImage(recepeID: number, image: File)
    {
        const url = backendURL.concat('images/new/' + recepeID.toString());
        const options: RequestOptionsArgs = new RequestOptions();
        const formData = new FormData();
        formData.append('image', image);
        return this.imgHTTP.post(url, formData, options);

    }

    private getRequest<T>(path: string, headers: HttpHeaders = null, params: HttpParams = null)
    {
        if (headers === null)
        {
            headers = new HttpHeaders({'Content-Type': 'application/json; charset=utf-8'});
            headers.append('Content-Type', 'application/json; charset=utf-8');       // not working -> bug in angular
        }

        return this.http.get<T>(backendURL.concat(path), { 'headers': headers, 'params': params});
    }

    private postRequest<T>(path: string, body: string, headers: HttpHeaders = null, params: HttpParams = null)
    {
        if (headers === null)
        {
            headers = new HttpHeaders().set('Content-Type', 'application/json; charset=utf-8');
        }

        return this.http.post<T>(backendURL.concat(path), body, { 'headers': headers, 'params': params});
    }
}
