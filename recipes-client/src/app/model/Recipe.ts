import { ECategory } from './ECategory';

export class Recipe
{
    id: number;
    name: string;
    category: ECategory;
    description: string;
    incredients: string[];
    images: string[];
}
