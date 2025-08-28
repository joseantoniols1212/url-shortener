import { DashboardPageComponent } from './urls/pages/dashboard-page/dashboard-page.component';
import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: 'login',
        loadComponent: () => import('./auth/pages/login-page/login-page.component').then(m => m.LoginPageComponent)
    },
    {
        path: 'register',
        loadComponent: () => import('./auth/pages/register-page/register-page.component').then(m => m.RegisterPageComponent)
    },
    {
        path: 'dashboard',
        loadComponent: () => import('./urls/pages/dashboard-page/dashboard-page.component').then(m => m.DashboardPageComponent),
        children: [
            {
                path: 'urls',
                loadComponent: () => import('./urls/pages/urls-page/urls-page.component').then(m => m.UrlsPageComponent),
            },
            {
                path: 'create-url',
                loadComponent: () => import('./urls/pages/short-url-creation-page/short-url-creation-page.component').then(m => m.ShortUrlCreationPageComponent),
            },
            {
                path: 'statistics',
                loadComponent: () => import('./urls/pages/statistics-page/statistics-page.component').then(m => m.StatisticsPageComponent),
            }
        ]
    },
    {
        path: '**',
        redirectTo: 'login'
    }
];
