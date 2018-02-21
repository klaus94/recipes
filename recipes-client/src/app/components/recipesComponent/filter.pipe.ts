import { Pipe, PipeTransform } from '@angular/core';
import { Recipe } from '../../model/Recipe';
@Pipe({
  name: 'filter'
})
export class FilterPipe implements PipeTransform
{
    transform(items: Recipe[], searchText: string): Recipe[]
    {
        if (!items)
        {
            return [];
        }
        if (!searchText)
        {
            return items;
        }
        searchText = searchText.toLowerCase();
        return items.filter( it =>
        {
            return it.name.toLowerCase().includes(searchText) ||
                it.description.toLocaleLowerCase().includes(searchText);
                // could also include incredients into search...
        });
    }
}
