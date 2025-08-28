import { Component } from '@angular/core';
import { ThemeSwapComponent } from "./theme-swap/theme-swap.component";
import { RouterLinkActive, RouterLink } from "@angular/router";

@Component({
  selector: 'app-top-menu',
  imports: [ThemeSwapComponent, RouterLink, RouterLinkActive],
  templateUrl: './top-menu.component.html',
})
export class TopMenuComponent {
  items = [
    {
      label: 'Your URLs',
      url: '/dashboard/urls'
    },
    {
      label: 'Create URL',
      url: '/dashboard/create-url'
    },
    {
    label: 'Statistics',
      url: '/dashboard/statistics'
    }
  ];
}
