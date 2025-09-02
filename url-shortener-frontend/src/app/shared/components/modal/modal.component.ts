import { Component, input } from '@angular/core';

@Component({
  selector: 'app-modal',
  imports: [],
  templateUrl: './modal.component.html',
})
export class ModalComponent {

  id = input.required<string>();
  textModal = input.required<string>();
  titleModal = input.required<string>();

  openModal() {
    const dialog = <HTMLDialogElement>document.getElementById(this.id());
    dialog?.showModal();
  }
}
