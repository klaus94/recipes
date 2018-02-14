import { Component } from '@angular/core';
import {DomSanitizer} from '@angular/platform-browser';
import { MatIconRegistry, MatDialog } from '@angular/material';
import { CreateRecipeComponent } from './components/createRecipeComponent/createRecipe.component';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.css']
})
export class AppComponent {
    title = 'recipes';

    constructor(
      iconRegistry: MatIconRegistry,
      sanitizer: DomSanitizer,
      private dialog: MatDialog)
    {
        iconRegistry.addSvgIcon('add',
            sanitizer.bypassSecurityTrustResourceUrl('assets/img/add.svg'));
        iconRegistry.addSvgIcon('folder',
            sanitizer.bypassSecurityTrustResourceUrl('assets/img/folder.svg'));
        iconRegistry.addSvgIcon('arrow_back',
            sanitizer.bypassSecurityTrustResourceUrl('assets/img/arrow_back.svg'));
        iconRegistry.addSvgIcon('close',
            sanitizer.bypassSecurityTrustResourceUrl('assets/img/close.svg'));
    }
}
