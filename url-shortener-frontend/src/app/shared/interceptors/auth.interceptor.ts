import { HttpInterceptorFn } from "@angular/common/http";
import { inject } from "@angular/core";
import { Router } from "@angular/router";
import { AuthService } from "../../auth/services/authService.service";
import { catchError, throwError } from "rxjs";

export const authInterceptor: HttpInterceptorFn = (req, next) => {
    const authService = inject(AuthService);
    const router = inject(Router);
    const token = authService.storedToken();


    const authReq = token
    ? req.clone({ setHeaders: { Authorization: `Bearer ${token}` } })
    : req;

    return next(authReq).pipe(
        catchError(err => {
        if (err.status === 401) {
            authService.logout();
            router.navigate(['/login'], { queryParams: { redirectTo: router.url } });
        }
        return throwError(() => err);
        })
    ); 
}   