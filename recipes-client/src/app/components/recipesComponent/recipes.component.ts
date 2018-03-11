import { Component, OnInit } from '@angular/core';
import {DomSanitizer} from '@angular/platform-browser';
import { MatIconRegistry, MatDialog } from '@angular/material';
import { ECategory } from '../../model/ECategory';
import { RestService } from '../../services/rest-service';
import { Part } from '../../model/Part';
import { FormControl } from '@angular/forms';
import { Observable } from 'rxjs/Observable';
import {startWith} from 'rxjs/operators/startWith';
import {map} from 'rxjs/operators/map';
import { Recipe } from '../../model/Recipe';
import { CreateRecipeComponent } from '../createRecipeComponent/createRecipe.component';
import { Router } from '@angular/router';
/**
 * @title List with sections
 */
@Component({
    selector: 'app-recipes-list',
    styleUrls: ['recipes-list.css'],
    templateUrl: 'recipes.component.html',
})
export class RecipesListComponent implements OnInit
{
    myControl: FormControl = new FormControl();
    options = [];
    filteredOptions: Observable<string[]>;

    data: any[] = [];

    constructor(
        private dialog: MatDialog,
        private router: Router,
        private restService: RestService)
    {
    }

    ngOnInit()
    {
        this.loadRecipes();

        this.filteredOptions = this.myControl.valueChanges.pipe(
            startWith(''),
            map(val => this.filter(val))
        );
    }

    create()
    {
        const dialogRef = this.dialog.open(CreateRecipeComponent, {
            hasBackdrop: false
        });

        dialogRef.afterClosed().subscribe(addedRecipe =>
        {
            if (addedRecipe)
            {
                this.loadRecipes();
            }
        });
    }

    filter(val: string): string[]
    {
        return this.options.filter(option => option.toLowerCase().indexOf(val.toLowerCase()) === 0);
    }

    itemClick(item: Recipe)
    {
        // console.log(item);
        const t = '/recipe/' + item.id;
        this.router.navigate([t]);
    }

    queryResultSected(event: any)
    {
        const recipeName = event.source.value;
        this.data.forEach(part => {
            if (part.recipes)
            {
                const clickedRecipe = part.recipes.find(recipe => recipe.name === recipeName);
                if (clickedRecipe)
                {
                    this.itemClick(clickedRecipe);
                    return;
                }
            }
        });
        console.log("item not found");
    }

    private loadRecipes()
    {
        this.restService.getRecepes().subscribe(
            recepes =>
            {
                this.data = [];
                const tmpRecepeList = [];
                recepes.forEach(recepe => {
                    if (!tmpRecepeList[recepe.category])
                    {
                        tmpRecepeList[recepe.category] = [];
                    }
                    tmpRecepeList[recepe.category].push(recepe);
                });

                for (const enumMember in ECategory)
                {
                    if (parseInt(enumMember, 10) >= 0)
                    {
                        this.data.push({
                            category: ECategory[enumMember],
                            recipes: tmpRecepeList[enumMember]
                        });
                    }
                }

                // update options-list
                this.options = [];
                this.data.forEach(part =>
                {
                    if (part.recipes)
                    {
                        this.options = this.options.concat(part.recipes.map(recipe => recipe.name));
                    }
                });
            }
        );

    }
}
