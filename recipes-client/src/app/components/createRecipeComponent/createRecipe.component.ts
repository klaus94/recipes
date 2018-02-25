import {Component, Inject} from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA, MatSnackBar } from '@angular/material';
import { ECategory } from '../../model/ECategory';
import { RestService } from '../../services/rest-service';
import { Recipe } from '../../model/Recipe';
import {MatChipInputEvent} from '@angular/material';
import {ENTER, COMMA} from '@angular/cdk/keycodes';
import { backendURL } from '../../utils/const';

@Component({
    selector: 'create-dialog',
    styleUrls: ['createRecipe.component.css'],
    templateUrl: 'createRecipe.component.html',
})
export class CreateRecipeComponent
{
    name = '';
    description = '';
    categories: string[] = [];
    selectedCategory = '';
    createID = Math.floor(Math.random() * 100000);  // unique id for this creation
    uploadURL = backendURL + 'images/new/' + '1'; //this.createID.toString();

    // chips control
    visible = true;
    selectable = true;
    removable = true;
    addOnBlur = true;
    // Enter, comma
    separatorKeysCodes = [ENTER, COMMA];
    incredients = [];

    constructor(
        public dialogRef: MatDialogRef<CreateRecipeComponent>,
        public snackbar: MatSnackBar,
        private restService: RestService)
    {
        for (const enumMember in ECategory)
        {
            if (parseInt(enumMember, 10) >= 0)
            {
                this.categories.push(ECategory[enumMember]);
            }
        }
    }

    add(event: MatChipInputEvent): void
    {
        const input = event.input;
        const value = event.value;

        // Add our incredient
        if ((value || '').trim()) {
            this.incredients.push(value.trim());
        }

        // Reset the input value
        if (input) {
            input.value = '';
        }
    }

    remove(incredient: any): void
    {
        const index = this.incredients.indexOf(incredient);

        if (index >= 0) {
            this.incredients.splice(index, 1);
        }
    }

    createRecepe()
    {
        const newRecepe = new Recipe();
        newRecepe.category = ECategory[this.selectedCategory];
        newRecepe.description = this.description;
        newRecepe.name = this.name;
        newRecepe.incredients = this.incredients;

        if (newRecepe.category === undefined || newRecepe.description === undefined || !newRecepe.name)
        {
            this.openSnackbar('important entry is missing...');
            return;
        }

        this.restService.createRecepe(newRecepe).subscribe(
              actionResult => console.log(actionResult),
              error => console.log(error));

        this.openSnackbar('success');

        this.dialogRef.close(true);
    }

    onNoClick(): void
    {
        this.dialogRef.close(false);
    }

    private openSnackbar(text: string)
    {
        this.snackbar.open(text, null, {
            duration: 2000,
          });
    }
}
