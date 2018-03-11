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

    fileChangeEvent(fileInput: any)
    {
        console.log(fileInput);
        if (fileInput.target.files)
        {
            console.log(fileInput.target.files[0]);
            this.imageChanged.next(fileInput.target.files[0]);
        }
    }
}
