import { Component } from '@angular/core';
import { UrlsListComponent } from "../../components/urls-list/urls-list.component";

@Component({
  selector: 'app-urls-page',
  imports: [UrlsListComponent],
  templateUrl: './urls-page.component.html',
})
export class UrlsPageComponent { }
