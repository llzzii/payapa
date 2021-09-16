import { HttpClient, HttpHeaders, HttpParams } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable, throwError as observableThrowError } from "rxjs";
import { catchError, map, mergeMap, tap, timeout } from "rxjs/operators";

let httpOptions = {
  headers: new HttpHeaders({
    "Content-Type": "application/json",
    withCredentials: "true",
  }),
};

@Injectable({
  providedIn: "root",
})
export class CrawlerService {
  constructor(private http: HttpClient) {}

  getProjectDatas(pageNo, pageSize): Observable<any> {
    let url = `/api/project?pageNo=${pageNo}&&pageSize=${pageSize}`;
    return this.http.get(url).pipe(tap((response) => response));
  }

  addProject(data): Observable<any> {
    let url = `/api/project`;
    return this.http
      .post(url, JSON.stringify(data), httpOptions)
      .pipe(tap((response) => response));
  }

  updateProject(id, data): Observable<any> {
    let url = `/api/project?id=${id}`;
    return this.http
      .put(url, JSON.stringify(data), httpOptions)
      .pipe(tap((response) => response));
  }

  deleteProject(id): Observable<any> {
    let url = `/api/project?id=${id}`;
    return this.http.delete(url).pipe(tap((response) => response));
  }

  projectAction(id): Observable<any> {
    let url = `/api/project/action?pId=${id}`;
    return this.http.get(url).pipe(tap((response) => response));
  }

  listDb(): Observable<any> {
    let url = `/api/data_project`;
    return this.http.get(url).pipe(tap((response) => response));
  }

  listByProject(project, pageNo, pageSize): Observable<any> {
    let url = `/api/data?pageNo=${pageNo}&&pageSize=${pageSize}&&project=${project}`;
    return this.http.get(url).pipe(tap((response) => response));
  }
}
