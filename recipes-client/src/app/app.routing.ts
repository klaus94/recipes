import { Routes, RouterModule } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';
import { RecipesListComponent } from './components/recipesComponent/recipes.component';
import { DetailComponent } from './components/detailComponent/detail.component';
// order is important!
const routes: Routes = [
    { path: '', component: RecipesListComponent },
    { path: 'recipe/:id', component: DetailComponent },
    { path: '**', redirectTo: '' }

];

export const routing: ModuleWithProviders = RouterModule.forRoot(routes);
