import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { RestService } from '../../services/rest-service';
import { Recipe } from '../../model/Recipe';
import { ECategory } from '../../model/ECategory';
import { backendURL } from '../../utils/const';

@Component({
    selector: 'app-detail',
    templateUrl: 'detail.component.html',
    styleUrls: ['detail.component.css']
})
export class DetailComponent implements OnInit
{
    recipe: Recipe;
    category: string;
    imageSources: string[];

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
        const imgUrl = backendURL.concat('images/');
        this.restService.getRecepe(parseInt(id, 0)).subscribe(result =>
        {
            this.category = ECategory[result.category];
            this.recipe = result;

            this.imageSources = this.recipe.images.map(imgId => imgUrl.concat(imgId));
        });
    }

    backClick()
    {
        this.router.navigate(['']);
    }
}
