import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppComponent } from './app.component';
import { RecipesListComponent } from './components/recipesComponent/recipes.component';
import { CreateRecipeComponent } from './components/createRecipeComponent/createRecipe.component';

import { MatInputModule,
  MatListModule,
  MatIconModule,
  MatButtonModule,
  MatDialogModule,
  MatSelectModule,
  MatAutocompleteModule,
  MatSnackBarModule,
  MatChipsModule
 } from '@angular/material';
 import { HttpClientModule } from '@angular/common/http';
 import { RestService } from './services/rest-service';
 import { ReactiveFormsModule, FormsModule } from '@angular/forms';
 import { FilterPipe } from './components/recipesComponent/filter.pipe';
 import { routing } from './app.routing';
 import { DetailComponent } from './components/detailComponent/detail.component';

 import { ImageUploadModule } from 'angular2-image-upload';

@NgModule({
  declarations: [
    AppComponent,
    RecipesListComponent,
    CreateRecipeComponent,
    DetailComponent,
    FilterPipe,
  ],
  imports: [
    routing,
    BrowserModule,
    BrowserAnimationsModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule,
    MatInputModule,
    MatListModule,
    MatIconModule,
    MatButtonModule,
    MatDialogModule,
    MatSelectModule,
    MatAutocompleteModule,
    MatSnackBarModule,
    MatChipsModule,
    ImageUploadModule.forRoot()
  ],
  entryComponents: [
    CreateRecipeComponent
  ],
  providers: [
    RestService
    // {provide: MAT_DIALOG_DEFAULT_OPTIONS, useValue: {hasBackdrop: false}}
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
