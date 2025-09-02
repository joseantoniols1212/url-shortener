import { Component, signal } from '@angular/core';
import { ModalComponent } from "../../../shared/components/modal/modal.component";

@Component({
  selector: 'app-short-url-creation-page',
  imports: [ModalComponent],
  templateUrl: './short-url-creation-page.component.html',
})
export class ShortUrlCreationPageComponent {

  modalId = signal('short-url-creation-form-modal')

  openModal() {
    const modal = document.getElementById(this.modalId()) as HTMLDialogElement;
    if (modal) {
      modal.showModal();
    }
  }
}