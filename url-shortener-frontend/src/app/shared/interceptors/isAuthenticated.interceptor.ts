import { inject } from "@angular/core";
import { AuthService } from "../../auth/services/authService.service";
import { ActivatedRouteSnapshot, CanActivateFn, RedirectCommand, Router, RouterStateSnapshot } from "@angular/router";

export const IsAuthenticated: CanActivateFn = (route: ActivatedRouteSnapshot, state: RouterStateSnapshot) => {
    const authService = inject(AuthService);
    const router = inject(Router);

    const isAuthenticated = !!authService.userId();

    console.log(isAuthenticated);

    if (isAuthenticated) {
        const homePath = router.parseUrl("")
        return new RedirectCommand(homePath, {skipLocationChange: true})
    }

    return true;
};