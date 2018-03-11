import { Component, Output, EventEmitter } from '@angular/core';


@Component({
    selector: 'app-image-upload',
    templateUrl: 'imageUpload.component.html',
})
export class ImageUploadComponent
{
    @Output() imageChanged: EventEmitter<File>;

    constructor()
    {
        this.imageChanged = new EventEmitter<File>();
    }
}
