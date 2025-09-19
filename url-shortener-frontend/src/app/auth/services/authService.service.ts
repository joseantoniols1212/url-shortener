import { IsAuthenticated } from './../../shared/guards/isAuthenticated.guard';
import { HttpClient } from '@angular/common/http';
import { computed, Injectable, signal, inject } from '@angular/core';
import type { JWTPayload } from "jose";
import {
    decodeJwt
} from "jose";
import { firstValueFrom, map, Observable, tap } from 'rxjs';
import { environment } from '../../../environments/environment';

const baseUrl = environment.baseUrl;


@Injectable({providedIn: 'root'})
export class AuthService {

    http = inject(HttpClient);

    private decode(token: string): JWTPayload {
        let payload = null;

        try {
            payload = decodeJwt(token);
        } finally {
            localStorage.removeItem("token");
            return payload;
        }
    }

    storedToken = signal(localStorage.getItem("token"));
    claims = computed(() =>  {
        const token = this.storedToken();
        return token? this.decode(token) : null
    });
    userId = computed(() => this.claims()?.sub)
    isAuthenticated = computed(() => !!this.storedToken())

    logout() {
        localStorage.removeItem("token");
        this.storedToken.set(null);
    }

    async login(email: string, password: string) {
        await firstValueFrom(this.http.post<{ token: string }>(`${baseUrl}/auth/login`, {
            email,
            password
        }).pipe(
            tap(console.log),
            map(reponse => reponse.token),
            tap(token => localStorage.setItem("token", token)),
            tap(token => this.storedToken.set(token))
        ));
    };

}