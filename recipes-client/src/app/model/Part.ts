import { Recipe } from './Recipe';
import { ECategory } from './ECategory';

export class Part
{
    category: ECategory;
    recepes: Recipe[] = [];

    constructor(category: ECategory)
    {
        this.category = category;
    }
}
