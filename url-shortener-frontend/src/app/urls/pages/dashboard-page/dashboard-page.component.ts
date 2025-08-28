import { Component } from '@angular/core';
import { TopMenuComponent } from "../../components/top-menu/top-menu.component";
import { RouterOutlet } from "@angular/router";

@Component({
  selector: 'app-dashboard-page',
  imports: [TopMenuComponent, RouterOutlet],
  templateUrl: './dashboard-page.component.html',
})
export class DashboardPageComponent { }
