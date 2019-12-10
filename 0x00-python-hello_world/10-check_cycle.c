#include "lists.h"
#include <stddef.h>
#include <stdarg.h>
#include <stdio.h>

/**
* check_cycle - entry point
* @list: listint_t variable
* Return: 0 or 1
*/

int check_cycle(listint_t *list)
{
	if (list == NULL)
		return (0);
	while (list)
	{
		if ((list->next) >= list)
			return (1);
		list = list->next;
	}
	return (0);
}
