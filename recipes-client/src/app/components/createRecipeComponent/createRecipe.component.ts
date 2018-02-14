import {Component, Inject} from '@angular/core';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA, MatSnackBar } from '@angular/material';
import { ECategory } from '../../model/ECategory';
import { RestService } from '../../services/rest-service';
import { Recipe } from '../../model/Recipe';
import {MatChipInputEvent} from '@angular/material';
import {ENTER, COMMA} from '@angular/cdk/keycodes';

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

    // chips control
    visible = true;
    selectable = true;
    removable = true;
    addOnBlur = true;

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


    // Enter, comma
    separatorKeysCodes = [ENTER, COMMA];

    fruits = [
      { name: 'Lemon' },
      { name: 'Lime' },
      { name: 'Apple' },
    ];

    add(event: MatChipInputEvent): void {
      let input = event.input;
      let value = event.value;

      // Add our fruit
      if ((value || '').trim()) {
        this.fruits.push({ name: value.trim() });
      }

      // Reset the input value
      if (input) {
        input.value = '';
      }
    }

    remove(fruit: any): void {
      let index = this.fruits.indexOf(fruit);

      if (index >= 0) {
        this.fruits.splice(index, 1);
      }
    }

    createRecepe()
    {
        const newRecepe = new Recipe();
        newRecepe.category = ECategory[this.selectedCategory];
        newRecepe.description = this.description;
        newRecepe.name = this.name;
        if (!newRecepe.category || !newRecepe.description || !newRecepe.name)
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
