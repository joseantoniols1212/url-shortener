import { inject } from "@angular/core";
import { AuthService } from "../../auth/services/authService.service";
import { CanMatchFn, Router } from "@angular/router";

export const IsAuthenticated: CanMatchFn = () => {
    const authService = inject(AuthService);
    const router = inject(Router);

    const isAuthenticated = !!authService.userId();

    console.log(authService.userId());

    return isAuthenticated? router.createUrlTree(["/dashboard"]) : true;
};