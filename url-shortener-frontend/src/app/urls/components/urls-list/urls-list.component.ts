import { Component, input } from '@angular/core';
import { UrlInfo } from '../../interfaces/url-info.interface';

@Component({
  selector: 'app-urls-list',
  imports: [],
  templateUrl: './urls-list.component.html',
})
export class UrlsListComponent {

  urls = input.required<UrlInfo[]>();

}
