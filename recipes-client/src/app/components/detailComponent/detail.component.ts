import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { RestService } from '../../services/rest-service';
import { Recipe } from '../../model/Recipe';
import { ECategory } from '../../model/ECategory';

@Component({
    selector: 'app-detail',
    templateUrl: 'detail.component.html',
})
export class DetailComponent implements OnInit
{
    recipe: Recipe;
    category: string;

    constructor(
        private route: ActivatedRoute,
        private router: Router,
        private restService: RestService
    )
    {
    }

    ngOnInit(): void
    {
        const id = this.route.snapshot.url[1].path;
        this.restService.getRecepe(parseInt(id, 0)).subscribe(result =>
        {
            this.category = ECategory[result.category];
            this.recipe = result;
        });
    }

    backClick()
    {
        this.router.navigate(['']);
    }
}
