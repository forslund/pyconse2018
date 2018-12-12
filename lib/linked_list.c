#include <stdio.h>
#include <stdlib.h>
#include "linked_list.h"

char *version = "0.1.0";


element_t * new_element(void)
{
    element_t *new;
    new = malloc(sizeof(element_t));
    new->val = NULL;
    new->next = NULL;
    return new;
}


element_t * new_list(void)
{
    return new_element();
}


void append_val(element_t *list, int val)
{
    element_t *new, *last = list;
    printf("%p, %d\n", list, val);
    // If the first element is unused add value to that one
    if (last->val != NULL)
    {
        for (last = list; last->next != NULL; last = last->next)
        {
           ; // loop until the last element is found
        }

        new = new_element();
        last->next = new;
        last = new;
    }
    last->val = malloc(sizeof(int));
    *last->val = val;
}


element_t *get_element_indexed(element_t * list, int index)
{
    element_t * e = list;
    int i;
    for (i = 0; e != NULL; e = e->next, i++)
    {
        if (i == index)
            break;
    }
    return e;
}

int divide(int i)
{
    return 123 / i;
}
