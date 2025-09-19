import { Component, effect, inject, signal } from '@angular/core';
import { Router, RouterLink } from '@angular/router';
import { AuthService } from '../../services/authService.service';

@Component({
  selector: 'app-login-page',
  imports: [RouterLink],
  templateUrl: './login-page.component.html',
})
export class LoginPageComponent {

  authService = inject(AuthService);
  router = inject(Router);

  isWaitingAuth = signal(false);

  redirect$ = effect(() => {
    if (this.authService.isAuthenticated()) this.router.navigate(["/dashboard/url"]);
  });

  async onClick(email: string, password: string) {
    this.authService.login(email, password);
    this.isWaitingAuth.set(true);
  }

}